def step(x):
    if x % 2 == 0:
        return  x / 2
    else:
        return 3 * x + 1

def chain_number(x):
    chainNumber = 1
    while chainNumber > 0:
        x = step(x)
        chainNumber += 1
        if x == 1:
            return chainNumber

max_steps = 0
champ_number = 0

for number in range(1,1000001):
    temp = chain_number(number)
    if temp > max_steps:
        max_steps = temp
        champ_number = number
        
print(max_steps)
print(champ_number)