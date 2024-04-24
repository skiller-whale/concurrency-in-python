"""
This script is an alternative to example_3, using a multiprocessing.Pool to
return the calculated prime numbers.
"""

import multiprocessing
import time

from utils import is_prime


RANGE_START = 100_000_000_000_000     # The start of the range to check
RANGE_END   = 100_000_000_000_200     # The end of the range to check

N_PROCESSES = 8


if __name__ == '__main__':
    start_time = time.time()

    with multiprocessing.Pool(processes=N_PROCESSES) as pool:
        results = {
            number: pool.apply_async(is_prime, (number,))
            for number in range(RANGE_START, RANGE_END)
        }

        # The call to result.get() is blocking, and returns True or False
        primes = [number for number, result in results.items() if result.get()]


    print(f"Done. Calculation took {time.time() - start_time:.2f}s")
    print("All primes found:")
    print(primes)
