# -*- coding: utf-8 -*-


def test_get_new_size():
    from aeroplast import get_new_size
    original_size = (100, 200)
    new_size = get_new_size(original_size)
    assert new_size == (102, 202)
