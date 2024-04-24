"""
At the moment, the code below fetches 10 Shakespeare quotes from a website
in a loop (using a list comprehension). Each of the requests is slow, so
collecting all 10 takes some time.

Update the code so that 10 separate threads are used to fetch the quotes, and
return the result. You will need to update the code between the two comment
lines starting and ending with <<< ... >>>

You will need to:

1. Create a new subclass of `threading.Thread` called `GetQuoteThread`. When
   run, this thread should implement the behaviour of the `get_quote` method
2. Create 10 instances of this thread, and start each one running
3. Join all of the threads, to ensure that all the results have been fetched
4. Update the `for` loop, so that it correctly prints out the returned values
"""

import threading
import time

# The fake_requests module is used to fake slow web requests
import fake_requests as requests


start_time = time.time()  # This is used to time the execution of the script

# <<< DO NOT EDIT THE LINES ABOVE HERE >>>


def get_quote():
    return requests.get('http://shakespeare.com/quote')


quotes = [get_quote() for _ in range(10)]

for quote in quotes:
    print(quote)


# <<< DO NOT EDIT THE LINES BELOW HERE >>>

total_time = time.time() - start_time
print(f'All done in {total_time:.1f}s')
