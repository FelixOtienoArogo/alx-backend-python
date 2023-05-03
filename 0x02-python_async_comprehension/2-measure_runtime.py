#!/usr/bin/env python3
"""measure_runtime."""


import asyncio
import random
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Description.

    ------------
    coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather
    """
    start = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    return time.time() - start
