"""
The `add_unique_line` function writes new lines to file, but only if they
are not already in the file, ensuring that no repeats are written.

The `fetch_quote` function uses `add_unique_line` to create a file which
contains all of the unique quotes returned by 'http://shakespeare.com/quote'

At the moment, this code suffers from a race condition:


1. Run this script, and look at the contents of the quotes.txt file that's been
   created in this directory. If the script were working correctly, there would
   be 38 quotes in the file.

   You may see some garbled content, and some threads might also have raised
   UnicodeDecodeError exceptions.

2. Use a lock in the `add_unique_line` method to protect the file access, and
   prevent different threads from interfering with the updates.

3. Run the script again, and make sure that the quotes.txt file now contains
   38 rows, all of which should start with QUOTE XX for some quote number.
"""

import pathlib
import threading

import fake_requests as requests


# Do not edit these two lines: They create (or overwrite) the quotes.txt file
# which will be updated when this script runs.
QUOTES_PATH = pathlib.Path(__file__).parent / 'quotes.txt'
QUOTES_PATH.write_text('')


def add_unique_line(path, line):
    """Adds new unique lines to the file, and sorts the lines"""
    with open(path) as file:
        current_lines = set(file.readlines())

    # If line is already in current_lines then this will not change the set
    current_lines.add(line + '\n')

    with open(path, 'w') as file:
        file.writelines(sorted(current_lines))


def fetch_quote():
    """Get a Shakespeare quote, add it to the QUOTES_PATH file, and print it"""
    url = 'http://shakespeare.com/quote'
    quote = requests.get(url)
    add_unique_line(QUOTES_PATH, quote)
    print("Fetched:", quote)


N_REQUESTS = 300

for _ in range(N_REQUESTS):
    thread = threading.Thread(target=fetch_quote)
    thread.start()
