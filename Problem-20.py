#Find the sum of the digits in the number 100!
def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact
x = factorial(100)
x = str(x)
sum = 0
for i in x:
    sum += int(i)
print(sum)