"""
The code below takes 10 username-password combinations, and securely hashes
the passwords using a slow hashing algorithm. It writes the hashed results to
a file, along with the username and a 'salt' used in the hashing.

This process is deliberately CPU expensive, to make brute-force attacks hard.

* Update the code so that each password is hashed in a separate process.
* Make sure that the final output is only printed once all processes have
  completed.

Note:
the imported PASSWORDS is a dictionary mapping from username to password, e.g:
{
    'geri.hallibut@gmail.com':       'password123',
    'sealion@dion.com':              'better9098!pw01',
    'w.a.floatzart@music.com':       'iHEARTsymphonies',
}
"""

import multiprocessing
import pathlib
import time

from utils import hash_password, PASSWORDS  # a dict of { username : password }


def save_hashed_password(username, password, path):
    """Hash password, and append it to path with its salt and username"""
    hashed_password, salt = hash_password(password)
    with open(path, 'a') as file:
        file.write(f'{username}, {salt}, {hashed_password}\n')
    print('.', end='', flush=True)


if __name__ == '__main__':
    start_time = time.time()  # Used to time the execution of this script

    # Define the hashed passwords file path, and create a blank file there
    target_path = pathlib.Path(__file__).parent / 'hashed_passwords.txt'
    with open(target_path, 'w'):
        pass

    # TODO: Move each the call to save_hashed_password into its own process
    for username, password in PASSWORDS.items():
        save_hashed_password(username, password, target_path)

    print(f'Done in {time.time() - start_time:.2f}.')
    print(f'Hashed passwords saved to: {target_path}')
