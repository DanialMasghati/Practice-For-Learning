# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_as_lower = name1.lower()
name2_as_lower = name2.lower()
# T  R  U  E
t_name=name1_as_lower.count("t")+name2_as_lower.count("t")
r_name=name1_as_lower.count("r")+name2_as_lower.count("r")
u_name=name1_as_lower.count("u")+name2_as_lower.count("u")
e_name=name1_as_lower.count("e")+name2_as_lower.count("e")
true_sum = t_name+r_name+u_name+e_name
#L O V E
l_love=name1_as_lower.count("l")+name2_as_lower.count("l")
o_love=name1_as_lower.count("o")+name2_as_lower.count("o")
v_love=name1_as_lower.count("v")+name2_as_lower.count("v")
e_love=name1_as_lower.count("e")+name2_as_lower.count("e")
love_sum=l_love+o_love+v_love+e_love
score=true_sum*10+love_sum
if score< 10 or score> 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score<  50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
