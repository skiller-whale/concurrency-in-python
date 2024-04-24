"""
The code below sends requests to 10 urls, and then prints them out in order of
how quickly the web request are returned.

At the moment, this script performs each request in the same thread, and then
prints out all results at the end. Update the code so that it uses:

* A concurrent.futures thread pool to make the web requests
* The submit method, to return futures for each request
* The concurrent.futures.as_completed function, to print results out in the
  order that they complete, as they complete.

Note: You might want to create a new function (e.g. `perform_check`), which will
      perform a web request, and then return the url that was called, rather
      than the response. This will make it easier to work out which url
      corresponds to each future.
"""
import time

import fake_requests as requests


# A list of 10 website endpoints which will return at different speeds
TEST_URLS = [
    f"http://www.speed-testing-website.com/test-{i}"
    for i in range(1, 11)
]


speeds = {}

for url in TEST_URLS:
    start = time.time()
    requests.get(url)
    speeds[url] = time.time() - start


for url, duration in sorted(speeds.items(), key=lambda x: x[1]):
    print(f"{url} (took {duration:.2f}s)")
