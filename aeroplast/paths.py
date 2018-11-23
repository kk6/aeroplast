# -*- coding: utf-8 -*-


def get_absolute_path(path):
    """
    Get the absolute path.

    :param pathlib.Path path: Path object
    :return: Absolute path
    :rtype: pathlib.Path

    """
    return path.expanduser().resolve()


def get_destination_filename(path, prefix="t", overwrite=False):
    """
    Get the output file name.

    :param pathlib.Path path: Destination path
    :param str prefix: prefix of filename.
    :param bool overwrite: if True then
    :return: file name for output
    :rtype: str

    """
    if overwrite:
        name = path.name
    else:
        name = "-".join([prefix, path.name])
    return name


def get_destination_path(dest, absolute_path, name):
    """
    Get the output file path

    :param pathlib.Path dest: File path for output.
    :param pathlib.Path absolute_path: Source file's absolute path.
    :param str name: Output file name.
    :return: Destination file path
    :rtype: pathlib.Path

    """
    if dest is None:
        dest = absolute_path.parent / name
    return dest
