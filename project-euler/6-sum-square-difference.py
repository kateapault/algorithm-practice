# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2=55^2=3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

def sum_of_squares_to_n(n):
    return(n*(n+1)*(2*n+1) / 6)

def sum_to_n(n):
    return(n*(n+1)/2)

def sum_square_difference(n):
    sum_squares = sum_of_squares_to_n(n)
    square_sum = sum_to_n(n)**2
    return(square_sum - sum_squares)

print(sum_square_difference(100))