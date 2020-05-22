from collections import Counter

def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    >>> majority_element_indexes([1,3,4,1,1,1])
    [0, 3, 4, 5]
    '''
    result = []
    count = Counter(lst)
    for index, value in enumerate(lst): # O(n)
        if count[value] > len(lst)//2:
            result.append(index)
    return result
