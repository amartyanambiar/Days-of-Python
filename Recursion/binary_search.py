def bin_search(a,x,low,high):
    if(high<low):
        return -1

    mid = (low+high)//2

    if(a[mid] == x):
        return mid

    elif(a[mid]<x):
        return bin_search(a,x,mid+1,high)

    elif(a[mid]>x):
        return bin_search(a,x,low,mid-1)
        
print(bin_search([1,2,3,4],3,1,4))
    