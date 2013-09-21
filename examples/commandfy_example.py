#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from climson import (
    commandfy,
    commandfy_client
)


@commandfy(description='Say hello.')
def hello(name=None):
    print 'Hello, {}'.format(name)


@commandfy(description='Say goodbye.')
def goodbye(name=None):
    print 'Hello, {}'.format(name)


if __name__ == '__main__':
    commandfy_client.execute()

