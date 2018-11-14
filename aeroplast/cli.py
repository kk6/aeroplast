# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image
from logzero import logger

from .images import add_transparent_frame


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
