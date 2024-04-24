import threading

import fake_requests as requests


class GetWeatherThread(threading.Thread):
    def __init__(self, date):
        super().__init__()
        self.date = date
        self.response = None

    def run(self):
        self.response = requests.get(f'http://weather.com/london/{self.date}')

# Create a thread to fetch each date
threads = [
    GetWeatherThread(date)
    for date in ['29_07_2020', '28_07_2020', '27_07_2020']
]

# Start all of the threads
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()  # Wait for the thread to complete
    print(f'The weather on {thread.date} was {thread.response}')
