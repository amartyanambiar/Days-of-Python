def asc_print(n):
    if(n==0):
        return
    
    asc_print(n-1)
    print(n)
    

def desc_print(n):
    if(n==0):
        return
    
    print(n)
    desc_print(n-1)
   
    

if __name__ == "__main__":
    n = int(input("Enter number: "))
    i = int(input("Enter Your Choice \n 1. Ascending Order \n 2. Descending Order"))
    
    if(i==1):
        asc_print(n)
    elif(i==0):
        desc_print(n)
    else:
        print("Invalid")
        exit