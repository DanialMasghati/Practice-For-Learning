# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

bmi_calculator = weight / (height ** 2)
# bmi_calculator_2f = f"bmi_calculator: .2f"
bmi_calculator_2f = float("{:.2f}".format(bmi_calculator))
# print(bmi_calculator_2f)
if bmi_calculator_2f < 18.5:
    print(f"Your BMI is {bmi_calculator_2f}, you are underweight.")
elif 18.5<= bmi_calculator_2f<25:
    print(f"Your BMI is {bmi_calculator_2f}, you have a normal weight.")
elif 25<= bmi_calculator_2f<30:
    print(f"Your BMI is {bmi_calculator_2f}, you are slightly overweight.")
elif 30<= bmi_calculator_2f<35:
    print(f"Your BMI is {bmi_calculator_2f}, you are obese.")
else:
    print(f"Your BMI is {bmi_calculator_2f}, you are clinically obese.")