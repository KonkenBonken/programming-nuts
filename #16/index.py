N, K, r = int(input("N:")), int(input("K:")), 1

for i in range(N, 1, -K):
    r *= i

print(str(N) + '!'*K, '=', r)


# Shorter version
from math import prod
print(prod(range(int(input('N')), 1, -int(input('K')))))
