# map : (func, *iterable)

import collections
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

currentYear = datetime.now().year
name_and_age = tuple ( map(lambda x : { 'name': x.name, 'age': currentYear - x.born}, scientists))
pprint(name_and_age)
""" Create a new iterable containnong info about name and age
    without modifying an old iterable
"""


# List Comprehensions
print('########################## List Comprehensions')
pprint( [{ 'name': x.name, 'age': currentYear - x.born} for x in scientists ] )


# get rid of List Comprehensions
print('########################## generator expression')
pprint( tuple( { 'name': x.name, 'age': currentYear - x.born} for x in scientists ) )
