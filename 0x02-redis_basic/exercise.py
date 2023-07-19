#!/usr/bin/env python3
"""python redis script"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache:
    """ class definition"""
    def __init__(self):
        """Initialization method"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """ Decoratore method"""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """Wrapper method"""
            key = f"{method.__qualname__}_calls"
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper


    @count_calls
    def store(self, data: Union[str, float, bytes, int]) -> str:
        """returns a string of random number"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key


    def get(self, key: str, fn: Callable = None) -> Union[bytes, str, None]:
        """Checks if key exists"""
        if not self._redis.exists(key):
            return None

        res = self._redis.get(key)
        if fn is not None:
            return fn(res)

        return res

    def get_str(self, key: str) -> Union[str, None]:
        """Parametize get as string"""
        return self.get(key, fn=lambda a: a.decode())

    def get_int(self, key: str) -> Union[int, None]:
        """ Parametize get to int"""
       return self.get(key, fn=int) 
