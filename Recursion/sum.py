
def sumN(n):
    if(n == 0):
        return 0
    
    ans = n + sumN(n-1)
    return ans


if __name__ == '__main__':
    y = int(input("N = "))
    print(sumN(y))

