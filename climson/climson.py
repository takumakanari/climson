#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import absolute_import
import argparse
import inspect

__all__ = [
    'ClimsonException',
    'ValidateError',
    'BaseCommand',
    'add',
    'make_option'
]


class ClimsonException(Exception):
    pass


class ValidateError(ClimsonException):

    def __init__(self, args, msg=None):
        self._args = args
        self._msg = msg

    def __str__(self):
        return 'ValidateError {} with args {}'.format(
            self._msg or '',
            self._args
        )


class BaseCommand(object):

    name = None

    description = ''

    options = ()

    def __init__(self, optargs):
        self._optargs = optargs

    @property
    def optargs(self):
        return self._optargs

    @classmethod
    def cleanup_args(cls, args_dict):
        for exclude_arg in ('__exec_func__', '__subcommand__'):
            if exclude_arg in args_dict:
                args_dict.pop(exclude_arg)
        return args_dict

    def execute(self):
        optargs = self.optargs
        args_dict = optargs.__dict__
        self.cleanup_args(args_dict)
        if not self.validate(**args_dict):
            raise ValidateError(args_dict)
        return self.do_command(**args_dict)

    def validate(self, **kwargs):
        """
         Do custom validation with args and
         raise ValidateError or return False when validate failed.
        """
        return True

    def do_command(self, **kwargs):
        raise NotImplementedError('do_command in {}'.format(self))

    def __str__(self):
        return '<{}: ({})>'.format(self.name, self.description)


def add(parser, command_cls):
    if not issubclass(command_cls, BaseCommand):
        raise ClimsonException('InvalidValue: command cls '
        'must be extends BaseCommand, but {}'.format(
            command_cls
        ))

    if not command_cls.name:
        raise ClimsonException('InvalidValue: Specify command_cls.name')

    cmd = parser.add_parser(command_cls.name, help=command_cls.description)

    def inner_exec_func(args):
        handler = command_cls(args)
        return handler.execute()

    cmd.set_defaults(__exec_func__=inner_exec_func)

    for opt in command_cls.options:
        cmd.add_argument(*opt['args'], **opt['kwargs'])

    return parser


def make_option(*args, **kwargs):
    return dict(args=args, kwargs=kwargs)

