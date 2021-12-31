# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import functools

def topla(a, b):
    return a+b
square_result_numbers = 0
for i in range(1, 101):
    i = i*i
    square_numbers = [i]
    for j in square_numbers:
        square_result_numbers += j

list1 = range(1, 101)
result_sum = functools.reduce(topla, list1)
square_result_sum = result_sum * result_sum

print(square_result_sum - square_result_numbers)

'''
sum = 0
sum_square = 0
for i in range(1,101):
    sum += i
    sum_square += i*i
result = (sum*sum) - sum_square
print(result)
'''