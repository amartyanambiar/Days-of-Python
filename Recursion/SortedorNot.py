# l = [1,2,3,4]


def isSorted(l):
    x = len(l)
    if x==0 or x==1:
        return True

    if l[0]>l[1]:
        return False
    
    cutList = l[1:]
    isCutlistSorted = isSorted(cutList)
    if isCutlistSorted:
        return True
    else:
        return False

list= [1,10,6]
print(isSorted(list))


