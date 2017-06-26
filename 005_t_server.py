import requests
import time
from threading import Thread


def fetch(pid):
    response = requests.get('http://localhost:8080')
    result = response.json()
    name = result['name']
    consulted_at = result['consulted_at']

    print('Process %s: %s, %s' % (pid, name, consulted_at))
    return result


def asynchronous():
    threads = []
    for i in range(1, 10):
        t = Thread(target=fetch, args=(i,))
        t.start()
        threads.append(t)
    [thread.join() for thread in threads]


print('Asynchronous:')
start = time.time()
asynchronous()
print(time.time() - start)
