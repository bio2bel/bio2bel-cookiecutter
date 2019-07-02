# -*- coding: utf-8 -*-

"""Constants for Bio2BEL {{ cookiecutter.module_stylized }}."""

from bio2bel import get_data_dir

__all__ = [
    'MODULE_NAME',
    'DATA_DIR',
]

MODULE_NAME = '{{ cookiecutter.module_name }}'
DATA_DIR = get_data_dir(MODULE_NAME)
