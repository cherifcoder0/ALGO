def getDividers(n):
    dividersList=[]
    for i in range(1,n+1):
        if n%i==0:
            dividersList.append(i)
    return dividersList

#.................... test................
# print(getDividers(25))