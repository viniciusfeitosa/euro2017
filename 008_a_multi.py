import time
import asyncio
import requests
import uvloop


def fetch(pid):
    response = requests.get('http://localhost:8080')
    result = response.json()
    name = result['name']
    consulted_at = result['consulted_at']
    print('Process %s: %s, %s' % (pid, name, consulted_at))


async def asynchronous():
    loop = asyncio.get_event_loop()
    tasks = [
        loop.run_in_executor(None, fetch, i)
        for i in range(10)
    ]
    [await task for task in tasks]

print('Asynchronous:')
# loop = asyncio.get_event_loop()
loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
start = time.time()
loop.run_until_complete(asynchronous())
print(time.time() - start)
loop.close()
