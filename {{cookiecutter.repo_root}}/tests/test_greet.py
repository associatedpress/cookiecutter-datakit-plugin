#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import mock 


from {{ cookiecutter.project_slug }}.greet import Greet


def test_greet(capsys):
    """Sample pytest test function with a built-in pytest fixture as an argument.
    """
    # cmd = Greeting(None, None, cmd_name='{{cookiecutter.project_slug':greet')
    # parsed_args = mock.Mock()
    # parsed_args.greeting = 'Hello world!'
    # cmd.run(parsed_args)
    # out, err = capsys.readouterr()
    # assert 'Hello world!' in out
