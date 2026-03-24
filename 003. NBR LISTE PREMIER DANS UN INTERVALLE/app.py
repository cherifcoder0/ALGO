def isPrime(nbr):
    if nbr<2:
        return False
    if nbr==2:
        return True
    for i in range(2,nbr):
        if nbr%i==0:
            return False
    return True

def getPrimeList(inf, sup):
    primeList=[]
    for i in range(inf, sup+1):
        if isPrime(i):
            primeList.append(i)
    return primeList

# test
# print(getPrimeList(1,100))