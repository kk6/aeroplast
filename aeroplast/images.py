# -*- coding: utf-8 -*-
"""

Transparent PNG conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from PIL import Image


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




