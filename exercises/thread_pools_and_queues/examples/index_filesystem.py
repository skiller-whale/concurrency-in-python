import os
import queue
import threading


tasks = queue.Queue()
results = queue.Queue()


# Create and start a thread to print out any results that are added to the queue

def print_results():
    while True:
        print("\t", results.get(), flush=True)
        results.task_done()

threading.Thread(target=print_results, daemon=True).start()


# Create a pool of 20 worker threads, which recursively search directories

def search_recurse():
    while True:
        try:
            path = tasks.get()
            for items in os.listdir(path):
                subpath = os.path.join(path, items)

                results.put(subpath)  # Add all found paths to the results

                if os.path.isdir(subpath):
                    tasks.put(subpath)  # Add subdirectories back to the queue

        except Exception:
            pass  # Ignore exceptions, but keep the thread alive

        finally:
            tasks.task_done()

for _ in range(20):
    threading.Thread(target=search_recurse, daemon=True).start()


# Add the root directory to the tasks list, and wait for the queues to join.
SEARCH_PATH = '/'  # You might want to change this to a smaller root
tasks.put(SEARCH_PATH)

tasks.join()
results.join()

print("Done")
