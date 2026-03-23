def getPrimeDividers(n):
    list=[]
    for i in range(1,n+1):
        if n%i==0:
           if isPrime(i):
               list.append(i)
    return list


def isPrime(nbr):
    if nbr<2:
        return False
    if nbr==2:
        return True
    for i in range(2,int(nbr**0.5)+1):
        if nbr%i==0: 
            return False
    return True

print(getPrimeDividers(100))