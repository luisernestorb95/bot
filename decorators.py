import asyncio
from datetime import datetime


def async_decorator(func):
    print(func)
    def run(*args, **kwargs):
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(None, func, *args, **kwargs)

    return run

