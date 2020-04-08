
from functools import reduce
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


total_age = reduce( lambda acc, val : acc + val['age'], name_and_age, 0 )
print(total_age)


def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

sc_by_grouped_by_filed = reduce(
    reducer,
    scientists,
    {'math':[], 'physics': [], 'chemistry': []}
)
pprint(sc_by_grouped_by_filed)

print('##########################')
sc_by_grouped_by_filed = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)
""" Usually, a Python dictionary throws a KeyError
    if you try to get an item with a key that is not currently in the dictionary.
    The defaultdict in contrast will simply create any items that you try to access
    (provided of course they do not exist yet).
"""
pprint(sc_by_grouped_by_filed)
