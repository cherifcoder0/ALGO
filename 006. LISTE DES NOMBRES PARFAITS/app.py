def isPerfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True
    else:
        return False
    
print(isPerfect(28))

def isPerfectList(inf, sup):
    list=[]
    for i in range(inf, sup):
        if isPerfect(i):
            list.append(i)
    return list

print(isPerfectList(1, 100000))