import time


def wrapper_time(function):
    def wrapped_function(*args, **kwargs):
        time_start = time.time()
        result = function(*args, **kwargs)
        time_end = time.time()
        print("Processing time is {}".format(time_end - time_start))
        return result

    return wrapped_function


@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(5))

