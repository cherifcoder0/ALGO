def maxList(list):
    max=list[0]
    for i in range(1, len(list)):
        if max<list[i]:
            max=list[i]
    return max

# print(maxList([12,56,87,1,273]))
        