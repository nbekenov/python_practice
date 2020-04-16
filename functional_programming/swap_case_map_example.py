#!/usr/bin/python
# -*- coding: utf-8 -*-
# task from the https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result=''.join(map(lambda x: x.lower() if x.isupper() == True else x.upper() ,s))
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
