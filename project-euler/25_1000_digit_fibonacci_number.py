def fib_dig(n):
    a = 1
    b = 1
    i = 3
    while a + b < 10**(n-1):
        a,b = b,a+b
        i += 1
    return i
    
print(fib_dig(1000))