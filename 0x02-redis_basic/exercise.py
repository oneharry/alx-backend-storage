#!/usr/bin/env python3
"""python redis script"""
import redis
import uuid
from typing import Union


class Cache:
    """ class definition"""
    def __init__(self):
        """Initialization method"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, float, bytes, int]) -> str:
        """returns a string of random number"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    
