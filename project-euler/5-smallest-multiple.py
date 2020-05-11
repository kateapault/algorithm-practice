# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?

# 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 => 3628800
# -   -   3 * 4 * 5 * 6 * 7   -   -   -- => 2520
# so maybe highest prime #?
# idk how to find that, so let's try brute force...

def smallest_multiple(max_num)
    