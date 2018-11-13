# -*- coding: utf-8 -*-
"""

Transparent PNG conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import fire
from PIL import Image


def add_transparent_frame(src):
    original_image = Image.open(src)
    new_size = tuple(x + 2 for x in original_image.size)
    color = (255, 255, 255, 0)
    image = Image.new(original_image.mode, new_size, color)
    image.paste(original_image, (1, 1))
    return image


class CLI(object):
    """Transparent PNG conversion"""

    def convert(self, src, dest):
        """
        Output image with transparent PNG

        :param src: Input src image filename.
        :param dest: Output destination filename.
        :return: None

        """
        image = add_transparent_frame(src)
        image.save(dest, quality=100)


if __name__ == "__main__":
    fire.Fire(CLI)
