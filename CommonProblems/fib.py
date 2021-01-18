def cache_it(func):
    d = {}
    def wrapper(num):
        if num in d:
            return d[num]
        else:
            res = func(num)
            d[num] = res
            return res
    return wrapper


@cache_it
def fib(num):
    if num in [0, 1]:
        return num

    return fib(num-1) + fib(num-2)


for i in range(1, 10000):
    print(i, ': ', fib(i))
