#!/usr/bin/env python3
"""
store an instance of the Redis client as a
private variable named _redis (using redis.Redis())
and flush the instance using flushdb.
"""

import redis
import uuid
from typing import Union
from typing import Callable, Optional, Union
from functools import wraps


class Cache:
    """
    store an instance of the Redis client as a
    private variable named _redis (using redis.Redis())
    and flush the instance using flushdb.
    """

    def __init__(self):
        """ This is the constructor method. """

        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """ This is the constructor method. """

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """ This is the constructor method. """

            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and
    outputs for a particular function.
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):  # sourcery skip: avoid-builtin-shadow
        """ Wrapper for decorator functionality """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method that takes a data argument and
        returns a string. The method should generate a
        random key (e.g. using uuid), store the input data
        in Redis using the random key and return the key.
        """

        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        conserve the original Redis.get behavior if the key does not exist.
        """

        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        conserve the original Redis.get behavior if the key does not exist.
        """

        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        conserve the original Redis.get behavior if the key does not exist.
        """

        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
