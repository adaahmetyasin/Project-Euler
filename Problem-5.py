#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import functools

# gcd fonksiyonu ebob hesaplar
#ebob(x,y)*ekok(x,y)=x*y

def gcd(x,y):
    return math.gcd(x,y)

# '/' işareti ile bölme yapınca float değer verir. '//' işareti ile bölme yapınca tam degeri alır.

def ekok(x,y):
    return (x*y) // gcd(x,y)

liste = range(1,21)

result = functools.reduce(ekok,liste)

print(result)