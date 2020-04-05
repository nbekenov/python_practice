# ABout filter func
# filter() takes another function object, and you can define a function object inline with lambda expressions.

import collections
from pprint import pprint

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
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

pprint( tuple(filter( lambda x : x.field == 'physics' and x.nobel is True , scientists )) )
""" Declaritive and only functions
    Can replace for in loop
"""
print('########################## Filter with defined function')

def nobel_filter(input):
    """ Return only records with nobel prize
    """
    return input.nobel is True

pprint( tuple( filter(nobel_filter, scientists) ))


# List Comprehensions
print('########################## List Comprehensions')
pprint ( tuple([ item for item in scientists if item.nobel is True ]) )

# get rid of List Comprehensions
print('########################## generator expression')
pprint ( tuple( item for item in scientists if item.nobel is True) )
""" Here we are not creating a list obj as intermidiate
    A generator expressions defines an ad hoc iterator
    that then produces values for you without first creating a list,
    and then creating a tuple from that list, and then destroying the list again,
    so it’s more memory efficient.
"""
