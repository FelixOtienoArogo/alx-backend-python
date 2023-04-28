#!/usr/bin/env python3
"""sum_mixed_list."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Take a list of ints and float and return sum as float.

    ------------------------------------------------------
    Param: mxd_lst.
    """
    tot: float = 0
    for num in mxd_lst:
        tot += num
    return (tot)
