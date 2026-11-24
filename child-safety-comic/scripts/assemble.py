"""Arrange approved comic panels into a wordless two-column PNG."""

import argparse
import re
from pathlib import Path

from PIL import Image, ImageOps


def assemble(folder, rows, output):
    positions = [f"r{row}-{side}" for row in range(1, rows + 1)
                 for side in ("left", "right")]
    panels = {}
    errors = []
    for path in sorted(folder.iterdir()):
        key = path.stem.lower()
        if not path.is_file() or not re.fullmatch(r"r\d+-(left|right)", key):
            continue
        if key not in positions:
            errors.append(f"Unexpected position: {path.name}")
        elif key in panels:
            errors.append(f"Duplicate {key}: {panels[key].name}, {path.name}")
        elif path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            panels[key] = path
        else:
            errors.append(f"Unsupported image: {path.name}")
    errors.extend(f"Missing: {key}" for key in positions if key not in panels)
    if errors:
        raise ValueError("\n".join(errors))
    if output.suffix.lower() != ".png" or output.resolve() in {
        path.resolve() for path in panels.values()
    }:
        raise ValueError("Choose a separate .png output file.")

    width, height, gutter = 768, 800, 12
    page = Image.new("RGB", (2 * width + gutter, rows * height + (rows - 1) * gutter), "white")
    for index, key in enumerate(positions):
        with Image.open(panels[key]) as source:
            panel = ImageOps.contain(ImageOps.exif_transpose(source).convert("RGBA"),
                                     (width, height), Image.Resampling.LANCZOS)
        row, col = divmod(index, 2)
        x = col * (width + gutter) + (width - panel.width) // 2
        y = row * (height + gutter) + (height - panel.height) // 2
        page.paste(panel, (x, y), panel)
    with output.open("xb") as stream:
        page.save(stream, format="PNG")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--rows", type=int, required=True, choices=(2, 3, 4))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        assemble(args.folder, args.rows, args.output)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")
