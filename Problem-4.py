#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome_check(x):
    number = str(x)
    reversed_number = number[::-1]
    if reversed_number == number:
        return True
    else:
        return False
biggest_palindrom = 0
for i in range(100,1000):
    for j in range(100,1000):
        if palindrome_check(i*j) and i*j > biggest_palindrom:
            biggest_palindrom = i*j
print(biggest_palindrom)