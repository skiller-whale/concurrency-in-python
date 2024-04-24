import itertools


def split_range(start, end, n):
    """Split a range up into n evenly sized sub-ranges"""
    range_size = end - start
    split_points = [start + (i * range_size) // n for i in range(n + 1)]
    return list(zip(split_points[:-1], split_points[1:]))


def is_prime(n):
    """Return True if n is a prime number or False otherwise

    This is a naive approach, that tests all numbers smaller than the square
    root of n until one of them is a divisor of n. It is intentionally slow.
    """
    divisor = 2
    while divisor ** 2 <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True
