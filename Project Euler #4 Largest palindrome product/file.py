#!/bin/python3
import sys

def larrgestPalindrome(n):
  
    max_product = 0 # Initialize result
    for i in range(999,99, -1):
     
        for j in range(i,99,-1):
         
            # calculating product of
            # two n-digit numbers
            product = i * j
                
            if (product < max_product):
                break
            number = product
            reverse = 0
  
            # calculating reverse of
            # product to check
            # whether it is palindrome or not
            if(product < n):
                while (number != 0):
                
                    reverse = reverse * 10 + number % 10
                    number =number // 10
                
    
                # update new product if exist and if
                # greater than previous one
                if (product == reverse and product > max_product):
                    max_product = product
         
     
    return max_product

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(larrgestPalindrome(n))
