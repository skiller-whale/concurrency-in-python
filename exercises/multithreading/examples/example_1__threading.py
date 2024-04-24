import threading
import time

import fake_requests as requests


def print_weather(date):
    request_start = time.time()
    response = requests.get(f'http://weather.com/london/{date}')
    request_time = time.time() - request_start
    print(f'{date}: {response} (request took {request_time:.1f}s)')


program_start = time.time()

# Create a list of threads (but don't start them running yet)
threads = [
    threading.Thread(target=print_weather, args=(date,))
    for date in ['29_07_2020', '28_07_2020', '27_07_2020']
]

# Start all of the threads running
for thread in threads:
    thread.start()

# Wait for all of the threads to complete and rejoin the main flow
for thread in threads:
    thread.join()

print(f"Completed in ({time.time() - program_start:.1f}s)")
