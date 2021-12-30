#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
numbers1 = 0
for i in range(0,1000,3):
    numbers1 = i + numbers1

numbers2 = 0
for i in range(0,1000,5):
    numbers2 = i + numbers2

print(numbers1 + numbers2)