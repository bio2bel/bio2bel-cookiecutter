# -*- coding: utf-8 -*-

"""Test cases for Bio2BEL {{ cookiecutter.module_stylized }}."""

import os

from bio2bel.testing import AbstractTemporaryCacheClassMixin
from bio2bel_{{ cookiecutter.module_name }} import Manager

__all__ = [
    'TemporaryCacheClass',
]


class TemporaryCacheClass(AbstractTemporaryCacheClassMixin):
    """A test case containing a temporary database and a Bio2BEL {{ cookiecutter.module_stylized }} manager."""

    Manager = Manager
    manager: Manager

    @classmethod
    def populate(cls):
        """Populate the Bio2BEL {{ cookiecutter.module_stylized }} database with test data."""
        # cls.manager.populate(url=...)
        raise NotImplementedError
