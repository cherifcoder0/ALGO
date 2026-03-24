def isPower(a,b):
    if a*a==b:
        return f" {a} au carre fait  {b}"
    elif b*b==a:
        return f" {b}  au carre fait  {a} "
    else:
        return f" {a} et {b}  ne sont pas puissance l'un de l'autre "
    


def isPowerof(a,b):
    if a<b:
        for i in range(1,b):
            if a**i==b:
                return f"{b} est une puissance de {a}"
        return False
    for i in range(1,a):
        if b**i==a:
            return f"{a} est une puissance de {b}"
    return False
print(isPowerof(25,5))