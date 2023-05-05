#!/usr/bin/env python3
"""wait_n."""


import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Description.

    -----------
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
    """
    result = []
    
    tasks = [task_wait_random(max_delay) for i in range(n)]

    for sort in asyncio.as_completed(tasks):
        val = await sort
        result.append(val)

    return result
