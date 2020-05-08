# python -m doctest doctest_example.py
class A:
    def my_func(self):
        '''
        Function desc
        >>> a = A()
        >>> a.my_func()
        Hello world
        'Hello world'
        '''
        print('Hello world')
        return 'Hello world'
