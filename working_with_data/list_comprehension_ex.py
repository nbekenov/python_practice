"""
values = [expression for value in collection if condition]
values = []
for value in collection:
    if condition:
        values.append(expression)
"""
sq = [ x * x for x in range(10)]
print(sq)

even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)
