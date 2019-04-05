# -*- coding: utf-8 -*-
"""

Transparent PNG conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from PIL import Image


def get_new_size(original_size):
    """
    Returns each width and height plus 2px.

    :param original_size: Original image's size
    :return: Width / height after calculation
    :rtype: tuple

    """
    return tuple(x + 2 for x in original_size)


def resize_image(image, size):
    """
    Resize the image to fit in the specified size.

    :param image: Original image.
    :param size: Tuple of (width, height).
    :return: Resized image.
    :rtype: :py:class: `~PIL.Image.Image`

    """
    image.thumbnail(size)
    return image
