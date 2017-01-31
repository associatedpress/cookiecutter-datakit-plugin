======================
Datakit Plugin Package
======================

.. image:: https://pyup.io/repos/github/associatedpress/cookiecutter-datakit-plugin/shield.svg
     :target: https://pyup.io/repos/github/associatedpress/cookiecutter-datakit-plugin/
     :alt: Updates

Cookiecutter_ template for generating a Datakit plugin. This is a modified
version of the most excellent https://github.com/audreyr/cookiecutter-pypackage

* GitHub repo: https://github.com/associatedpress/cookiecutter-datakit-plugin/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.3, 3.4, 3.5
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Build Status
-------------

Linux:

.. image:: https://img.shields.io/travis/zstumgoren/cookiecutter-datakit-plugin.svg
    :target: https://travis-ci.org/zstugmoren/cookiecutter-datakit-plugin
    :alt: Linux build status on Travis CI


Quickstart
----------

Install the latest Cookiecutter_ if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Datakit plugin project::

    cookiecutter https://github.com/associatedpress/cookiecutter-datakit-plugin.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.python.org/pypi
