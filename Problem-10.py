import math

def prime(x):
    is_prime = True
    if x == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(x) + 1)):
            if x % i == 0:
                is_prime = False
                break
        return is_prime

sum_of_prime = 0
number = 2
while True:
    if prime(number):
        sum_of_prime += number
    if number == 2000000:
        break
    number += 1
print(sum_of_prime)