import time
from threading import Thread

COUNT = 50000000


def worker(id, n):
    print('starting id:', id)
    while(n > 0):
        n -= 1
    print('finished id:', id)


if __name__ == '__main__':
    t1 = Thread(target=worker, args=(1, COUNT // 2))
    t2 = Thread(target=worker, args=(2, COUNT // 2))
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(time.time() - start)
