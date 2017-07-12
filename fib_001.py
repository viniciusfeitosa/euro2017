import time

NUMBER = 34


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


start = time.time()
fib(NUMBER)
fib(NUMBER)
end = time.time()
print(end - start)
