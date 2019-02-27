#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""To make the code below work, create a parametrized decorator named “caching”.
Store it in a separate module named “functional_utils”.
Let it accept timeout as an argument for return values retention"""

import time

__author__ = "Sergey_Matusevich"


def caching(timeout):
    start_time = time.time()
    results = {}

    def wrapper(func):
        def inner():
            if time.time() - start_time >= timeout:
                results.clear()
            if 'key' not in results:
                results['key'] = func()
            return results['key']

        return inner

    return wrapper
