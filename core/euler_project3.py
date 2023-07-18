# import math


def largest_prime_factor(number):
    largest_factor = 1

    # Divide by 2 until it is no longer divisible
    while number % 2 == 0:
        largest_factor = 2
        number = number // 2

    # Check for prime factors starting from 3
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            largest_factor = i
            number //= i

    # If the remaining number is greater than 2, it is prime
    if number > 2:
        largest_factor = number

    return largest_factor


# Test with the given number
number = 600851475143
largest_factor = largest_prime_factor(number)
print("The largest prime factor of", number, "is", largest_factor)
