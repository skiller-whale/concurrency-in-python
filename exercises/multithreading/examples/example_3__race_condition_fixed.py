import threading
import time


# This solution uses a lock in the StockCounter class to prevent more than one
# thread from updating the dictionary at the same time.
#
# There are three alternative methods for plus_one defined in the StockCounter
# class (with two of them commented out). Any of these methods would solve the
# problem, but the final (uncommented) one is preferred.


class StockCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.counts = dict(eggs=0, milk=0, bread=0)

    # def plus_one(self, item):
    #     self.lock.acquire()
    #     self.counts[item] += 1
    #     self.lock.release()

    # def plus_one(self, item):
    #     self.lock.acquire()
    #     try:
    #         self.counts[item] += 1
    #     finally:
    #         self.lock.release()

    def plus_one(self, item):
        with self.lock:
            self.counts[item] += 1


def stock_taker(counter, item):
    for _ in range(100_000):
        counter.plus_one(item)


threads = []
counter = StockCounter()


s = time.time()

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
print(time.time() - s)
