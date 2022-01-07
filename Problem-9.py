for a in range(1,1000):
    for b in range(1,1000-a):
        c = 1000 - a - b
        if a<b<c and (c*c) == (a*a) + (b*b):
           print(a)
           print(b)
           print(c)
           print(a*b*c)

