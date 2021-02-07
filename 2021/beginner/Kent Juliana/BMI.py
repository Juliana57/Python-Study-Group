height = float(input("Enter your height:"))
weight = float(input("Enter yor weight:"))

bmi = (weight * 703)/height**2

if bmi > 25:
    print("You are overwight!")
elif bmi == 18.5 and bmi <25:
    print("You have optimal weight")
elif bmi < 18.5:
    print("You are under weight")