#!/usr/bin/env python3
""" Python script """
import requests
import redis
from typing import Callable
from functools import wraps


red = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator"""
    @wraps(method)
    def wrapper(url):
        """ wrapper method"""
        red.incr(f"count:{url}")
        cached_html = red.get(f"cached:{url}")

        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        red.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ uses the requests module to obtain the HTML content
    of a particular URL and returns it """
    req = requests.get(url)
    return req.text
