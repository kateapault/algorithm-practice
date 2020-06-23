# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import datetime

def getfactors(n):
    w = datetime.datetime.now()
    f = {}
    for m in range(2,n//2):
        if n % m == 0:
            f[m] = True
        if m == 1000000:
            print("1M")
            print(f"{datetime.datetime.now() - w}")
        elif m == 5000000:
            print("5M")
            print(f"{datetime.datetime.now() - w}")
        elif m == 10000000:
            print("ten million")
            print(f"{datetime.datetime.now() - w}")
        elif m == 100000000:
            print("100M")
            print(f"{datetime.datetime.now() - w}")
        if m % 1000000000 == 0:
            print(f"{m}")
            print(f"{datetime.datetime.now() - w}")
            print(f"{f}")
    return f

def isprime(n):
    if n > 2:
        for m in range(2,n//2+1):
            if n % m == 0:
                return False
        return True
    else:
        return True

def largest_prime_factor(n):
    f = getfactors(n)
    print(f"factors: {f}")
    p = []
    for x in f:
        if isprime(x):
            p.append(x)
    print(f"prime factors: {p}")
    return max(p)

print(largest_prime_factor(600851475143))