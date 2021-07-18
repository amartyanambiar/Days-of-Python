def Sum(n):
    if n==0:
        return 0
    
    ans = n + Sum(n-1)
    return ans


if __name__ == '__main__':
    y = int(input("N = "))
    print(Sum(y))

