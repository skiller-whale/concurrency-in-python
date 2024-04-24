import time
from datetime import datetime, timedelta

import fake_requests as requests


def log_message(tag, message):
    """Log messages to the console with a timestamp and tag"""
    # time.sleep() are here to artificially increase likelihood of race
    # conditions for the purpose of exercises.
    print('  ', datetime.now(), end=' | ')
    time.sleep(0.001)
    print(tag.upper(), end=' | ')
    time.sleep(0.001)
    print(message)


def get_temperature(city, date):
    """Fetches the temperature in the given city, on the given date"""
    url = f'http://world_temperature.com/{city}/{date:%Y%m%d}'
    response = requests.get(url, max_wait=0.01)
    return float(response)


# Initialise a set of cities, and the dates we wish to query
cities = ['Lagos', 'Cairo', 'Kigali', 'Luanda']
dates = [datetime(year=2019, month=1, day=1) + timedelta(days=i) for i in range(365)]
