# -*- coding: utf-8 -*-
import os.path
import pytest
from PIL import Image


@pytest.fixture(scope="function")
def src_image():
    return Image.open("tests/images/src.png")


@pytest.fixture(scope="function")
def output_image_filename():
    filename = "tests/images/output.png"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture(scope="function")
def resized_image():
    return Image.open("tests/images/resized.png")


@pytest.fixture(scope="function")
def cli():
    from aeroplast.cli import CLI

    return CLI()
