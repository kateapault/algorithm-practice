def nth_fib(x):
    if x > 3:
        return nth_fib(x-1) + nth_fib(x-2)
    elif x == 3:
        return 2
    elif x == 2 or x == 1:
        return 1
    else:
        return f"Unknown entry {x}"

print(nth_fib(10))