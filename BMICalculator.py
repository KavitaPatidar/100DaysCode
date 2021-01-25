height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))

BMI = round(weight/(height*height),2)
print(f"Your BMI is {BMI}.")