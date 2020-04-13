#!/usr/bin/python
# -*- coding: utf-8 -*-

from ds.stack import Stack

def test_constructor():
    s = Stack()
    assert  isinstance(s, Stack)
    assert len(s) == 0
