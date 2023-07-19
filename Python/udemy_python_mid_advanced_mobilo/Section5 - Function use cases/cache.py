import functools
import time
NUMBER_OF_FIBONACCI_ITER = 36


@functools.lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


def old_fib(n):
    if n < 2:
        result = n
    else:
        result = old_fib(n - 1) + old_fib(n - 2)

    return result


def wrapper_time(function):
    def wrapped_function(*args, **kwargs):
        time_start = time.time()
        result = function(*args, **kwargs)
        time_end = time.time()
        print("Processing time is {}".format(time_end - time_start))
        return result

    return wrapped_function


@wrapper_time
def test_func(func):
    for a in range(0, NUMBER_OF_FIBONACCI_ITER):
        func(a)


print("Run function without results caching...")
test_func(old_fib)
print("Run function with cache of old results...")
test_func(fib)
print(fib.cache_info())
