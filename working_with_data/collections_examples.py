from collections import Counter
from collections import defaultdict

def top_three_letters(str):
    print(Counter(str).most_common(3))

def top_three_letters_brute(str):
    counter = defaultdict(int)
    for c in str:
        counter[c] +=1
    top_tree = sorted(counter, key = lambda k: counter[k], reverse=True)[:3]

    return [ (letter, counter[letter] ) for letter in top_tree ]

top_three_letters("asdrdbbaaa")
print('#########')
print(top_three_letters_brute("asdrdbbaaa"))



from collections import deque

deq = deque([1, 2, 3])
deq.appendleft(5)
deq.append(6)
deq.popleft()
print(f'deq = {deq}')



import collections
from pprint import pprint
Student = collections.namedtuple('Student', [
    'first_name',
    'last_name',
    'birth_date'
])


my_immutable =( Student(first_name = 'Jim',last_name = 'Oms', birth_date = '05/20/1987' ),
                Student(first_name = 'Tom',last_name = 'Hanse', birth_date = '05/20/1987')
)

pprint(my_immutable)
