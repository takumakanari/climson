#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from climson import (
    ClimsonClient,
    climson
)
from climson.climson import make_option


class Hello(climson.BaseCommand):

    name = 'hello'

    description = 'Say hello.'

    options = climson.BaseCommand.options + (
        make_option('-n', '--name', help='Your name', required=True, dest='name'),
        make_option('-a', '--age', help='Your age', required=False, type=int, dest='age'),
    )

    def do_command(self, name=None, age=0):
        print 'Hello, {} age={} in kwargs'.format(name, age)
        # or use self.optargs
        print 'Hello, {} age={} in self.optargs'.format(self.optargs.name, self.optargs.age)


class GoodBye(climson.BaseCommand):

    name = 'goodbye'

    description = 'Say goodbye.'

    options = climson.BaseCommand.options + (
        make_option('-n', help='Your name', required=True, dest='name'),
    )

    def validate(self, name=None):
        if len(name) < 5:
            raise climson.ValidateError('name length must be ov 5!')
        return True

    def do_command(self, name=None):
        print 'GoodBye, {}'.format(name)


client = ClimsonClient(prog='test prog', description='This is test program.')
client.add(Hello)
client.add(GoodBye)

if __name__ == '__main__':
    client.execute()

