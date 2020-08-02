import time


class time_it:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f'Running time: {end - start}s')
        return result


@time_it
def quintuple(integer):
    time.sleep(1)
    return integer * 5


rv = quintuple(12)
print(rv)
