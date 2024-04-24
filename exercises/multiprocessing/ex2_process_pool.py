"""
The code below is similar to the previous exercise, hashing passwords with a
CPU-intensive algorithm. Follow the instructions further down to update the
script so that it runs using a process pool.
"""

import multiprocessing
import pathlib
import time

from utils import hash_password, PASSWORDS  # a dict of { username : password }


def write_to_file(path, username, salt, hashed_password):
    """Write username, salt and hashed_password to file, separated by commas"""
    with open(path, 'a') as file:
        file.write(f'{username}, {salt}, {hashed_password}\n')
    print('.', end='', flush=True)


if __name__ == "__main__":
    start_time = time.time()  # Used to time the execution of this script

    # Define the hashed passwords file path, and create a blank file there
    target_path = pathlib.Path(__file__).parent / 'hashed_passwords_2.txt'
    with open(target_path, 'w'):
        pass

# <<<<<<<<<<<<<<<<<<<<<<<<<<<< INSTRUCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Update this code to use queues, and a process pool of 4 workers
#
# You'll need to:
#   1. Create two queues, one to contain jobs in the form of (username, password)
#      tuples, and one to contain results in the form of (username, salt,
#      hashed_password) tuples.
#   2. Define a worker function, which gets jobs from the job queue, hashes
#      the password, and adds items to the results queue.
#   3. Create, and start 4 processes, each of which runs the worker function.
#   4. Update the for loop below so that it adds each (username, password) tuple
#      to the jobs queue.
#   5. Uncomment the while loop to take results off the result queue and write
#      them to file.

    job_queue = ...
    result_queue = ...


    for username, password in PASSWORDS.items():
        hashed_password, salt = hash_password(password)
        write_to_file(target_path, username, salt, hashed_password)


    # while not result_queue.empty():
    #     username, salt, hashed_password = result_queue.get()
    #     write_to_file(target_path, username, salt, hashed_password)


    # <<<<<<<<<<<<<<< DON'T CHANGE THE CODE BELOW HERE >>>>>>>>>>>>>>>>>>>>>>>>>

    print(f'Done in {time.time() - start_time:.2f}.')
    print(f'Hashed passwords saved to: {target_path}')
