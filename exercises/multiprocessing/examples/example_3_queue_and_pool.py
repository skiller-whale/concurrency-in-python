"""
This script is a fixed version of example_2, using a process pool and queue to
return the calculated prime numbers.
"""

import multiprocessing
import time

from utils import split_range, is_prime


RANGE_START = 100_000_000_000_000     # The start of the range to check
RANGE_END   = 100_000_000_000_200     # The end of the range to check

N_PROCESSES = 8


# Create a queue of numbers to check, and prime numbers that are found
numbers_queue = multiprocessing.JoinableQueue()
primes_queue = multiprocessing.Queue()


# Define a worker, which interacts with the Queues
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def worker(tasks_queue, results_queue):
    while True:
        try:
            number = tasks_queue.get()
            if is_prime(number):
                print(f"Found {number}")
                results_queue.put(number)
        finally:
            tasks_queue.task_done()


if __name__ == '__main__':
    start_time = time.time()

    # Create several daemon worker processes
    for _ in range(N_PROCESSES):
        multiprocessing.Process(
            target=worker,
            args=(numbers_queue, primes_queue),
            daemon=True
        ).start()

    # Add each number to test to the numbers queue
    for n in range(RANGE_START, RANGE_END):
        numbers_queue.put(n)

    numbers_queue.join()  # Wait for all numbers to be processed


    print(f"Done. Calculation took {time.time() - start_time:.2f}s")
    print("All primes found:")

    results = []
    while not primes_queue.empty():
        results.append(primes_queue.get())
    print(results)
