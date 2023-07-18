def IsEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


Number1 = 1
Number2 = 2
sum = 0
while (Number1 < 4000000):
    # 3
    Number3 = Number1+Number2
    # Number1 = temp
    # temp = Number2
    Number1 = Number2
    Number2 = Number3
    # print(Number1)
    if IsEven(Number1):
        sum = sum+Number1
print("sum is:", sum)
