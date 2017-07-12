import time
from threading import Thread


NUMBER = 34


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


t1 = Thread(target=fib, args=(NUMBER, ))
t2 = Thread(target=fib, args=(NUMBER, ))
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(end - start)
