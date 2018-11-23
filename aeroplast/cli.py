# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image
from logzero import logger

import aeroplast.images as images
import aeroplast.paths as paths


class CLI(object):
    """Transparent PNG conversion"""

    def convert(self, src, dest=None, prefix="t", overwrite=False, resize=False):
        """
        Output image with transparent PNG

        :param src: Input src image filename.
        :param dest: Output destination filename.
        :param prefix: Prefix added to output image file name.
        :param overwrite: Whether to overwrite the image or not.
        :param resize: Resize the image. When only option is specified, resize to the default 1000 * 1000px.
                       If you pass a number (pixel) as an optional argument, resize it to fit that size.
        :return: None

        """
        path = Path(src)
        absolute_path = paths.get_absolute_path(path)
        name = paths.get_destination_filename(path, prefix, overwrite)
        dest = paths.get_destination_path(dest, absolute_path, name)

        logger.info(f"Open the image: {absolute_path}")
        try:
            original_image = Image.open(absolute_path)
        except FileNotFoundError:
            logger.error(f"Image not found: {absolute_path}")
        else:
            if resize:
                if resize is True:
                    size = (1000, 1000)
                else:
                    size = (resize, resize)

                logger.info(f"Resize the image to fit within {size[0]}*{size[1]} px.")
                original_image = images.resize_image(original_image, size)
                logger.info("Resize complete.")

            logger.info("Image converting...")
            image = images.add_transparent_frame(original_image)
            image.save(dest)
            logger.info(f"Image generation succeeded: {dest}")

    def resize(self, src, dest=None, prefix="t", overwrite=False, length=1000):
        """
        Resize image.

        :param src: Input src image filename.
        :param dest: Output destination filename.
        :param prefix: Prefix added to output image file name.
        :param overwrite: Whether to overwrite the image or not.
        :param length: default 1000 px
        :return: None

        """
        path = Path(src)
        absolute_path = paths.get_absolute_path(path)
        name = paths.get_destination_filename(path, prefix, overwrite)
        dest = paths.get_destination_path(dest, absolute_path, name)
        size = (length, length)

        logger.info(f"Open the image: {absolute_path}")
        try:
            original_image = Image.open(absolute_path)
        except FileNotFoundError:
            logger.error(f"Image not found: {absolute_path}")
        else:
            logger.info(f"Resize the image to fit within {size[0]}*{size[1]} px.")
            image = images.resize_image(original_image, size)
            logger.info("Resize complete.")
            image.save(dest)
            logger.info(f"Image generation succeeded: {dest}")
