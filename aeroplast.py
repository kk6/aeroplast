# -*- coding: utf-8 -*-
"""

Transparent PNG conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from PIL import Image


def main(src, dest):
    img = Image.open(src)
    new_size = tuple(x + 2 for x in img.size)
    color = (255, 255, 255, 0)
    output = Image.new(img.mode, new_size, color)
    output.paste(img, (1, 1))
    output.save(dest, quality=100)


if __name__ == "__main__":
    import sys
    src, dest = sys.argv[1:]
    main(src, dest)
