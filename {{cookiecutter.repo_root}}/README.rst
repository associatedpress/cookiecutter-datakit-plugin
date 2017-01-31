{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
===============================
{{ cookiecutter.project_name }}
===============================

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_root }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_root }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_root }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_root }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_root | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.repo_root | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_root }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_root }}/
     :alt: Updates


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.repo_root | replace("_", "-") }}.readthedocs.io.
{% endif %}


Features
========

* TODO

Installation
============

In order to use this plugin with a system-wide install of datakit_::

  $ sudo pip install {{ cookiecutter.repo_root }}

Usage
=====

* TODO


Credits
========

This package was created with Cookiecutter_ and the `associatedpress/cookiecutter-datakit-plugin`_ 
project template (a modified version of the most excellent `audreyr/cookiecutter-pypackage`_).

.. _datakit: https://github.com/associatedpress/datakit-core
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`associatedpress/cookiecutter-datakit-plugin`: https://github.com/associatedpress/cookiecutter-datakit-plugin
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
