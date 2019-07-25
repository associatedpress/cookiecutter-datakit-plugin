{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_root }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_root }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_root }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_root }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_root }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_root }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_root | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.repo_root | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}


Overview
========

{{ cookiecutter.project_short_description }}

* Documentation: http://{{ cookiecutter.repo_root }}.readthedocs.io/en/latest/
* Github: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_root }}
* PyPI: https://pypi.python.org/pypi/{{ cookiecutter.repo_root }}
* Free and open source software: `{{ cookiecutter.open_source_license }}`_

.. _{{ cookiecutter.open_source_license }}: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_root }}/blob/master/LICENSE

Features
========

* TODO

Quickstart
==========

To use this datakit_ plugin::

  $ pip install {{ cookiecutter.repo_root }}

Check out the available commands::

  $ datakit --help

.. note:: See the `{{ cookiecutter.repo_root | replace("_", "-") }} docs`_ for more detailed usage info.


.. _datakit: https://github.com/associatedpress/datakit-core
.. _{{ cookiecutter.repo_root | replace("_", "-") }} docs: https://{{ cookiecutter.repo_root | replace("_", "-") }}.readthedocs.io/en/latest/
