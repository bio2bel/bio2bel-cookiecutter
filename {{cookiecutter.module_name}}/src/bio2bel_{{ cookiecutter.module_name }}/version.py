# -*- coding: utf-8 -*-

"""Version information."""

__all__ = [
    'VERSION',
    'get_version',
]

VERSION = '0.0.1-dev'


def get_version():
    """Get the software version of Bio2BEL {{ cookiecutter.module_stylized }}."""
    return VERSION
