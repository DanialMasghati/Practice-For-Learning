# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
END_AGE = 90
all_days = 365
all_month = 12
all_weeks = 52
age_left = END_AGE - int(age)
age_left_days = age_left * all_days
age_left_month = age_left * all_month
age_left_weeks = age_left * all_weeks

print(
    f"You have {age_left_days} days, {age_left_weeks} weeks, and {age_left_month} months left.")
