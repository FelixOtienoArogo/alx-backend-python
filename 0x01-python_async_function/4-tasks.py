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
    buf: List[float] = []
    out: List[float] = []

    for i in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: out.append(x.result()))
        buf.append(task)

    for j in buf:
        await j

    return out
