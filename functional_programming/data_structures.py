# Small info: If you want to have a multithreaded program and do parallel processing,
# then using immutable data structures would allow you
# to not have to worry about locking the data structures
# because there would be no way to update them.

import collections
from pprint import pprint

""" 1. Juf FYI  lists and dictionaries are mutable data structures
"""
list_of_dictionaries = [ { 'name': 'Jim', 'born': 1986 },
                         { 'name': 'Charlie', 'born': 1996 }
                       ]


""" 2. collections module helps with representing
    immutable data sctrutures such as tuples
"""

my_immutable_structure = collections.namedtuple('my_immutable_structure',['name', 'born'])
firt_record = my_immutable_structure(name = 'Jim', born = 1986)
second_record = my_immutable_structure(name = 'Charlie', born = 1996)

""" 3. mix immutable and mutable
"""
immutable_structure = collections.namedtuple('immutable_structure',['name', 'born'])
my_list = [ immutable_structure(name = 'Charlie', born = 1996),
            immutable_structure(name = 'Jim', born = 1986)
]
# we can delete and insert new values, however this is not best practice, but just to know is ok
del my_list[0]

""" 4. Tuple is immutable
"""
my_tuple = ( immutable_structure(name = 'Charlie', born = 1996),
             immutable_structure(name = 'Jim', born = 1986)
)

def just_print(input_data):
    """ Just preaty print whatever the input
    """
    pprint(input_data)


def main():
    just_print(my_tuple)

if __name__ == '__main__':
    main()
