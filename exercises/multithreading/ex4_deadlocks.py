"""
The `Account` class below stores the balance of a bank account, and allows for
transfers to another account.

To ensure that no money is 'lost' because of race conditions, the `transfer_to`
method has a lock on both the account being transferred from, and the account
being transferred to.

1. Read through the `transfer_to` method, and make sure you understand how it
   works. This function acquires the lock for the Account, and the lock for the
   destination account, before adjusting the balances of both accounts.

2. Run the script. It creates a few threads, which each try to carry out a
   transaction. You should see a deadlock. (if you don't then try increasing the
   argument to time.sleep() from 0.1 to 0.5, and run the script again)

3. Update the way that locks are acquired in the `transfer_to` method, so that
   deadlocks are no longer a risk.

   Make sure that you keep `time.sleep(0.1)` in-between acquiring locks so you
   can be confident that you've actually solved the deadlock, rather than just
   making it less likely.

   There are a some hints at the bottom of the file if you aren't sure where to
   start.
"""

import threading
import time


class Account:
    def __init__(self, name, starting_balance):
        self.name = name
        self.balance = starting_balance
        self.lock = threading.Lock()

    def transfer_to(self, destination, amount, transaction_id):
        """Move money from this account to another `destination` account"""

        print(f"Transaction {transaction_id} waiting to lock {self.name}'s account")
        with self.lock:
            print(f"Transaction {transaction_id} locked {self.name}'s account")

            # Don't remove this line. The time.sleep() isn't causing the race
            # condition, it just makes it more likely to cause a deadlock each
            # time the code runs. Keeping it makes the code easier to debug
            time.sleep(0.1)

            print(f"Transaction {transaction_id} waiting to lock {destination.name}'s account")
            with destination.lock:
                print(f"Transaction {transaction_id} locked {destination.name}'s account")
                self.balance -= amount
                destination.balance += amount
            print(f"Transaction {transaction_id} released {destination.name}'s account")

        print(f"Transaction {transaction_id} released {self.name}'s account")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# <<< DO NOT EDIT ANY CODE BELOW THIS LINE >>>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create three accounts
account_1 = Account('Ethel', 600)
account_2 = Account('Fred', 450)
account_3 = Account('Greta', 500)

# And a set of transactions that will be processed
transactions = [
    (account_1, account_2, 30, '1'),
    (account_1, account_3, 37, '2'),
    (account_2, account_3, 50, '3'),
    (account_2, account_3, 39, '4'),
    (account_3, account_1, 25, '5'),
]

# Create a thread to process each transaction
threads = [
    threading.Thread(
        target=source.transfer_to,
        args=(destination, amount, transaction_id)
    )
    for source, destination, amount, transaction_id in transactions
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for account in [account_1, account_2, account_3]:
    print(f"{account.name} has a final balance of {account.balance}")




"""HINTS TO SOLVE THE DEADLOCK

Option 1: Always acquire the locks in the same order:

  * Sort the accounts by their internal id (you can use `id(variable)`
    to get this), which is unique for each object in Python.
  * Acquire the lock for the account with the lowest id first


Option 2: Timeout if the lock cannot be obtained after a brief wait:
          (this option is harder!!)

  The `acquire()` method takes an optional `timeout` argument.
  `lock.acquire(timeout=0.1)` will return `True` if the lock has been acquired
  and `False` after 0.1s if the lock cannot be acquired.

  * Use a timeout when you try to acquire a lock (e.g. 0.1 seconds)
  * If a lock can't be acquired, release any locks you've already acquired
  * Retry after a brief wait
"""
