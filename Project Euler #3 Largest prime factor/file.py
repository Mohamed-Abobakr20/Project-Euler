#!/bin/python3

import sys, math

def primeFactors(n):
    arr = []  
    # Print the number of two's that divide n
    while n % 2 == 0:
        arr.append(2)
        n = n / 2
          
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):
          
        # while i divides n, print i ad divide n
        while n % i == 0:
            arr.append(i)
            n = n / i
              
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        arr.append(n)
        
    return int(arr[-1])    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primeFactors(n))
