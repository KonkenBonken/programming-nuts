from itertools import combinations


def sums(L, N):
    res = 0
    for length in range(1, len(L)+1):
        for combination in combinations(L, length):
            if sum(combination) == N:
                res += 1
    return res


assert sums([1, 6, 2, 7], 8) == 2
assert sums([12, 2, 10, 7, 3], 12) == 3
