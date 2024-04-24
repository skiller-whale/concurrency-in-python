import asyncio
import sys
import abc


async def get_stream_reader(pipe) -> asyncio.StreamReader:
    """Returns a stream reader from the given pipe.

    Args:
        pipe: A pipe object, e.g. sys.stdin.

    Returns:
        asyncio.StreamReader: A stream reader connected to the pipe.
    """
    loop = asyncio.get_event_loop()
    reader = asyncio.StreamReader(loop=loop)
    protocol = asyncio.StreamReaderProtocol(reader)
    await loop.connect_read_pipe(lambda: protocol, pipe)
    return reader


class PubSubClientInterface(abc.ABC):
    """A PubSubClient Interface. The client should provide
        a unique ID to subscribe to a channel.
    """
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_id(self) -> int:
        """Returns a unique client ID

        Returns:
            id: A unique integer identifier.
        """


class PubSubServerInterface(abc.ABC):
    @abc.abstractmethod
    async def subscribe(self, client: PubSubClientInterface, channel: str) -> bool:
        """Subscribe a client to a  channel.
            Relies on client.get_id() returning a unique integer ID.

        Args:
            client (PubSubClientInterface): The client to subscribe.
            channel (str): The channel to subscribe to.

        Returns:
            bool: True if successful, False otherwise
        """

        
    @abc.abstractmethod
    async def unsubscribe(self, client: PubSubClientInterface, channel: str) -> bool:
        """Unsubscribe a client from a  channel.
            Relies on client.get_id() returning a unique integer ID.

        Args:
            client (PubSubClientInterface): The client to unsubscribe.
            channel (str): The channel to unsubscribe from.

        Returns:
            bool: True if successful, False otherwise
        """

    @abc.abstractmethod
    async def publish(self, channel: str, message: str) -> int:
        """Publish a message to a channel.

        Args:
            channel (str): The channel to publish a message to.
            message (str): The message.

        Returns:
            int: The number of clients the message was sent to.
        """

    @abc.abstractmethod
    async def receive_message(self, client: PubSubClientInterface) -> str:
        """Checks channels that the client is subscribed
            to and return the oldest unread message (and marks it as read).

        Args:
            client (PubSubClientInterface): The client

        Returns:
            str: The oldest undread message. Returns an _empty string_ 
                if there are no unread messages.
        """

    @abc.abstractmethod
    def get_created_channels(self) -> set:
        """Returns the set of created channels.

        Returns:
            set: Created channels.
        """


class PubSubClient(PubSubClientInterface):
    client_ids = set()

    def __init__(self):
        self._id = self._get_client_id()

    @classmethod
    def _get_client_id(cls):
        client_id = 1 + max(cls.client_ids, default=0)
        cls.client_ids.add(client_id)
        return client_id

    def get_id(self):
        return self._id


class PubSubServer(PubSubServerInterface):
    """A publish-subscribe Server implemented using asyncio.
    """
    def __init__(self):
        self._channels = dict()
        self._messages = dict()

    def get_created_channels(self):
        return self._channels.keys()

    async def subscribe(self, client, channel):
        # simulate real-world servers
        await asyncio.sleep(0.05)
        client_id = client.get_id()
        if channel in self._channels:
            self._channels[channel].add(client_id)
        else:
            self._channels[channel] = {client_id}

        if client_id not in self._messages:
            self._messages[client_id] = []
        return True

    async def publish(self, channel, message):
        if channel not in self._channels:
            return

        sent = 0
        for client_id in self._channels[channel]:
            self._messages[client_id].append(message)
            # this is incremented here as clients
            #   can subscribe during the sending of
            #   the message
            sent += 1
            await asyncio.sleep(0)

        return sent

    async def receive_message(self, client):
        client_id = client.get_id()
        if client_id not in self._messages:
            return ""

        if len(self._messages[client_id]) == 0:
            return ""

        await asyncio.sleep(0.05)
        last_message = self._messages[client_id].pop(0)
        return last_message

    async def unsubscribe(self, client, channel):
        await asyncio.sleep(0.05)
        client_id = client.get_id()
        if channel in self._channels:
            self._channels[channel].discard(client_id)

            if client_id in self._messages:
                del self._messages[client_id]
        return True


async def read_stdin_and_send_messages(server: PubSubServerInterface):
    """Send message to the specified PubSubServer.

    Args:
        server (PubSubServerInterface): A Pub-Sub server
            that implements PubSubServerInterface.
    """
    while True:
        print("Type in your message [channel: message]!")
        print(">>> ", end="", flush=True)

        reader = await get_stream_reader(sys.stdin)
        data = await reader.readline()
        msg = data.decode().split(":")
        if len(msg) < 2:
            channels = list(server.get_created_channels())
            print(f"No channel specified, available channels: [{' | '.join(channels)}]")
        else:
            await server.publish(msg[0], msg[1].strip())

        await asyncio.sleep(0.5)
