#!/usr/bin/env python3
"""sum_list."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Take a list of floats and returns the sum.

    ------------------------------------------
    Parameter: input_list
    """
    tot: float = 0
    for num in input_list:
        tot += num
    return tot
