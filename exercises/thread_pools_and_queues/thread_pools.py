"""
The code below fetches temperature data from a (mocked) website for 4 cities
for every day of 2019, then calculates the average for each city.

* Read through the script to make sure you understand roughly what each stage
  is doing. (Part 1. is setting up a queue of tasks to run, Part 2. is making
  the requests and adding them to a results queue, and Part 3. is aggregating
  and printing the results)

* Update just Part 2. of this script so that instead of making all the requests
  on a single thread, it uses 50 worker threads. These should each take tasks
  from the task queue, and add results to the results queue.

  Make sure that:

    * All tasks are complete before the results are collected.
    * The program (and all threads) will terminate when the work is complete.
"""

import queue
import threading

from utils import get_temperature, cities, dates

# def get_temperature(city, date) -> temperature as a float
# cities = ['Lagos', 'Cairo', 'Kigali', 'Luanda']
# dates = ['20190101', '20190102', '20190103', ...]


# Initialize task and results queues
tasks = queue.Queue()
results = queue.Queue()


# ADD TASKS TO THE TASK QUEUE (as a city, date tuple)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

for city in cities:
    for date in dates:
        tasks.put((city, date))


# FETCH RESULTS, AND ADD THESE TO THE RESULTS QUEUE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TODO Replace this loop, so that it uses a pool of threads to execute the
# calls to get_temperature. You can still add the results to the results queue.
while not tasks.empty():
    city, date = tasks.get()
    temperature = get_temperature(city, date)
    results.put((city, temperature))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#             <<< DO NOT EDIT THE CODE BELOW THIS LINE >>>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Collect results from the queue, and print statistics
all_results = {city: [] for city in cities}

# Collect all the results from the results queue
while not results.empty():
    city, temperature = results.get()
    all_results[city].append(temperature)

# Calculate aggregates, and print out the results
print('\nRESULTS:')
for city, temperatures in all_results.items():
    average = sum(temperatures) / len(temperatures)
    print(
        f"\t{city}:\tAverage Temperature: {average:.1f}°C "
        f"(range {min(temperatures):.1f} - {max(temperatures):.1f}) "
        f"[from {len(temperatures)} readings]"
    )
