def max(fn):
    x = -1e15
    y = fn(x)
    step = 1e15
    for _ in range(15):
        while fn(x+step) > y:
            x += step
            y = fn(x)
        x += step
        y = fn(x)
        step /= 10
        while fn(x-step) > y:
            x -= step
            y = fn(x)
        x -= step
        y = fn(x)
        step /= 10
    return round(x, 4)


assert max(lambda x: -x**2) == 0
assert max(lambda x: -28 * x**2 + 42*x) == .75
