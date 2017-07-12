import time
import asyncio
import aiohttp
# import uvloop


async def fetch(pid):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:5001') as resp:
            result = await resp.json()
            name = result['Name']
            consulted_at = result['ConsultedAt']
            print('Process %s: %s, %s' % (pid, name, consulted_at))


async def asynchronous():
    tasks = [
        fetch(i)
        for i in range(1, 11)
    ]
    await asyncio.gather(*tasks)

print('Asynchronous:')
# ioloop = uvloop.new_event_loop()
# asyncio.set_event_loop(ioloop)
ioloop = asyncio.get_event_loop()
start = time.time()
ioloop.run_until_complete(asynchronous())
print(time.time() - start)
ioloop.close()
