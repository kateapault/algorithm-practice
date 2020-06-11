# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
import math
# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?

# 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 => 3628800
# -   -   3 * 4 * 5 * 6 * 7   -   -   -- => 2520
# so maybe highest prime #?
# idk how to find that, so let's try brute force...

def smallest_multiple(max_num):
    i = 1
    max_mult = math.factorial(max_num)
    mult = max_num
    while mult < max_mult:
        check = True
        for x in range(1,max_num+1):
            if mult % x != 0:
                check = False
        
        if check:
            print(f"{i} cycles")
            return mult
        
        i += 1
        mult += max_num
    print("Something went wrong, this took more than 10,000 cycles")

z = smallest_multiple(20)
print('')
print("ANSWER FOR 20")
print(z)