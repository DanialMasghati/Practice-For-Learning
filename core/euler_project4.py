def is_palindrome(number):
    return str(number) == str(number)[::-1]


largestPalindrome = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        Product_i_j = i*j
        # ye ghesmati bayad ezafe konim ke shart hamvare doros bashad
        if is_palindrome(Product_i_j) and Product_i_j > largestPalindrome:
            largestPalindrome = Product_i_j
print(largestPalindrome)
# print(is_palindrome(9009))
