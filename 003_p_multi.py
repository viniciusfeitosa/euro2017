import time
from multiprocessing import Process

COUNT = 50000000


def worker(id, n):
    print('starting id:', id)
    while(n > 0):
        n -= 1
    print('finished id:', id)


if __name__ == '__main__':
    p1 = Process(target=worker, args=(1, COUNT // 2))
    p2 = Process(target=worker, args=(2, COUNT // 2))
    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(time.time() - start)
