import requests
import time


def fetch(pid):
    response = requests.get('http://localhost:8080')
    result = response.json()
    name = result['name']
    consulted_at = result['consulted_at']

    print('Process %s: %s, %s' % (pid, name, consulted_at))
    return result


def synchronous():
    for i in range(1, 10):
        fetch(i)


print('Synchronous:')
start = time.time()
synchronous()
print(time.time() - start)
