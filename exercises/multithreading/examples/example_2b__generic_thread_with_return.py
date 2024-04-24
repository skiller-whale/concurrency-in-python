import threading

import fake_requests as requests


# The ThreadWithReturn class can be used instead of the `threading.Thread` class
# to return the target's return value from `.join()`.

class ThreadWithReturn(threading.Thread):
    """A generic sub-in replacement for threading.Thread with a return value"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.return_value = None

    def run(self):
        if self._target is not None:
            self.return_value = self._target(*self._args, **self._kwargs)

    def join(self, timeout=None):
        super().join(timeout=timeout)
        return self.return_value


# The code below uses the generic ThreadWithReturn class to call the
# get_weather function concurrently.


def get_weather(date):
    return requests.get(f'http://weather.com/london/{date}')


dates = ['29_07_2020', '28_07_2020', '27_07_2020']

# Create a thread to fetch each date
threads = [ThreadWithReturn(target=get_weather, args=(date,)) for date in dates]

# Start all of the threads
for thread in threads:
    thread.start()

# Wait for all the threads to complete and get return values
results = [thread.join() for thread in threads]

# Print out the results
for date, result in zip(dates, results):
    print(f'The weather on {date} was {result}')
