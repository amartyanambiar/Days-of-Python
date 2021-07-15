num = int(input("Number: "))
exp = int(input("Power: "))
result = 1
if(exp==0):
    result = 1

while(exp > 0):
    result = result * num
    exp = exp-1

print(result)