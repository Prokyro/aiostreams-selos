"""Regenerate the typographic badges from Barlow Semi Condensed Bold."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parent
FINISHES = {
    "res": ("#B7DDF4", "#37526C", "#152337", "#EFF9FF"),
    "src": ("#F0BD8B", "#53392D", "#271A17", "#FFEAD6"),
    "hdr": ("#EFC77E", "#5D4420", "#2B1C12", "#FFF0CB"),
    "enc": ("#A3CBFE", "#374D6A", "#172439", "#E6F2FF"),
    "audio": ("#8BDFCC", "#2A554E", "#132D2A", "#E2FFF5"),
    "ch": ("#8BDFCC", "#2A554E", "#132D2A", "#E2FFF5"),
    "ed": ("#D0BFF3", "#423753", "#251D32", "#F4EDFF"),
}


def number(value):
    return f"{value:.6f}".rstrip("0").rstrip(".")


def outline(label, glyphs, cmap):
    shapes = []
    advance = 0
    for char in label:
        glyph = glyphs[cmap[ord(char)]]
        path = SVGPathPen(glyphs, ntos=number)
        bounds = BoundsPen(glyphs)
        glyph.draw(path)
        glyph.draw(bounds)
        if bounds.bounds:
            left, bottom, right, top = bounds.bounds
            shapes.append((advance, path.getCommands(), (left + advance, bottom, right + advance, top)))
        advance += glyph.width + 14

    left = min(box[0] for _, _, box in shapes)
    right = max(box[2] for _, _, box in shapes)
    bottom = min(box[1] for _, _, box in shapes)
    top = max(box[3] for _, _, box in shapes)
    scale = 11.4 / (top - bottom)
    horizontal = min(scale, 96 / (right - left))
    width = max(22, round((right - left) * horizontal + 7))
    x = (width - (left + right) * horizontal) / 2
    y = 8 + (bottom + top) * scale / 2
    transform = f"translate({number(x)} {number(y)}) scale({number(horizontal)} -{number(scale)})"
    paths = "\n".join(f'    <path transform="translate({dx})" d="{path}"/>' for dx, path, _ in shapes)
    return width, transform, paths


def badge_svg(label, group, glyphs, cmap):
    width, transform, paths = outline(label, glyphs, cmap)
    rim, top, bottom, ink = FINISHES.get(group, FINISHES["ed"])
    if label == "4K":
        rim, top, bottom, ink = "#FFF4CD", "#FFF1B4", "#C38C40", "#241808"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="16" viewBox="0 0 {width} 16">
  <defs>
    <linearGradient id="metal" x2="0" y2="1">
      <stop stop-color="{top}"/>
      <stop offset=".39" stop-color="{bottom}"/>
      <stop offset=".85" stop-color="{bottom}"/>
      <stop offset="1" stop-color="{top}"/>
    </linearGradient>
  </defs>
  <rect x=".5" y=".5" width="{width - 1}" height="15" rx="2.8" fill="url(#metal)" stroke="{rim}" stroke-opacity=".78"/>
  <g transform="{transform}" fill="{ink}">
{paths}
  </g>
</svg>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", type=Path, required=True)
    args = parser.parse_args()

    with TTFont(args.font) as font:
        glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
        manifest = json.loads((ROOT / "badges.json").read_text(encoding="utf-8"))
        for badge in manifest["badges"]:
            if not badge.get("image"):
                continue
            relative = urlsplit(badge["image"]).path.split("/main/", 1)[-1]
            if not relative.startswith("selos/") or not relative.endswith(".svg"):
                continue
            svg = badge_svg(badge["label"], badge.get("group"), glyphs, cmap)
            (ROOT / relative).write_text(svg, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
