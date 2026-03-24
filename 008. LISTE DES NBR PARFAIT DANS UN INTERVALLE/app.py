def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def isPerfect(n):
    if isPrime(n):
        if isPrime(n*2+1):
            return True
    return False

def isPerfectList(n,m):
    list=[]
    for i in range(n, m):
       if isPerfect(i):
           list.append(i)
    return list
print(isPrime(7))
print(isPerfect(7))
print(isPerfectList(1,100))