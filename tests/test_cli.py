# -*- coding: utf-8 -*-
from PIL import Image


def test_cli(cli, src_image, resized_image, output_image_filename):
    cli.resize(src_image.filename, output_image_filename, length=100)
    result = Image.open(output_image_filename)
    assert resized_image.tobytes() == result.tobytes()
