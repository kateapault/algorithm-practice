from datetime import datetime as dt

def find_x_prime(n):
    st = dt.now()
    i = 2
    x = 5
    while i < n and x < 1000000000000:
        prime = True
        for y in range(3,x//3,2):
            if x % y == 0:
                prime = False
        if prime:
            i += 1
            if x == 5:
                print(f'5 is the {i}rd prime')
        x += 2
        if x == 10001:
            print('x is 10k')
            print(f"{(dt.now() - st).seconds/100} ms")
            print(f"found {i} primes")
        elif x == 20001:
            print('x is 20k')
            print(f"{(dt.now() - st).seconds/100} ms")
            print(f"found {i} primes")
        elif x == 40001:
            print('x is 40k')
            print(f"{(dt.now() - st).seconds/100} ms")
            print(f"found {i} primes")
        elif x == 60001:
            print('x is 60k')
            print(f"{(dt.now() - st).seconds/100} ms")
            print(f"found {i} primes")
        elif x == 80001:
            print('x is 80k')
            print(f"{(dt.now() - st).seconds/100} ms")
            print(f"found {i} primes")
        elif x == 100001:
            print('x is 100k')
            print(f"{(dt.now() - st).seconds/100} ms")
            print(f"found {i} primes")
        elif x == 120001:
            print('x is 120k')
            print(f"{(dt.now() - st).seconds/100} ms")
            print(f"found {i} primes")
        elif x == 140001:
            print('x is 140k')
            print(f"{(dt.now() - st).seconds/100} ms")
            print(f"found {i} primes")

    print(f"prime number {i} found!")
    return x

print(find_x_prime(10001))