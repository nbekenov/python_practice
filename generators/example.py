def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i


if __name__=='__main__':
    mygenerator = createGenerator()
    print(f'type = {type(mygenerator)}')
    for i in mygenerator:
        print(i)

"""
from https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
Here it's a useless example, but it's handy when you know your function will return a huge set of values that you will only need to read once.

To master yield, you must understand that when you call the function, the code you have written in the function body does not run. The function only returns the generator object, this is a bit tricky :-)

Then, your code will continue from where it left off each time for uses the generator.

Now the hard part:

The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each subsequent call will run another iteration of the loop you have written in the function and return the next value. This will continue until the generator is considered empty, which happens when the function runs without hitting yield. That can be because the loop has come to an end, or because you no longer satisfy an "if/else".
"""        