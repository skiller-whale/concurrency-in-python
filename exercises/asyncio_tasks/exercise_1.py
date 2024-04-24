import asyncio
import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / 'data'

# pylint: disable=pointless-string-statement
"""
This code calculates Euler's number (e) and PI. Currently it is waiting
    for both tasks before it stores the results in a file.

N.B.: You don't need to understand or edit the code that computes e or PI.

This is not good behavior, as if something happens (computer crashes,
    task gets cancelled, etc.), you lose what one function computed.

1. Convert the `asyncio.gather` call to use `asyncio.create_task` calls instead.

2. Write a loop that checks if either task is done and stores the result
    in "data/results.json" by calling `store_results` appropriately.
"""


async def compute_pi(it):
    """Compute pi using Madhava-Leibniz series.

    Args:
        it (int): The number of iteration of the series.

    Returns:
        float: pi
    """
    pi, sign = 0.0, 1

    for i in range(it):
        pi += sign * 4.0 / (2 * i + 1)
        sign *= -1

        await asyncio.sleep(0)

    return pi


async def compute_e(it):
    """Computes Euler's constant using the series:
       1/0! + 1/1! + 1/2! + 1/3! + ...

    Args:
        it (int): The number of iterations.

    Returns:
        float: e
    """
    e, fact = 0, 1
    for i in range(it):
        if i > 0:
            fact *= i
        e += 1 / fact

        await asyncio.sleep(0)
    return e


def store_results(results, file_path):
    """Stores results as JSON in file_path.

    Args:
        results (dict): Any serializable dictionary.
        file_path (str): Path to file.
    """
    print(f'Storing results in {file_path}.')
    with open(file_path, 'w') as f:
        f.write(json.dumps(results))


async def main_async():
    e, pi = await asyncio.gather(
        compute_e(it=10_000),
        compute_pi(it=100_000)
    )

    results = {
        'e': e,
        'pi': pi
    }

    store_results(results, DATA_PATH / 'results.json')


if __name__ == '__main__':
    # Call main_async to schedule all tasks
    asyncio.run(main_async())
