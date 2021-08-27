def merge_sort(l):
    h=len(l)
    if h == 1 or h == 0 : 
        return 
    mid = h//2
    l1 = l[:mid]
    l2 = l[mid:]

    merge_sort(l1)
    merge_sort(l2)
    merge(l1,l2,l)
    return l
    

def merge(l1,l2,l):
    i=0
    j=0
    k=0
    while i<len(l1) and j<len(l2):
        if (l1[i] < l2[j]):
            l[k] = l1[i]
            k = k + 1
            i = i + 1
        else:
            l[k] = l2[j]
            k = k + 1
            j = j + 1
    
    while i<len(l1):
        l[k] = l1[i]
        k = k + 1
        i = i + 1

    while j<len(l2):
        l[k] = l2[j]
        k = k + 1
        j = j + 1


print(merge_sort([1,65,21,34]))
