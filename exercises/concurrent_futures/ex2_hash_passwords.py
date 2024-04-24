"""
The code in the hash_passwords function below:

1. Iterates through a dictionary of {username: password} pairs (PASSWORDS).
2. Calls the `hash_password` function for each password, which returns a
   password hash and a 'salt'.
3. Calls the `write_to_file` function for each username, hashed_password and salt

This uses a CPU-intensive algorithm to hash the passwords.

Update the hash_passwords function to use concurrent.futures with `submit` to
parallelise the slow part of the process.

You'll need to:

  1. Create an appropriate executor (remember this is a CPU-bound task)
  2. Call .submit with each (username, password) combination and keep track
     of the futures returned.

     You'll also need to match these futures with their corresponding
     username, (e.g. you might want to store them as a {username: future} dict)
  3. Loop over these returned futures to get the results, and call
     write_to_file to write the results back to the file.
"""

import pathlib
import time

from utils import hash_password, PASSWORDS  # a dict of { username : password }


def write_to_file(path, username, salt, hashed_password):
    """Write username, salt and hashed_password to file, separated by commas"""
    print(f"Saving password for {username}")
    with open(path, 'a') as file:
        file.write(f'{username}, {salt}, {hashed_password}\n')


# <<<<<<<<<<<<<<<<< DON'T CHANGE THE CODE ABOVE HERE >>>>>>>>>>>>>>>>>>>>>>>>>>>


def hash_passwords():
    for username, password in PASSWORDS.items():
        hashed_password, salt = hash_password(password)
        write_to_file(target_path, username, salt, hashed_password)


# <<<<<<<<<<<<<<<<< DON'T CHANGE THE CODE BELOW HERE >>>>>>>>>>>>>>>>>>>>>>>>>>>

if __name__ == '__main__':
    start_time = time.time()  # Used to time the execution of this script

    # Define the hashed passwords file path, and create a blank file there
    target_path = pathlib.Path(__file__).parent / 'hashed_passwords.txt'
    with open(target_path, 'w'):
        pass

    hash_passwords()

    print(f'Done in {time.time() - start_time:.2f}s.')
    print(f'Hashed passwords saved to: {target_path}')
