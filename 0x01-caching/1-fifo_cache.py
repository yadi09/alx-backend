#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from BaseCaching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache"""
    def __init__(self):
        """initial function"""
        super().__init__()

    def put(self, key, item):
        """put = add item"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                key = next(iter(self.cache_data))
                print("DISCARD: {}".format(key))
                del self.cache_data[key]

    def get(self, key):
        """get = access items"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
