import asyncio
from pathlib import Path
from utils.job_server_base import JobServerBase
from utils import job_funcs
import importlib
import inspect

DATA_PATH = Path(__file__).parent / 'data'

# pylint: disable=pointless-string-statement, bare-except
"""
In this exercise you will implement live reloading of jobs.
    You will extend the JobServerBase class to do so.

The JobServerBase class will watch for file changes to data/jobs.json
    and call `cancel_all_running_jobs` followed by `create_job` for
    each job in the file.

1. Create an instance attribute (a set) that stores a reference
    to all running jobs (asyncio.Task).

2. Implement the method `cancel_all_running_jobs` so that it
    cancels all running jobs (asyncio.Task).

3. Run the script and you should see the jobs running.

4. Now change the duration of `print_date` to 1000 seconds (a long interval)
    in data/jobs.json What do you notice? Can you fix the problem?

5. Add a print statement that prints when a job is cancelled.
    f"[info] Job {job.__name__} cancelled."

6. Start the script, then add a new job to `job_funcs.py`.
    Make sure it's live-reloaded and running.

HINT 1: You might want to override the `__init__` method to initalize
    the set of all running `asyncio.Task`s.

HINT 2: Is the try-except block in _run_job appropriate?
    `asyncio.CancelledError` is a subclass of `BaseException`,
    so you can still catch `Exception` without catching it.

HINT 3: You can use `func.__name__` to access a function's name.
HINT 4: Use your imagination -- you can add any job to job_funcs.py!

[OPTIONAL]
7. Using `inspect.iscoroutinefunction(<function>)` you can check
    whether a function is a coroutine.

    Use it to enable the definition of `async` jobs in `job_funcs.py`.

8. Make `print_unix_time` a coroutine and ensure it still works.
"""

class JobServer(JobServerBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # YOUR CODE GOES HERE
    @staticmethod
    async def _run_job(job, interval):
        while True:
            try:
                job()
                await asyncio.sleep(interval)
            except:
                print(f'[error] Job {job.__name__} stopped due to an error!')
                break

    def create_job(self, job_name, job_interval):
        # reload the files in jobs
        #   this lets you create jobs while the server is running
        importlib.reload(job_funcs)
        if not hasattr(job_funcs, job_name):
            print(f'No such job {job_name}')
            return

        job_function = getattr(job_funcs, job_name)

        # YOUR CODE GOES HERE
        ...

    # YOUR CODE GOES HERE
    def cancel_all_running_jobs(self):
        pass


if __name__ == '__main__':
    server = JobServer(DATA_PATH / 'jobs.json')

    asyncio.run(server.run())
