"""
The code below starts up two threads, one which regularly checks the free
disk space, and another which regularly monitors the number of memory blocks
allocated by the Python interpreter.

Both of these functions call the non thread-safe log_message function, which
should print out a message of the form    TIMESTAMP | TAG | VALUE   for example:

   2020-08-22 15:47:34.520069 | MEMORY BLOCKS | 31566

When you run this code, some of the log lines printed will probably appear
garbled like this:

   2020-08-22 15:54:10.883183 | MEMORY BLOCKS |    2020-08-22 15:54:10.883221 | FREE DISK SPACE | 88342376 31565


You'll need to hit Ctrl + C to stop the thread running.

--------------------------------------------------------------------------------

To avoid mixed up output (which is caused by a race condition), change the code
so that all logging is handled by a separate thread.

1. Create a new queue that will hold the data to be logged, and update
   `track_disk_space` and `track_memory_blocks` so they add to this queue,
   instead of calling `log_message` directly.

2. Create a new function, `process_log_queue` which repeatedly fetches items
   from the queue, and calls `log_message` for each item.

3. Run this function in a third thread, alongside the other threads. You should
   see that the log output all looks correct now.
"""

import queue
import shutil
import sys
import threading
import time

from utils import log_message


def track_disk_space():
    while True:
        log_message("free disk space", shutil.disk_usage(".").free)
        time.sleep(1./12)  # Check ~12 times per second


def track_memory_blocks():
    while True:
        log_message('memory blocks', sys.getallocatedblocks())
        time.sleep(1./30)  # Check ~30 times per second


threads = [
    threading.Thread(target=track_disk_space),
    threading.Thread(target=track_memory_blocks)
]

for thread in threads:
    thread.start()
