N, K, r = int(input("N:")), int(input("K:")), 1

for i in range(N, 1, -K):
    r *= i

print(str(N) + '!'*K, '=', r)
