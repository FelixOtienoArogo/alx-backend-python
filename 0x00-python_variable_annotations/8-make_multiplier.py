#!/usr/bin/env python3
"""make_multiplier."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Description.

    -----------

    takes a float and returns a function that multiplies a float by multiplier.
    """
    return (lambda x: x * multiplier)
