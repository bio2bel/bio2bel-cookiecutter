Bio2BEL {{ cookiecutter.module_stylized }} |build|
==================================================
{{ cookiecutter.short_description }}

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_{{ cookiecutter.module_name }}`` can be installed easily from
`PyPI <https://pypi.python.org/pypi/bio2bel_{{ cookiecutter.module_name }}>`_
with the following code in your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install bio2bel_{{ cookiecutter.module_name }}

or from the latest code on `GitHub <https://github.com/bio2bel/{{ cookiecutter.module_name }}>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/{{ cookiecutter.module_name }}.git

Setup
-----
{{ cookiecutter.module_stylized }} can be downloaded and populated from either the
Python REPL or the automatically installed command line utility.

Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_{{ cookiecutter.module_name }}
    >>> {{ cookiecutter.module_name }}_manager = bio2bel_{{ cookiecutter.module_name }}.Manager()
    >>> {{ cookiecutter.module_name }}_manager.populate()

Command Line Utility
~~~~~~~~~~~~~~~~~~~~
.. code-block:: sh

    bio2bel_{{ cookiecutter.module_name }} populate


.. |build| image:: https://travis-ci.com/bio2bel/{{ cookiecutter.module_name }}.svg?branch=master
    :target: https://travis-ci.org/bio2bel/{{ cookiecutter.module_name }}
    :alt: Build Status

.. |documentation| image:: http://readthedocs.org/projects/bio2bel-{{ cookiecutter.module_name }}/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/{{ cookiecutter.module_name }}/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_{{ cookiecutter.module_name }}.svg
    :alt: Current version on PyPI

.. |coverage| image:: https://codecov.io/gh/bio2bel/{{ cookiecutter.module_name }}/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/{{ cookiecutter.module_name }}?branch=master
    :alt: Coverage Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_{{ cookiecutter.module_name }}.svg
    :alt: Stable Supported Python Versions

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_{{ cookiecutter.module_name }}.svg
    :alt: MIT License
