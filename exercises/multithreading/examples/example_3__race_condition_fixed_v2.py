import threading

# This solution uses three locks in the StockCounter class, one for each dict
# key. This will perform much faster than example_3__race_condition_fixed.py
# because threads are only blocked from updating a value by another thread if
# it is updating the same value.
#
# This works because updating two different values in a dictionary is not
# vulnerable to a race condition. Each separate value can therefore be
# separately protected by its own lock.


class StockCounter:
    def __init__(self):
        self.counts = dict(eggs=0, milk=0, bread=0)
        # Create one lock for each key in the dictionary
        # (different keys will not interfere with each other)
        self.locks = {key: threading.Lock() for key in self.counts}

    def plus_one(self, item):
        with self.locks[item]:
            self.counts[item] += 1


def stock_taker(counter, item):
    for _ in range(100_000):
        counter.plus_one(item)


threads = []
counter = StockCounter()


# Create and start 10 threads to count each item (eggs, milk and bread)
for item in 'eggs', 'milk', 'bread':
    for _ in range(10):
        thread = threading.Thread(target=stock_taker, args=(counter, item))
        thread.start()
        threads.append(thread)

# Wait for all of the threads to complete
for thread in threads:
    thread.join()

print(counter.counts)
