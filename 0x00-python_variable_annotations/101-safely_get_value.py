#!/usr/bin/env python3
"""
Given the parameters and the return values,
add type annotations to the function

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T,
                     None] = None) -> Union[Any, T]:
    """Return value and annotation type"""
    if key in dct:
        return dct[key]
    else:
        return default
