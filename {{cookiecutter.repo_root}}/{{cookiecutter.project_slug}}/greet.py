# -*- coding: utf-8 -*-

from cliff.command import Command


class Greet(Command):
    "Example datakit command"

    def get_parser(self, prog_name):
        parser = super(Greet, self).get_parser(prog_name)
        parser.add_argument(
            '-g',
            '--greeting',
            help="A greeting of your choice"
        )
        return parser

    def take_action(self, parsed_args):
        print(parsed_args.greeting)
