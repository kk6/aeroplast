# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import fire
from PIL import Image
from logzero import logger

import aeroplast.images as images
import aeroplast.paths as paths

MAX_PNG_LENGTH = 900


class CLI(object):
    """Transparent PNG conversion"""

    def _get_paths(self, src, dest, prefix, overwrite):
        path = Path(src)
        absolute_path = paths.get_absolute_path(path)
        name = paths.get_destination_filename(path, prefix, overwrite)
        dest = paths.get_destination_path(dest, absolute_path, name)
        return absolute_path, dest

    def _open_image(self, absolute_path):
        logger.info(f"Open the image: {absolute_path}")
        try:
            return Image.open(absolute_path)
        except FileNotFoundError:
            logger.error(f"Image not found: {absolute_path}")

    def _resize_image(self, original_image, size):
        logger.info(f"Resize the image to fit within {size[0]}*{size[1]} px.")
        original_image = images.resize_image(original_image, size)
        logger.info("Resize complete.")
        return original_image

    def resize(
        self, src, dest=None, prefix="t", overwrite=False, length=MAX_PNG_LENGTH
    ):
        """
        Resize image.

        :param src: Input src image filename.
        :param dest: Output destination filename.
        :param prefix: Prefix added to output image file name.
        :param overwrite: Whether to overwrite the image or not.
        :param length: default 900 px
        :return: None

        """
        absolute_path, dest = self._get_paths(src, dest, prefix, overwrite)
        size = (length, length)

        original_image = self._open_image(absolute_path)
        if original_image is None:
            sys.exit(1)

        image = self._resize_image(original_image, size)

        image.save(dest)
        logger.info(f"Image generation succeeded: {dest}")


def main():
    return fire.Fire(CLI)
