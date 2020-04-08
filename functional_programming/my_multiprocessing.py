#!/usr/bin/python
# -*- coding: utf-8 -*-
# Note Avoid using `multiprocessing.py' whcih conflicts with the system module.
import collections
import multiprocessing
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
    print('Processing record {} ...'.format(x.name))
    time.sleep(1)
    currentYear = datetime.now().year
    result = { 'name': x.name, 'age': currentYear - x.born}
    print('Done processing record {} '.format(x.name))
    return result

start = time.time()

""" This is regular execution
"""
#transformation_result = tuple(map(transform, scientists))

""" multiprocessing in action
"""
pool = multiprocessing.Pool()
transformation_result=pool.map(transform, scientists)

end = time.time()
print(f'\nTime to complettion {end - start:.2f}s\n')
pprint(transformation_result)
