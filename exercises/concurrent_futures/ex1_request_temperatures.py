"""
The code below fetches temperature data from a (mocked) website for 4 cities
for every day of 2019, then calculates the average for each city.

Update the fetch_results function so that it:

* Creates an appropriate executor from the `concurrent.futures` module
* Uses the `executor.map` method to concurrently fetch all of the temperature
  results for each city (it might be easiest to call map once for each city)

The results dictionary created should be identical after your change.
"""
import time

from utils import get_temperature, cities, dates


def fetch_results():
    # Initialize empty array of results
    results = {city: [] for city in cities}

    # For each city get the temperature for each date,and add it to the relevant list
    for city in cities:
        for date in dates:
            temp = get_temperature(city, date)
            results[city].append(temp)

    return results


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#             <<< DO NOT EDIT THE CODE BELOW THIS LINE >>>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    start_time = time.time()  # Used to time the execution of this script
    results = fetch_results()
    # Calculate aggregates, and print out the results
    print('\nRESULTS:')
    for city, temperatures in results.items():
        average = sum(temperatures) / len(temperatures)
        print(
            f"\t{city}:\tAverage Temperature: {average:.1f}°C "
            f"(range {min(temperatures):.1f} - {max(temperatures):.1f}) "
            f"[from {len(temperatures)} readings]"
        )
    print(f'Done in {time.time() - start_time:.2f}s.')
