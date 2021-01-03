# Driver age definition program

driver = input("Please Enter your name:- ")
print("welcome", driver, "to the age recognition program. We will help you decide whether to drive car or not.")
age = int(input("Please enter your age:- "))
if 0 >= age >= 100:
    print("Not valid age, Please restart the program!!!")
elif 1 <= age <= 17:
    print("You are under-age. We suggest you to wait for minimum", 18-age, "Year(s)")
elif age == 18:
    print("You are eligible for driving. We leave the opinion about learning on you!!")
elif 19 >= age > 99:
    print("You are eligible and perfectly alright to take driving classes and obtain license!!")
else:
    print("Wrong input!!")