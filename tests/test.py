#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import nose
from nose.tools import (
    ok_, 
    eq_,
    raises
)
from climson import ClimsonClient
from climson.climson import (
    BaseCommand,
    ClimsonException,
    ValidateError,
    make_option
)


class TestCommand(BaseCommand):

    name = 'test'

    description = 'description'

    options = BaseCommand.options + (
        make_option('--message', dest='message'),
        make_option('--age', dest='age', type=int),
    )

    def do_command(self, message=None, age=0):
        return (message, age)

    def validate(self, message=None, age=0):
        if age < 10:
            return False
        return True

class TestClimsonClient(object):

    def __init__(self):
        self.client = ClimsonClient(prog=str(self), description='test')

    def test_add(self):
        ret = self.client.add(TestCommand)
        ok_(ret is not None)

    @raises(ClimsonException)
    def test_add_invalid_type(self):
        self.client.add(str)

    def test_execute(self):
        self.client.add(TestCommand)
        ret = self.client.execute(args=['test', '--message', 'ok', '--age', '10'])
        ok_(ret is not None)
        eq_(ret[0], 'ok')
        eq_(ret[1], 10)

    @raises(ValidateError)
    def test_validate(self):
        self.client.add(TestCommand)
        ret = self.client.execute(args=['test', '--message', 'ok', '--age', '9'])

