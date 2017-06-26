import asyncio
import requests


async def main():
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future2 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future3 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future4 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future5 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future6 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future7 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future8 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future9 = loop.run_in_executor(None, requests.get, 'http://localhost:8080')
    future10 = loop.run_in_executor(
        None, requests.get, 'http://localhost:8080')
    response1 = await future1
    response2 = await future2
    response3 = await future3
    response4 = await future4
    response5 = await future5
    response6 = await future6
    response7 = await future7
    response8 = await future8
    response9 = await future9
    response10 = await future10
    print(response1.text)
    print(response2.text)
    print(response3.text)
    print(response4.text)
    print(response5.text)
    print(response6.text)
    print(response7.text)
    print(response8.text)
    print(response9.text)
    print(response10.text)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
