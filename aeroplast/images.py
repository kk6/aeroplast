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


def add_transparent_frame(original_image):
    """
    Add a transparent frame.

    Generate a transparent image that is 2px larger than the original image,
    and paste the original image on it.

    :param original_image: Original image
    :return: Image with transparent frame added.
    :rtype: :py:class: `~PIL.Image.Image`

    """
    new_size = get_new_size(original_image.size)
    color = (255, 255, 255, 0)
    image = Image.new("RGBA", new_size, color)
    image.paste(original_image, (1, 1))
    return image
