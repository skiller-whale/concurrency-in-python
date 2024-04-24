"""
This script will check each of the numbers between RANGE_START and
(RANGE_START + RANGE_SIZE) to see which ones are prime. It will print out all
of the prime numbers (but not necessarily in order)

This uses a 'naive' (slow) method is_prime, and speeds up the work by using
multiple processes. The number of processes is determined by N_PROCESSES
"""

import multiprocessing
import time

from utils import split_range, is_prime


RANGE_START = 100_000_000_000_000     # The start of the range to check
RANGE_END   = 100_000_000_000_200     # The end of the range to check

N_PROCESSES = 8


# Define the is_prime and print_primes functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def print_primes(range_start, range_end):
    for number in range(range_start, range_end):
        if is_prime(number):
            print(number)


if __name__ == '__main__':

    # Split the range up evenly for different processes
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    print(f"Finding prime numbers between {RANGE_START} and {RANGE_END}.")
    print(f"Using {N_PROCESSES} processes, checking the sub-ranges:")
    for i, (start, end) in enumerate(split_range(RANGE_START, RANGE_END, N_PROCESSES)):
        print(f"Process {i}: {start} - {end}")


    # Parallelize the calculation
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    print("\nFound Primes:")
    start_time = time.time()

    # Create one process for each sub-range
    processes = [
        multiprocessing.Process(target=print_primes, args=(start, end))
        for start, end in split_range(RANGE_START, RANGE_END, N_PROCESSES)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f"Done. Calculation took {time.time() - start_time:.2f}s")
