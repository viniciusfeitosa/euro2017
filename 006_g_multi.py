import requests
import time
import gevent.monkey
gevent.monkey.patch_socket()


def fetch(pid):
    response = requests.get('http://localhost:5001')
    result = response.json()
    name = result['Name']
    consulted_at = result['ConsultedAt']

    print('Process %s: %s, %s' % (pid, name, consulted_at))


def asynchronous():
    threads = []
    for i in range(1, 11):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


print('Asynchronous:')
start = time.time()
asynchronous()
print(time.time() - start)
