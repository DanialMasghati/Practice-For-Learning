# "hello"
# print("hello"[4])
digit = input("enter your digit? ")
digit_num = int(digit)
# 39 -- > 3
digit_num_dahgan = digit_num // 10
# 39 -- > 9
digit_num_yekan = digit_num % 10

sum_of_digit = digit_num_dahgan+digit_num_yekan
print(f"your sum of digit is:{sum_of_digit}")
