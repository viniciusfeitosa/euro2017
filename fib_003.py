import time
from multiprocessing import Process


NUMBER = 34


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


p1 = Process(target=fib, args=(NUMBER, ))
p2 = Process(target=fib, args=(NUMBER, ))
start = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
end = time.time()
print(end - start)
