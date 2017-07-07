import asyncio
import time
import uvloop

from concurrent.futures import ProcessPoolExecutor

COUNT = 50000000


def worker(id, n):
    print('starting id:', id)
    while(n > 0):
        n -= 1
    print('finished id:', id)


async def asynchronous(loop):
    tasks = [
        loop.run_in_executor(None, worker, i, COUNT // 2)
        for i in range(2)
    ]
    [await task for task in tasks]


print('Asynchronous:')
loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
# loop = asyncio.get_event_loop()
loop.set_default_executor(ProcessPoolExecutor())
start = time.time()
loop.run_until_complete(asynchronous(loop))
print(time.time() - start)
loop.close()
