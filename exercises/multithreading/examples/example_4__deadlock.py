import threading
import time


# In this basic example, two locks are used in opposite orders in different
# functions. Because each function acquires one lock and then waits for the
# other at the same time, a deadlock results.

# This example is intentionally minimal, so may seem a bit unrealistic. The
# exercise on deadlocks contains a more complicated / realistic example.


driver_lock = threading.Lock()
passenger_lock = threading.Lock()

def taxi():
    with driver_lock:
        time.sleep(0.5)
        print('Taxi driver is here, waiting for a passenger')
        with passenger_lock:
            print('The taxi is off')

def bus():
    with passenger_lock:
        time.sleep(0.5)
        print('Bus passenger is here, waiting for a driver')
        with driver_lock:
            print('The bus is off')


taxi_thread = threading.Thread(target=taxi)
bus_thread = threading.Thread(target=bus)

taxi_thread.start()
bus_thread.start()

print('Both started')

taxi_thread.join()
bus_thread.join()

print('All done')
