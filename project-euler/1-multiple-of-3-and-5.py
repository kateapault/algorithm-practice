# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_x(max_num,x):
    max_num_inclusive = max_num - 1
    max_multiple = max_num_inclusive - (max_num_inclusive % x)
    max_factor = max_multiple / x
    
    sum_factors = max_factor * (1 + max_factor) / 2
    return(sum_factors*x)

def multiples_of_3_or_5(max_num):
    # sum_tot = sum_5s + sum_3s - sum_15s (<- to eliminate doubles)
    sum_5s = multiples_of_x(max_num,5)
    sum_3s = multiples_of_x(max_num,3)
    sum_15s = multiples_of_x(max_num,15)
    
    return(sum_3s + sum_5s - sum_15s)

print(multiples_of_3_or_5(1000))