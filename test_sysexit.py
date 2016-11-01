#!/usr/bin/env python3
'''
Test for sys exit.

'''

import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

if __name__=='__main__':
    test_mytest()