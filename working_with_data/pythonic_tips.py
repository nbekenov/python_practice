# use enumerate
my_list = [45, 22, 14, 65, 97, 72]


def fizz_buzz(numbers):
    for item, value in enumerate(numbers):
        if value % 3 == 0 and value % 5 == 0:
            numbers[item] = 'fizzbuzz'
        elif value % 3 == 0:
            numbers[item] = 'fizz'
        elif value % 5 == 0:
            numbers[item] = 'buzz'

fizz_buzz(my_list)
for item, value in enumerate(my_list):
    print(f' index = {item}, value = {value}')



# list Comprehensions
numbers = [4, 2, 1, 6, 9, 7]

def square(x):
    return x*x


result = [ square(num) for num in numbers]
print(result)


def is_odd(x):
    return bool(x % 2)

print([x for x in [1, 2, -5, 4] if is_odd(x)] )


# example create grid
print('>>>>>>>>>>>>>>>>')


def create_grid(num_rows, num_colums):
    grid = [ [ 0 for _ in range(num_colums) ] for _ in range(num_rows) ]
    return grid

print(f' grid = {create_grid(3,5)}')


# max function
# find the max square
lst = [1, 3, 5, -9, 4]

print(f' max_square =  {max(lst, key = lambda x : x * x)}')

# check wihc num is odd
result = [(lambda x: x % 2 == 1)(num) for num in lst]
print(f' result for odd check = {result} ')

# formating string with f
print(f"""Hi this is the first line
and this is the second one
""")


# sorting
animals = [{'type': 'cat', 'name': 'Stephanie', 'age': 8}, {'type': 'dog', 'name': 'Devon', 'age': 3}, {'type': 'rhino', 'name': 'Moe', 'age': 5}]

print(f""" return the oldest animal
{sorted(animals, key=lambda animal: animal['age'], reverse=True)[0]}
""")




import string
white_space_set = set(string.whitespace)
print(''.join(letter for letter in 'HELLO WORLD' if letter not in white_space_set))
