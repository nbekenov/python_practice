import pdb

def my_max(lst):
    max_num = -float('inf')
    for num in lst:
        #breakpoint()
        pdb.set_trace()
        if num > max_num:
            max_num = num
    return max_num

lst = [-1,-14,-7,-3,-9, -3]
print(my_max(lst))
