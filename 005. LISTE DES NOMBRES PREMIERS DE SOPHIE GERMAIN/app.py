def isPrime(nbr):
    if nbr<2:
        return True
    for i in range(2,nbr):
        if nbr%i==0:
            return False
    return True
        
        
def isSophieGermainPrime(n):
    if isPrime(n):
        j=n*2+1
        return isPrime(j)
    
print(isSophieGermainPrime(7))

def isSophieGermainPrimeList(inf, sup):
    list=[]
    for i in range(inf, sup+1):
        if isSophieGermainPrime(i):
            list.append(i)
    return list

print(isSophieGermainPrimeList(1, 1000))