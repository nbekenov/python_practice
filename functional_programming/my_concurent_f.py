#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections
import time
import os
import concurrent.futures
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

def transform(x):
    print(f'Process {os.getpid()} working on record {x.name} ...')
    time.sleep(1)
    currentYear = datetime.now().year
    result = { 'name': x.name, 'age': currentYear - x.born}
    print(f'Process {os.getpid()} done processing record {x.name} ')
    return result


""" With multythreading you can get into Global Interpreter Lock (GIL).
    Because of the GIL, no two threads can execute Python code at the same time.
    So even if you have multiple threads running in your Python program,
    only one of them can execute at a time.
    The best way to get around this is to use process-based parallel programing,
    or process-based parallelism.
"""
def concurent_func():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # if you want multiprocessing then concurrent.futures.ProcessPoolExecutor()
        result = executor.map(transform, scientists)
    return tuple(result)

def main():
    start = time.time()
    transformation_result=concurent_func()
    end = time.time()
    print(f'\nTime to complettion {end - start:.2f}s\n')
    pprint(transformation_result)

if __name__ == '__main__':
    main()
