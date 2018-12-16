# -*- coding: utf-8 -*-
"""
The main entry point. Invoke as `python -m aeroplast'.
"""
import sys

if __name__ == "__main__":
    from .cli import main

    sys.exit(main())
