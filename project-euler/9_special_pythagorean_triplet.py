from math import sqrt

def prod(li):
    p = 1
    for x in li:
        p *= x
    return p

def find_pythagorean_triplets_under(n):
    p = []
    for i in range(2,n):
        for j in range(2,n):
            k = sqrt(i**2+j**2)
            if int(k) == k:
                # print(f"{i}^2 + {j}^2 = {k}^2")
                p.append([i,j,k])
    return p

def find_triplets_equal_to(n):
    p = find_pythagorean_triplets_under(n-2)
    for q in p:
        print(q)
        if sum(q) == n:
            return prod(q)

print(find_triplets_equal_to(1000))