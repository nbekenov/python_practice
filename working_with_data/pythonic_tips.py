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
