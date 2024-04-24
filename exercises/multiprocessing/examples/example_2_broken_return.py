"""
This script is a broken attempt to do the same thing as example_1, but
returning prime numbers instead of printing them out.

This doesn't work because each process works on a copy of the memory, so the
original list in the main process is not modified.
"""

import multiprocessing
import time

from utils import split_range, is_prime


RANGE_START = 100_000_000_000_000     # The start of the range to check
RANGE_END   = 100_000_000_000_200     # The end of the range to check

N_PROCESSES = 8


# Define a process subclass, which calculates the primes in a given range
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class PrimesInRange(multiprocessing.Process):
    def __init__(self, range_start, range_end):
        super().__init__()
        self.range_start = range_start
        self.range_end = range_end
        self.primes = []

    def run(self):
        for number in range(self.range_start, self.range_end):
            if is_prime(number):
                print(f"Found {number}")
                self.primes.append(number)

if __name__ == '__main__':
    start_time = time.time()

    # Create one process for each sub-range
    processes = [
        PrimesInRange(start, end)
        for start, end in split_range(RANGE_START, RANGE_END, N_PROCESSES)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


    print(f"Done. Calculation took {time.time() - start_time:.2f}s")
    print("Primes found by each process:")
    for process in processes:
        print(f"Range {process.range_start} - {process.range_end}:", end='\t')
        # This fails, because the primes list has only been updated in the copied
        # memory available to the subprocess
        print(process.primes)
