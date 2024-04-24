import asyncio
import time
from utils.async_file import read_and_print_file_sync, read_and_print_file_async
from example_data import USERS_FILE_PATH

# pylint: disable=pointless-string-statement
"""
COROUTINES
-------------

Currently, this script uses synchronous functions to read a file line-by-line.
Your task is to write asynchronous functions that do the same.

* Run the script. How long does it take to run?

* Create a `main_async` coroutine and use `asyncio.run` to run it.

* Inside `main_async` use the coroutine `read_and_print_file_async`
    to read the file in USERS_FILE_PATH.

* Print the number of lines read.

* Create a function called `print_after_delay_async(delay, message)`, which
    should be the async equivalent of `print_after_delay_sync`.

* Use it to print `f"Reading file {USERS_FILE_PATH.name}"` after a 0.5 second delay.

* How long does it take to run the async version of the script?
"""


def print_after_delay_sync(delay, message):
    """Prints a message after a delay (synchronous)

    Args:
        delay (float): Delay (in seconds) to sleep for.
        message (str): Message to print.
    """
    time.sleep(delay)
    print(message)


def main_sync():
    """Synchronous main function.
    """
    print_after_delay_sync(0.5, f"Reading file {USERS_FILE_PATH.name}")
    lines_read = read_and_print_file_sync(USERS_FILE_PATH)
    print(f"Done, read {lines_read} lines!")


# TODO: Create and implement the coroutine main_async

# TODO: Create and implement the coroutine print_after_delay_async

if __name__ == "__main__":
    # NOTE: Do not remove timing computation
    start_time = time.time()

    ## TODO: Run main_async using asyncio.run instead
    main_sync()

    end_time = time.time()
    print(f"Reading file took {(end_time - start_time):.3f} seconds.")

