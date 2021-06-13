"""

Разработка функции-декоратора, позволяющей выполнить декорируемую функцию единожды.

"""

import sqlite3
import functools
import json

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.called = True
        return func(*args, **kwargs) 
    inner.called = False 
    return inner

@once
def f():
    return 0

f()
