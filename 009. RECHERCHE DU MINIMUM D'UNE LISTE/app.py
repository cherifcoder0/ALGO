def minOfList(list):
    min=list[0]
    for i in range(1, len(list)):
        print(f"{i}==> {list[i]}")
        if min>list[i]:
            min=list[i]
    return min
print(minOfList([2,34,0,4,5]))
