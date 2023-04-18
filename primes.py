from math import sqrt, floor

def isPrime(n: int):
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = [2]
n = 3

while len(primes) < 20:
    if isPrime(n):
        primes.append(n)
    n += 2

print(primes)
