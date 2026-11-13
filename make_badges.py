"""Redraw the AIOStreams pack using outlines from Barlow Semi Condensed Bold."""

import argparse
import json
import re
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parent
ASSET_URL = "https://raw.githubusercontent.com/Prokyro/aiostreams-selos/main"
# Plate face (top, shoulder, base), rim (light, dark), ink.
FINISHES = {
    "emerald": ("#176E56", "#124638", "#071E17", "#6EE0A9", "#268564", "#E1FFEF"),
    "sapphire": ("#255B80", "#17394F", "#0B1B2B", "#8FDDFF", "#407BA9", "#EAF8FF"),
    "platinum": ("#FFF9E9", "#E0C89A", "#B89A69", "#FFF8DE", "#A68453", "#241B10"),
    "resolution": ("#4A4F59", "#2E333B", "#191C23", "#C6CFDB", "#566171", "#F4F7FF"),
    "source": ("#563A29", "#342417", "#211811", "#E8AA73", "#9D6946", "#FFE4C9"),
    "dynamic": ("#5D4925", "#352816", "#221A0F", "#F4CE7B", "#A7793C", "#FFE8AB"),
    "codec": ("#394B63", "#222F44", "#151B2A", "#9FB8E3", "#586C93", "#E9F2FF"),
    "sound": ("#265451", "#183936", "#102221", "#83D2C7", "#437B75", "#DFFAF4"),
    "edition": ("#403B53", "#2B2838", "#1A1823", "#ACA4C8", "#635B80", "#EEE9FA"),
    "service": ("#3B4350", "#292F3A", "#171C24", "#9DAABF", "#525F73", "#E7EDF7"),
}

GROUP_FINISH = {
    "res": "resolution",
    "src": "source",
    "hdr": "dynamic",
    "enc": "codec",
    "audio": "sound",
    "ch": "sound",
    "aiostreams-selos-services": "service",
}

SPEAKER = """    <path fill="url(#icon)" d="M26.2 5.9h2.65l3.75-2.75a.6.6 0 0 1 .95.5v8.7a.6.6 0 0 1-.95.49l-3.75-2.74H26.2a.7.7 0 0 1-.7-.7V6.6a.7.7 0 0 1 .7-.7Z"/>
    <path d="M35.8 5.75a3.1 3.1 0 0 1 0 4.5m2.25-6.2a5.4 5.4 0 0 1 0 7.9" fill="none" stroke="url(#icon)" stroke-width="1.35" stroke-linecap="round"/>"""

CAPTIONS = """    <path fill="url(#icon)" d="M27 3.45h11a1.8 1.8 0 0 1 1.8 1.8v4.9a1.8 1.8 0 0 1-1.8 1.8h-6.1l-2.85 1.48a.42.42 0 0 1-.62-.37v-1.1H27a1.8 1.8 0 0 1-1.8-1.8v-4.9a1.8 1.8 0 0 1 1.8-1.8Z"/>
    <path d="M28.1 6.4h8.8m-8.8 2.65h6.2" fill="none" stroke="#173A53" stroke-width="1.23" stroke-linecap="round"/>"""


def number(value):
    return f"{value:.6f}".rstrip("0").rstrip(".")


def outline(label, font, ink):
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    shapes = []
    advance = 0
    for char in label:
        glyph = glyphs[cmap[ord(char)]]
        pen = SVGPathPen(glyphs, ntos=number)
        glyph.draw(pen)
        if pen.getCommands():
            bounds = BoundsPen(glyphs)
            glyph.draw(bounds)
            left, bottom, right, top = bounds.bounds
            shapes.append((advance, pen.getCommands(), (left + advance, bottom, right + advance, top)))
        advance += glyph.width + 18

    left = min(bounds[0] for _, _, bounds in shapes)
    right = max(bounds[2] for _, _, bounds in shapes)
    bottom = min(bounds[1] for _, _, bounds in shapes)
    top = max(bounds[3] for _, _, bounds in shapes)

    scale_y = (10 if label == "4K" else 9.1) / (top - bottom)
    max_ink_width = 77
    scale_x = min(scale_y, max_ink_width / (right - left))
    width = max(23, round((right - left) * scale_x + 9))
    x = (width - (left + right) * scale_x) / 2
    y = 8 + (bottom + top) * scale_y / 2
    transform = f"translate({number(x)} {number(y)}) scale({number(scale_x)} -{number(scale_y)})"
    paths = "\n".join(f'    <path transform="translate({dx})" d="{path}"/>' for dx, path, _ in shapes)
    return width, f'  <g transform="{transform}" fill="{ink}">\n{paths}\n  </g>'


