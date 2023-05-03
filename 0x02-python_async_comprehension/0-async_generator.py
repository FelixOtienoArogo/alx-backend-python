"""async_generator."""
import asyncio
import random


async def async_generator():
    """
    Description.

    ------------
    he coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    for i in range(10):
        num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield num
