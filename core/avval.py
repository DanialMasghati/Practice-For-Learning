def is_prime(n):
    avval = True
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            avval = False
    return avval


prime_count = 0

for i in range(2, 100):
    if is_prime(i):
        print(i)
        prime_count += 1
print(prime_count)
