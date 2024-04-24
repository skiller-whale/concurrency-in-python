"""
The code below is similar to the previous exercise, hashing passwords with a
CPU-intensive algorithm. Follow the instructions further down to update the
script so that it runs using the Pool class of multiprocessing.
"""

import multiprocessing
import pathlib
import time

from utils import hash_password, PASSWORDS


# Define the hashed passwords file path, and create a blank file there
target_path = pathlib.Path(__file__).parent / 'hashed_passwords_3.txt'
with open(target_path, 'w'):
    pass


def save_hashed_password(username, password):
    """Hash password, and append it to path with its salt and username"""
    hashed_password, salt = hash_password(password)
    with open(target_path, 'a') as file:
        file.write(f'{username}, {salt}, {hashed_password}\n')
    print('.', end='', flush=True)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<< INSTRUCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Update this code to use a `multiprocessing.Pool`, with 4 processes
#
# You can either do this using apply_async or map
#
#   1. Create a multiprocessing.Pool with 4 workers.
#
#   IF you use apply_async:
#
#      2. Call apply_async with save_hashed_password for each (username, password)
#         combination, and keep track of the returned result
#      3. Call .get() on each of the results to block the program until all
#         processes have completed.
#
#   IF you use map:
#
#      2. Modify the save_hashed_password function so that it expects a tuple
#         (username, password) instead of two separate arguments. This is needed
#         because map only supports one iterable argument.
#      3. Call map with save_hashed_password and PASSWORDS.items(). This works
#         because .items returns (username, password) tuples.

if __name__ == '__main__':

    start_time = time.time()  # Used to time the execution of this script

    for username, password in PASSWORDS.items():
        save_hashed_password(username, password)


    # <<<<<<<<<<<<<<< DON'T CHANGE THE CODE BELOW HERE >>>>>>>>>>>>>>>>>>>>>>>>>

    print(f'Done in {time.time() - start_time:.2f}.')
    print(f'Hashed passwords saved to: {target_path}')
