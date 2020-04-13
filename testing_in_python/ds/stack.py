#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stack:

    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)
