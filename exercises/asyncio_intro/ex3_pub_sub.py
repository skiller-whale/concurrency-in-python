import asyncio
from utils.pub_sub import PubSubServer, PubSubClient, read_stdin_and_send_messages

# pylint: disable=pointless-string-statement
"""
PUB-SUB SERVER/CLIENT
-------------

In this exercise you will implement a pub-sub server loop using
    the provided PubSubServer and PubSubClient classes.

* Create a `PubSubServer` in `main_async` and two clients. Subscribe:
    * Client 1 to `chat` and `general
    * Client 2 to `chat`

`read_stdin_and_send_messages(server: PubSubServerInterface)`
    waits for user input (stdin) and sends messages to the server.

* Use `asyncio.gather` to run `read_stdin_and_send_messages`.

* Implement `receive_and_print_messages` so that it polls 
    `server.receive_message` appropriately in a loop 
    and prints the following upon receiving a message:

    "Client <client_id> received message: <message>".

    You will need to call a method on each client to get <client_id>.

* Use `asyncio.gather` to run `receive_and_print_messages` for
    both clients.

HINT 1: You will need to use `asyncio.sleep(0)` inside the loop.
HINT 2: You will need to filter the messages received. Check
    the documentation of server.receive_message for details
    of system messages.
"""


async def receive_and_print_messages(client, server):
    # TODO: Implement receive_and_print_messages so that
    #    it continuously polls the PubSubServer and
    #    prints the messages client received.
    pass



async def main_async():
    # TODO: Implement pub-sub logic here.
    pass


if __name__ == "__main__":
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\nGoodbye!")
