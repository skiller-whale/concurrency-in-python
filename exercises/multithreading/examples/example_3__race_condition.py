import threading


class StockCounter:
    def __init__(self):
        self.counts = dict(eggs=0, milk=0, bread=0)

    def plus_one(self, item):
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