def plate(width, finish, art, definitions="", flag=False):
    face, shoulder, base, highlight, rim, _ = FINISHES[finish]
    shade = "#382913" if finish == "platinum" else "#000"
    extra_namespace = ' xmlns:xlink="http://www.w3.org/1999/xlink"' if flag else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg"{extra_namespace} width="{width}" height="16" viewBox="0 0 {width} 16">
  <defs>
    <linearGradient id="face" x2=".22" y2="1">
      <stop stop-color="{face}"/>
      <stop offset=".45" stop-color="{shoulder}"/>
      <stop offset=".49" stop-color="{shoulder}"/>
      <stop offset="1" stop-color="{base}"/>
    </linearGradient>
    <linearGradient id="rim" x2=".4" y2="1">
      <stop stop-color="{highlight}"/>
      <stop offset=".42" stop-color="{rim}"/>
      <stop offset=".76" stop-color="{rim}"/>
      <stop offset="1" stop-color="{highlight}"/>
    </linearGradient>
    <linearGradient id="sheen">
      <stop stop-color="#FFF" stop-opacity=".44"/>
      <stop offset=".57" stop-color="#FFF" stop-opacity=".13"/>
      <stop offset="1" stop-color="#FFF" stop-opacity="0"/>
    </linearGradient>{definitions}
  </defs>
  <rect x=".2" y=".65" width="{number(width - .4)}" height="15.3" rx="3.4" fill="{shade}" opacity=".75"/>
  <rect x=".55" y=".5" width="{number(width - 1.1)}" height="14.45" rx="3.15" fill="url(#face)" stroke="url(#rim)" stroke-width=".95"/>
  <path d="M3.9 1.6h{number(width - 7.8)}" fill="none" stroke="url(#sheen)" stroke-width=".65" stroke-linecap="round"/>
{art}
</svg>
"""


def portuguese(flag_file, icon, finish):
    flag = flag_file.read_text(encoding="utf-8").strip()
    flag = re.sub(r'^<svg[^>]*>', '', flag).removesuffix("</svg>")
    flag = flag.replace('fill="#009440"', 'fill="#00A94F"', 1).replace('fill="#302681"', 'fill="#153789"', 1)
    definitions = """
    <clipPath id="flag-window"><rect x="3.5" y="2.1" width="17" height="11.9" rx="1.35"/></clipPath>
    <linearGradient id="enamel" x2=".16" y2="1">
      <stop stop-color="#FFF" stop-opacity=".32"/>
      <stop offset=".38" stop-color="#FFF" stop-opacity=".04"/>
      <stop offset=".63" stop-color="#000" stop-opacity="0"/>
      <stop offset="1" stop-color="#000" stop-opacity=".29"/>
    </linearGradient>
    <linearGradient id="icon" x2="0" y2="1">
      <stop stop-color="#FFF"/>
      <stop offset="1" stop-color="#DBEAF2"/>
    </linearGradient>"""
    art = f"""  <!-- Flag geometry from https://commons.wikimedia.org/wiki/File:Flag_of_Brazil.svg (public domain). -->
  <rect x="3" y="1.6" width="18" height="12.9" rx="1.8" fill="#07191A" stroke="#F9F8DA" stroke-opacity=".54" stroke-width=".5"/>
  <g clip-path="url(#flag-window)">
    <g transform="translate(12 8.05) scale(.004047619)">{flag}</g>
    <rect x="3.5" y="2.1" width="17" height="11.9" fill="url(#enamel)"/>
  </g>
  <path d="M22.7 4.1v7.8" stroke="#EDF9FF" stroke-width=".6" opacity=".26"/>
{icon}"""
    return plate(44, finish, art, definitions, flag=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", type=Path, required=True)
    parser.add_argument("--flag", type=Path, required=True)
    options = parser.parse_args()

    font = TTFont(options.font)
    manifest = ROOT / "badges.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    used = set()
    for badge in data["badges"]:
        label = badge["label"]
        pattern = badge["match"]
        if pattern == "^Audio PT confirmado$":
            asset, finish = "pt/audio.svg", "emerald"
            badge["label"] = "Áudio em português do Brasil"
            svg = portuguese(options.flag, SPEAKER, finish)
        elif pattern == "^Legenda PT confirmada$":
            asset, finish = "pt/subs.svg", "sapphire"
            badge["label"] = "Legendas em português do Brasil"
            svg = portuguese(options.flag, CAPTIONS, finish)
        else:
            group = badge.get("group")
            finish = GROUP_FINISH.get(group, "edition")
            if label == "4K":
                finish = "platinum"
            elif label in {"IMAX", "10BIT", "CRITERION"}:
                finish = "dynamic"
            slug = re.sub(r"[^a-z0-9]+", "-", label.lower().replace("+", " plus ").replace("&", " and ")).strip("-")
            asset = f"selos/{slug}.svg"
            width, art = outline(label, font, FINISHES[finish][-1])
            svg = plate(width, finish, art)
        if asset in used:
            raise ValueError(f"Duplicate asset path: {asset}")
        used.add(asset)

        destination = ROOT / asset
        destination.parent.mkdir(exist_ok=True)
        destination.write_text(svg, encoding="utf-8", newline="\n")
        badge["color"] = FINISHES[finish][-1] if finish != "platinum" else "#FFE8AB"
        badge.pop("background", None)
        badge.pop("border", None)
        badge["image"] = f"{ASSET_URL}/{asset}?v=3"

    manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
