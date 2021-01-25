import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
choosed_letter=""
choosed_letter_list=[]
for n in range(1,nr_letters+1):
    choosed_letter+= random.choice(letters)
    choosed_letter_list.append(random.choice(letters))


choosed_symbol=""
choosed_symbol_list=[]
for n in range(1,nr_symbols+1):
    choosed_symbol+= random.choice(symbols)
    choosed_symbol_list.append(random.choice(symbols))

choosed_number=""
choosed_number_list=[]
for n in range(1,nr_numbers+1):
    choosed_number+= random.choice(numbers)
    choosed_number_list.append(random.choice(numbers))

password_list=choosed_letter_list+choosed_symbol_list+choosed_number_list
random.shuffle(password_list)
# print(password_list)
hard_password=""
for l in password_list:
    hard_password+=l




password=choosed_letter+choosed_symbol+choosed_number
print(f"Easy Password: {password}")
print(f"Hard Password: {hard_password}")
