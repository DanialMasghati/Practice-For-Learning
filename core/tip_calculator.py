# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill?")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people_share = input("How many people to split the bill? ")
total_bill = float(bill)
people_share_as_int = int(people_share)
tip_percent = int(tip)
tip_percent_num = (tip_percent+100)/100
each_people_share = total_bill / people_share_as_int
each_people_share_pay = each_people_share * tip_percent_num
massage = f"Each person should pay: {round(each_people_share_pay,2)}"
print(massage)
