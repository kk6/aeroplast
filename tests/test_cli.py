# -*- coding: utf-8 -*-
from PIL import Image


def test_cli(cli, src_image, expected_image, output_image_filename):
    cli.convert(src_image.filename, output_image_filename)
    result = Image.open(output_image_filename)
    assert expected_image.tobytes() == result.tobytes()
