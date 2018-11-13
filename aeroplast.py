# -*- coding: utf-8 -*-
"""

Transparent PNG conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from pathlib import Path

import fire
from PIL import Image
from logzero import logger


def get_new_size(original_size):
    """
    Returns each width and height plus 2px.

    :param original_size:
    :return: Width / height after calculation
    :rtype: tuple

    """
    return tuple(x + 2 for x in original_size)


def add_transparent_frame(original_image):
    new_size = get_new_size(original_image.size)
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
        path = Path(src)
        absolute_path = path.resolve()

        logger.info(f"Open the image: {absolute_path}")
        try:
            original_image = Image.open(absolute_path)
        except FileNotFoundError:
            logger.error(f"Image not found: {absolute_path}")
        else:
            logger.info("Image converting...")
            image = add_transparent_frame(original_image)
            image.save(dest, quality=100)
            logger.info(f"Image generation succeeded: {dest}")


if __name__ == "__main__":
    fire.Fire(CLI)
