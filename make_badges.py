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
    "res": ("#53657A", "#232E3A", "#EEF5FF"),
    "src": ("#765B35", "#332819", "#FFE3AE"),
    "hdr": ("#745A35", "#372A19", "#FFE2A5"),
    "enc": ("#4C607C", "#253043", "#DDEBFF"),
    "audio": ("#3E615C", "#203531", "#DBF6F0"),
    "ch": ("#3E615C", "#203531", "#DBF6F0"),
    "ed": ("#62566D", "#2B2534", "#EDE5F4"),
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
    scale = 9.8 / (top - bottom)
    horizontal = min(scale, 81 / (right - left))
    width = max(21, round((right - left) * horizontal + 8))
    x = (width - (left + right) * horizontal) / 2
    y = 8 + (bottom + top) * scale / 2
    transform = f"translate({number(x)} {number(y)}) scale({number(horizontal)} -{number(scale)})"
    paths = "\n".join(f'    <path transform="translate({dx})" d="{path}"/>' for dx, path, _ in shapes)
    return width, transform, paths


def badge_svg(label, group, glyphs, cmap):
    width, transform, paths = outline(label, glyphs, cmap)
    rim, background, ink = FINISHES.get(group, FINISHES["ed"])
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="16" viewBox="0 0 {width} 16">
  <rect x=".5" y="1" width="{width - 1}" height="14" rx="3.25" fill="{background}" stroke="{rim}"/>
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
