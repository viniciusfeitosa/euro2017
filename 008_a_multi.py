import time
import asyncio
import requests
# import uvloop


def fetch(pid):
    response = requests.get('http://localhost:5001')
    result = response.json()
    name = result['Name']
    consulted_at = result['ConsultedAt']
    print('Process %s: %s, %s' % (pid, name, consulted_at))


async def asynchronous(loop):
    tasks = [
        loop.run_in_executor(None, fetch, i)
        for i in range(1, 11)
    ]
    [await task for task in tasks]

print('Asynchronous:')
# loop = uvloop.new_event_loop()
# asyncio.set_event_loop(loop)
loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(asynchronous(loop))
print(time.time() - start)
loop.close()
