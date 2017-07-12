import time
import asyncio
from concurrent.futures import ProcessPoolExecutor


NUMBER = 34


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


async def asynchronous(loop):
    tasks = [
        loop.run_in_executor(None, fib, NUMBER),
        loop.run_in_executor(None, fib, NUMBER),
    ]
    [await task for task in tasks]


loop = asyncio.get_event_loop()
loop.set_default_executor(ProcessPoolExecutor())
start = time.time()
loop.run_until_complete(asynchronous(loop))
end = time.time()
print(end - start)
loop.close()
