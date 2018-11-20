# -*- coding: utf-8 -*-

"""{{ cookiecutter.short_description }}"""

from .constants import get_version
from .manager import Manager

__all__ = [
    'Manager',
    'get_version',
]
