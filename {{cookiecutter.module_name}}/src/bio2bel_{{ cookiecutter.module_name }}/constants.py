# -*- coding: utf-8 -*-

"""Constants for Bio2BEL {{ cookiecutter.module_stylized }}."""

from bio2bel import get_data_dir

__all__ = [
    'VERSION',
    'MODULE_NAME',
    'DATA_DIR',
    'get_version',
]

VERSION = '0.0.1-dev'
MODULE_NAME = '{{ cookiecutter.module_name }}'
DATA_DIR = get_data_dir(MODULE_NAME)


def get_version() -> str:
    """Get the software version."""
    return VERSION
