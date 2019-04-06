# Even Fibonacci numbers
# Problem 2
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
old_number = 0
last_number = 1
new_number = 0
sum_of_even = 0
while new_number < 4000000:
    new_number = old_number + last_number
    old_number = last_number
    last_number = new_number
    if new_number % 2 == 0:
        sum_of_even += new_number


print(sum_of_even)
