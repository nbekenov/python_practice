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