# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
from math import sqrt
number = 600851475143
for i in range(round(sqrt(number)), 0, -1):
    if number % i == 0:
        #print(i)
        counter = 0
        for k in range(i, 0, -1):
            if i % k == 0:
                counter += 1
        #print(counter)
        if counter == 2:
            print('{}{}{}{}'.format("Max Prime factor of ", number, " is ", i))
            break



#No need to loop through all divisors
# Start reverse and find the first divisor which is a prime factor -> it will be the largest.
#Still to slow, there must be a way to reduce the scope
#-> sqrt to reduce scope bc divisors exist in pairs.