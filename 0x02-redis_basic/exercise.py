#!/usr/bin/env python3
"""python redis script"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decoratore method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ static method """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper methods"""
        key = method.__qualname__
        inputs_key = key + ":inputs"
        outputs_key = key + ":outputs"
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """display the  call history of a particular function"""
    cache = redis.Redis()

    name = method.__qualname__
    num_calls = cache.get(name).decode('utf-8')
    inputs_key = name + ":inputs"
    outputs_key = name ":outputs"

    inputs = cache._redis.lrange(inputs_key, 0, -1)
    outputs = cache._redis.lrange(outputs_key, 0, -1)
    print("{} was called {)} times:".format(name, num_calls))
    for inp, out in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, inp.decode('utf-8'),
              out.decode('utf-8')))


class Cache:
    """ class definition"""
    def __init__(self):
        """Initialization method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a string of random number"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[int, bytes, str, float]:
        """Checks if key exists"""

        res = self._redis.get(key)
        if fn is not None:
            return fn(res)
        return res

    def get_str(self, key: str) -> str:
        """Parametize get as string"""
        res = self.get(key)
        return res.decode('utf-8')

    def get_int(self, key: str) -> int:
        """ Parametize get to int"""
        res = self.get(key)

        try:
            return int(res.decode('utf-8'))
        except Exception:
            return 0
        return res
