#!/usr/bin/python
# -*- coding: utf-8 -*-
# Note Avoid using `multiprocessing.py' whcih conflicts with the system module.
import collections
import multiprocessing
import os
from functools import reduce
from pprint import pprint
from datetime import datetime

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='math', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='physics', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='chemistry', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1991, nobel=False),
)

import time
def transform(x):
    print(f'Process {os.getpid()} working on record {x.name} ...')
    time.sleep(1)
    currentYear = datetime.now().year
    result = { 'name': x.name, 'age': currentYear - x.born}
    print(f'Process {os.getpid()} done processing record {x.name} ')
    return result



""" This is regular execution
"""
#transformation_result = tuple(map(transform, scientists))

""" multiprocessing in action
    multiprocessing in the standard library was designed to run your code across multiple CPUs.
    At a high level, it does this by creating a new instance of the Python interpreter
    to run on each CPU and then farming out part of your program to run on it.

    bringing up a separate Python interpreter is not as fast as starting
    a new thread in the current Python interpreter.    
"""
def get_results():
    with multiprocessing.Pool(processes=len(scientists)) as pool:
        return pool.map(transform, scientists)

def main():
    start = time.time()
    transformation_result=get_results()
    end = time.time()
    print(f'\nTime to complettion {end - start:.2f}s\n')
    pprint(transformation_result)

if __name__ == '__main__':
    main()
