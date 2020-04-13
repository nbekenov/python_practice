#!/usr/bin/python
# -*- coding: utf-8 -*-
from ds.stack import Stack
import pytest


@pytest.fixtures
def stack():
    """ PyTest fixtures
        a great way to provide a fixed baseline
        upon which tests can reliably and repeatedly executed.
    """
    return Stack()

def test_constructor():
    """
        Test Stack class constructor
    """
    s = Stack()
    assert  isinstance(s, Stack)
    assert len(s) == 0

def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
