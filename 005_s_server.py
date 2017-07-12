import requests
import time


def fetch(pid):
    response = requests.get('http://localhost:5001')
    result = response.json()
    name = result['Name']
    consulted_at = result['ConsultedAt']

    print('Process %s: %s, %s' % (pid, name, consulted_at))


def synchronous():
    for i in range(1, 11):
        fetch(i)


print('Synchronous:')
start = time.time()
synchronous()
print(time.time() - start)
