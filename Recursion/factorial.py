import sys
sys.setrecursionlimit(5000)   # ivcreases the recursive limit to 5000

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)


if __name__ == "__main__": 
    z = int(input("Number: "))
    print(fact(z))