import math

prime_count = 0

def check_prime(x):
    isPrime = True
    if x == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                isPrime = False
                break
        return isPrime

i = 2
while True:
    if check_prime(i):
        prime_count += 1
    if prime_count == 10001:
        print(i)
        break
    i += 1
