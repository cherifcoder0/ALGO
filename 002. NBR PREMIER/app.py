def isPrime(nbr):
    if nbr<=2:
        return True
    for i in range(2,nbr):
        if nbr%i==0:
            return False
    return True

# test
# print(isPrime(3))