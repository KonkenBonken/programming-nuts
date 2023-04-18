def max(fn):
    x = -1e15
    last = fn(x)
    step = 1e15
    while abs(step) > 1e-15:
        while True:
            x += step
            y = fn(x)
            if y < last:
                break
            last = y
        last = y
        step /= -10
    return round(x, 4)


assert max(lambda x: -x**2) == 0
assert max(lambda x: -28 * x**2 + 42*x) == .75
