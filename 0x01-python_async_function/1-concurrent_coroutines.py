#!/usr/bin/env python3
"""wait_n."""


import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Description.

    -----------
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
    """
    out: List[float] = []
    i: int = 0
    while (i < n):
        dig = await wait_random(max_delay)
        out.append(dig)
        i += 1
    return out
