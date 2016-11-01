#!/usr/bin/env python3
'''
Simple test for a function.

'''


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

if __name__=='__main__':
    test_answer()