import time


def time_it(fn):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f'Running time: {end - start}s')
        return result

    return wrapper


@time_it
def quintuple(integer):
    time.sleep(1)
    return integer * 5


rv = quintuple(12)
print(rv)
