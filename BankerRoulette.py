import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

people_number= len(names)
# print(people_number)

bill_payer= names[random.randint(0,people_number-1)]
print(f"{bill_payer} is going to buy the meal today.")

