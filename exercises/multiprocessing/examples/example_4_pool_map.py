"""
This script is an alternative to example_3, using a multiprocessing.Pool to
return the calculated prime numbers.
"""

import multiprocessing
import time

from utils import is_prime


RANGE_START = 100_000_000_000_000     # The start of the range to check
RANGE_END   = 100_000_000_000_200     # The end of the range to check

N_PROCESSES = 4


start_time = time.time()

if __name__ == '__main__':
    with multiprocessing.Pool(processes=N_PROCESSES) as pool:
        numbers = range(RANGE_START, RANGE_END)
        result = pool.map(is_prime, numbers)

    primes = [number for number, is_a_prime in zip(numbers, result) if is_a_prime]


    print(f"Done. Calculation took {time.time() - start_time:.2f}s")
    print("All primes found:")
    print(primes)
