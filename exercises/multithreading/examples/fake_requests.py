import time
import random

# This module just exists to simulate slow web requests for the example code.
# Any call to `get` will sleep for between 2 and 4 seconds, before returning
# some weather data.


RESULTS = {
    'http://weather.com/london/29_07_2020': '20, cloudy',
    'http://weather.com/london/28_07_2020': '18, windy',
    'http://weather.com/london/27_07_2020': '19, sunny',
}


def get(url):
    time.sleep(random.uniform(2, 4))
    return RESULTS.get(url, 'no weather data for that day')
