# Largest palindrome product

# Problem 4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# possibility 1
# max 3 digits * 3 digits numbers
# nested loops & iterate until you find a palindrome..
# = BAD


# possibility 2
# iterate backword from largest number (product of 999*999) and find dividers

# Rappel: primary factor decomposition?

# Scoping
import numpy as np
import time


def solve(candidates, div):
    pal=[]
    div_inner = div.copy()
    for i in div:
        for k in div_inner:
            if i*k in candidates:
                pal.append(i*k)
                div_inner = div_inner[div_inner > k] # would result in lower palindrome anyway
                break  # no need to continue iterating
    return pal

start = time.time()
cand = np.array([number for number in range(997799, 10001, -1) if str(number) == str(number)[::-1]])
div = np.arange(999, 100, -1)

a = solve(cand, div)

print(max(a), "time running", time.time()-start)



