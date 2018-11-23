# -*- coding: utf-8 -*-
"""
The main entry point. Invoke as `python -m aeroplast'.
"""
import fire

from .cli import CLI


if __name__ == "__main__":
    fire.Fire(CLI)
