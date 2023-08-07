#!/usr/bin/env python3

"""
Module: my_module
This module defines an asynchronous coroutine for waiting a random delay.
"""

import asyncio
import random

async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (float, optional): Maximum delay in seconds (inclusive). Defaults to 10.

    Returns:
        float: Random delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Example usage
async def main():
    random_delay = await wait_random()
    print(f"Random delay: {random_delay:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
