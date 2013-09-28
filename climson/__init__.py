#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import absolute_import

import sys
import argparse
import inspect

from climson import climson

__version__ = '0.1.3'
__author__ = 'takumakanari (chemtrails.t@gmail.com)'
__license__ = 'MIT License'
__description__ = 'Commandline tool for easy and simplify to implement applications that is using multi-command CLI.'


class ClimsonClient(object):

    def __init__(self, **kwargs):
        self._root_parser = argparse.ArgumentParser(**kwargs)
        self._subparsers = self._root_parser.add_subparsers(
            dest='__subcommand__'
        )

    def execute(self, args=None):
        a = self._root_parser.parse_args(args)
        return a.__exec_func__(a)

    def add(self, command_cls):
        return climson.add(self._subparsers, command_cls)


# {ClimsonClient} instance for @commandfy
commandfy_client = ClimsonClient()


def commandfy(name=None, description=None):
    def _wrap(func):
        class C(climson.BaseCommand):
            pass

        def func_wrap_for_exec(self, **kwargs):
            func(**kwargs)

        C.name = name or func.__name__
        C.description = description or ''
        C.do_command = func_wrap_for_exec

        argvalues = inspect.getargspec(func)
        if argvalues.args:
            for a in argvalues.args:
                C.options = C.options + (
                    climson.make_option('--{}'.format(a), dest=a),
                )
        commandfy_client.add(C)

    return _wrap

