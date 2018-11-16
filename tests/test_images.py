# -*- coding: utf-8 -*-


def test_get_new_size():
    from aeroplast.images import get_new_size
    original_size = (100, 200)
    new_size = get_new_size(original_size)
    assert new_size == (102, 202)


def test_add_transparent_frame(src_image, expected_image):
    from aeroplast.images import add_transparent_frame
    result = add_transparent_frame(src_image)
    assert expected_image.tobytes() == result.tobytes()


def test_resize_image(src_image, resized_image):
    from aeroplast.images import resize_image
    result = resize_image(src_image, (100, 100))
    assert resized_image.tobytes() == result.tobytes()
