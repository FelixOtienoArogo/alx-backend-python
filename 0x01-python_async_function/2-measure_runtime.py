#!/usr/bin/env python3
"""measure_time."""


import asyncio
import time
import random
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Description.

    -----------
    Measure the total execution time for wait_n(n, max_delay), and
    return total_time / n.
    """
    start_time = time.perf_counter()
    out: List[float] = asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time: float = end_time - start_time

    return (total_time / n)
