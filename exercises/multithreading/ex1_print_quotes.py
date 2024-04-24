"""
At the moment, the code below fetches 10 Shakespeare quotes from a website
in a loop. Each of the requests is slow, so collecting 10 takes some time.

Update the code so that 10 separate threads are used to fetch the quotes. You
will need to replace the `for` loop, but don't edit any other code.

You will need to:

1. Wrap each call to `print_quote` in a separate thread
2. Start each thread running
3. Join the threads, so `All done` only prints when the threads are finished

Do not edit the `print_quote` function
"""

import threading
import time

# The fake_requests module is used to fake slow web requests
import fake_requests as requests


start_time = time.time()  # This is used to time the execution of the script

def print_quote():
    """Get and print a Shakespeare quote. Do NOT edit this function"""
    start = time.time()
    quote = requests.get('http://shakespeare.com/quote')
    speed = time.time() - start
    print(f"({speed:.1f}s)", quote)


# <<< YOUR CODE SHOULD REPLACE THE for LOOP BELOW >>>


for _ in range(10):
    print_quote()


# <<< DO NOT EDIT THE LINES BELOW HERE >>>

total_time = time.time() - start_time
print(f'All done in {total_time:.1f}s')
