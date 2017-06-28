import time

COUNT = 50000000


def worker(id, n):
    print('starting id:', id)
    while(n > 0):
        n -= 1
    print('finished id:', id)


if __name__ == '__main__':
    start = time.time()
    worker(1, COUNT)
    print(time.time() - start)
