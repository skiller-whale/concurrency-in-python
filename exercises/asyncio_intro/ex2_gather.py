import asyncio
import time
from utils.async_file import read_and_print_file_async
from example_data import USERS_FILE_PATH

# pylint: disable=pointless-string-statement
"""
USING GATHER TO RUN COROUTINES CONCURRENTLY
-------------

In this exercise you will use `asyncio.gather` to execute coroutines concurrently.

* Implement `main_async` to use `asyncio.gather` and run the coroutines
    `print_after_delay_async(0.5, f"Reading file {USERS_FILE_PATH.name}` and
    `read_and_print_file_async(USERS_FILE_PATH)` concurrently.

* Extract the number of lines read from `asyncio.gather` and print it.

* Was the message f"Reading file {USERS_FILE_PATH.name}" printed before the file was read?

"""


async def print_after_delay_async(delay, message):
    await asyncio.sleep(delay)
    print(message)


async def main_async():
    # TODO: Implement main_async to use `asyncio.gather`
    #   to run `print_after_delay_async` and 
    #   `read_and_print_file_async` concurrently
    pass


if __name__ == "__main__":
    start_time = time.time()

    asyncio.run(main_async())

    end_time = time.time()
    print(f"Reading file took {(end_time - start_time):.3f} seconds.")

