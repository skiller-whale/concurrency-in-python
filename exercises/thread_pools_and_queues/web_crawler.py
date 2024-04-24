"""
The code below 'crawls' a website, "whalesipedia.com", to recursively find all
of the pages that are linked to from the homepage. Note that this script does
not need to handle 'cycles' or duplicates (each url will only be linked to from
one page, without any cycles).

* Read through the script to make sure you understand roughly what is happening
* Run the script. At the moment, this script works on a single thread, and takes
  several seconds to crawl the website for pages.
* Update the script so that it uses a pool of 10 threads to crawl the site.
  Each worker should be able to take urls off a queue, and add new ones back onto
  the queue.
* Run the script again, and check it has worked. The time taken should be < 1s.

HINTS:
 - Update pages_to_visit, so that it is a queue instead of a list.
 - Put most of the code in the while loop inside a worker function.
 - Make this worker function the target for 10 threads, and start them running.
"""

import threading
import queue
import json
import time

import fake_requests as requests
start_time = time.time()


def extract_links(url):  # YOU DON'T NEED TO EDIT THIS FUNCTION
    """Extract a list of web links from a web response"""
    response = requests.get(url)
    data = json.loads(response)
    return data['links']


# TODO: Replace pages_to_visit with a task queue
pages_to_visit = [] # Keep a list of the pages that still need to be visited
pages_to_visit.append('http://whalesipedia.com')

all_urls = [] # Keep track of all urls that have been visited


# TODO: Replace this loop with a pool of 10 workers threads.
while pages_to_visit:
    url = pages_to_visit.pop()
    for link in extract_links(url):
        pages_to_visit.append(link)

    all_urls.append(url)


# Print out the complete set of urls found
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for url in all_urls:
    print(url)

print(f"Time taken to index website: {time.time() - start_time:.2f}s")
