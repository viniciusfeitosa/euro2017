import time
import asyncio
import aiohttp
import uvloop


async def fetch(pid):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8080') as resp:
            result = await resp.json()
            name = result['name']
            consulted_at = result['consulted_at']
            print('Process %s: %s, %s' % (pid, name, consulted_at))


async def asynchronous():
    tasks = [
        asyncio.ensure_future(fetch(i))
        for i in range(10)
    ]
    await asyncio.wait(tasks)

print('Asynchronous:')
ioloop = uvloop.new_event_loop()
asyncio.set_event_loop(ioloop)
start = time.time()
ioloop.run_until_complete(asynchronous())
print(time.time() - start)
ioloop.close()
