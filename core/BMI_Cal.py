# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_m = float(height)
weight_kg = float(weight)

bmi_calculator = weight_kg // (height_m * height_m)
bmi_calculator_int = int(bmi_calculator)
print(bmi_calculator_int)
