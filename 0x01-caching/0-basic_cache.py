#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    Caching system
    """
    def put(self, key, item):
        """ put = to add items """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get = to retrive items """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
