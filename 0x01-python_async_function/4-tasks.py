#!/usr/bin/env python3

'''
The code is nearly identical to wait_n except task_wait_random is being called.
'''

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Call wait_random n times
    '''

    sTasks = []

    tasks = [task_wait_random(max_delay) for time in range(n)]

    for sort in asyncio.as_completed(tasks):
        value = await sort
        sTasks.append(value)
    return sTasks
