def zarib3or5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False


sum = 0
for x in range(1, 1000):
    # print(x)
    if zarib3or5(x):
        sum = sum + x
        # print("sum is", sum)
print(sum)
