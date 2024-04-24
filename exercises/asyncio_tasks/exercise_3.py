import asyncio
import json
from pathlib import Path
from utils import job_funcs

DATA_PATH = Path(__file__).parent / 'data'

# pylint: disable=pointless-string-statement
"""
In this task you will implement code that runs tasks at regular intervals in the future.

Jobs are specified data/jobs.json as a python function name ("func")
    and an "interval" in seconds (delay between calls):
{
    "func": "print_date",
    "interval": 2.5
}

Jobs themselves are defined as python functions in `utils.job_funcs` (imported above).

Currently the `__main__` block parses the JSON file into a list of dicts that contain the job
    function and interval:
{
    "func": <python function>,
    "interval": <float>
}

1. `main_async` is called with a list of jobs. For each job, schedule
    `run_job` using `create_task`.

2. Implement `run_job` to run the job at the interval.

HINT 1: You can await tasks returned from `create_task`.
NOTE: This is similar to a cronjob service on UNIX/Linux.
"""

def parse_jobs_file(filename, job_funcs_dfns):
    """Parse a JSON file of jobs and return a list of dictionaries
        {
            'func': <python function>
            'interval': int
        }

    Args:
        filename (str): JSON file of job definitions
        job_funcs_dfns: A object that contains python functions.
    """
    # Read jobs file and parse to a list of dicts of
    all_jobs = []

    with open(filename) as job_file:
        try:
            # Parse JSON file
            contents = json.loads(job_file.read())

            # JSON file should be a list of jobs
            for job_definition in contents:
                all_jobs.append({
                    'func': getattr(job_funcs_dfns, job_definition['func']),
                    'interval': float(job_definition['interval'])
                })
        except Exception:
            print(f'[error] Error parsing jobs file!')

    return all_jobs


async def run_job(job, interval):
    """Runs `job` asynchronously at an `interval`.

    Args:
        job (func): A function that takes no arguments.
        interval (Numeric): Number of seconds between calls.
    """
    # YOUR CODE GOES HERE
    pass


async def main_async(jobs):
    # YOUR CODE GOES HERE
    pass


if __name__ == '__main__':
    all_jobs = parse_jobs_file(DATA_PATH / 'jobs.json', job_funcs)
    # Call main_async to schedule all jobs
    asyncio.run(main_async(all_jobs))
