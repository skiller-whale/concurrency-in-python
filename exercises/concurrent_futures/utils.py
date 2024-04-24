import os
import fake_requests as requests

from datetime import datetime, timedelta
from hashlib import pbkdf2_hmac  # An (intentionally) expensive hashing function


def hash_password(password, n_iterations=2_000_000):
    """Hash a password using a random salt, and save it to the file at path

    This is intentionally CPU intensive, so that brute-force attacks are hard
    """
    salt = os.urandom(32)
    result = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, n_iterations)
    return result, salt


# A dict of username : password pairs that need hashing
PASSWORDS = {
    'mark@whaleburg.com':            'hello_nice_day',
    'shark.whalburg@gmail.com':      'another-insecure-password!',
    'sting-ray.charles@hotmail.com': 'mothers!maiden!name',
    'oprahswimfrey@googlemail.com':  'strong943lkOIlknv!-PASsWord',
    'skate_winslet@gmail.com':       'weak_pw1',
    'whoopee@goldfish.com':          'weak_pw2',
    'geri.hallibut@gmail.com':       'dont-do-this',
    'sealion@dion.com':              'better9098kalsie!pw01',
    'agatha.fishtie@yahoo.com':      'password123',
    'w.a.floatzart@music.com':       'another-weakish-password',
}


def get_temperature(city, date):
    """Fetches the temperature in the given city, on the given date"""
    url = f'http://world_temperature.com/{city}/{date:%Y%m%d}'
    response = requests.get(url, max_wait=0.01)
    return float(response)


# Initialise a set of cities, and the dates we wish to query
cities = ['Lagos', 'Cairo', 'Kigali', 'Luanda']
dates = [datetime(year=2019, month=1, day=1) + timedelta(days=i) for i in range(365)]
