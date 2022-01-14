#What is the sum of the digits of the number 2^1000?

import math

number = str(pow(2,1000))
sumOfDigits= 0
for i in number:
    sumOfDigits += int(i)
print(sumOfDigits)