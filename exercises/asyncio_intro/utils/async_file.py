import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

class AsyncFile():
    """Asynchronous File Reader that uses ThreadPoolExecutor.
        Can be used both as a context manager and iterator.

        NOTE: This object is NOT thread-safe.
    """
    executor = None

    @classmethod
    def init_executor(cls):
        """Initializes the ThreadPoolExecutor (shared between instances).
        """
        if cls.executor is None:
            cls.executor = ThreadPoolExecutor(max_workers=1)

    def __init__(self, filename):
        self.loop = asyncio.get_running_loop()
        self.filename = filename
        self.file = None

        # ensure executor is running
        self.init_executor()

    def _open_sync(self):
        time.sleep(0.1)
        self.file = open(self.filename, "r+")

    def _close_sync(self):
        time.sleep(0.1)

        if self.file:
            self.file.close()
        return True

    def _readline(self):
        time.sleep(0.1)
        if self.file is None:
            raise ValueError("No file open")

        return self.file.readline()

    async def __aenter__(self):
        """Async file context manager.

        Returns:
            AsyncFile: Returns self, can be iterated over like a file object.
        """
        await self.loop.run_in_executor(
            self.executor, self._open_sync
        )
        return self

    async def readline(self):
        """Reads a line from the file (if its already open).
            Advances the read position.

        Returns:
            str: Next line in file.
        """
        return await self.loop.run_in_executor(
            self.executor, self._readline
        )

    async def __aexit__(self, type, val, traceback):
        return await self.loop.run_in_executor(
            self.executor, self._close_sync
        )

    def __aiter__(self):
        return self

    async def __anext__(self):
        line = await self.readline()
        if line:
            return line

        raise StopAsyncIteration

async def aenumerate(async_collection):
    """Asynchronous version of enumerate

    Args:
        async_collection (collection): An asynchronous collection.

    Yields:
        (idx, el): The index (idx) and corresponding collection element (el).
    """
    idx = 0
    async for el in async_collection:
        yield idx, el
        idx += 1

async def read_and_print_file_async(filename):
    """Read and print a file line by line (asynchronous).

    Args:
        filename (str): The file name.

    Returns:
        num_lines (int): The number of lines read
    """
    num_lines = 0
    async with AsyncFile(filename) as file:
        async for idx, line in aenumerate(file):
            num_lines = idx
            if not line:
                break
            print(f"Line {idx}: {line.strip()}")
    return num_lines

def read_and_print_file_sync(filename):
    """Read and print a file line by line (synchronous).

    Args:
        filename (str): The file name.

    Returns:
        num_lines (int): The number of lines read
    """
    num_lines = 0
    with open(filename, "r+") as file:
        time.sleep(0.1)
        for idx, line in enumerate(file):
            time.sleep(0.1)
            num_lines = idx
            if not line:
                break
            print(f"Line {idx}: {line.strip()}")

        time.sleep(0.1)

    return num_lines
