# formula = n! /(k! * (n-k)!)
def faktoriyel(x):
    fakt = 1
    while x > 1:
        fakt = x * fakt
        x -= 1
    return fakt

def kombinasyon(n, k):
    return faktoriyel(n) / (faktoriyel(k) * faktoriyel(n-k))

print(kombinasyon(40,20))
