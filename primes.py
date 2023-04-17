def isPrime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


primes = []
n = 2

while len(primes) < 20:
    if isPrime(n):
        primes.append(n)
    n += 1

print(primes)
