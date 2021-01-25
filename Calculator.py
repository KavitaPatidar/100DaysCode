from design import calculator_logo

def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(calculator_logo)
    num1 = int(input("What is the first number?\n"))
    for sign in operations:
        print(sign)
    further = True

    while further:

        user_operation = input("Pick an operation from above list?\n")
        next_num = int(input("What is the next number?\n"))

        calculation_function = operations[user_operation]
        answer = calculation_function(num1, next_num)

        print(f"{num1} {user_operation} {next_num} = {answer}")

        # user_operation=input("Pick an operation \n")
        # num3= int(input("What is the next number?\n"))
        # if user_operation in operations:
        #     calculation_function= operations[user_operation]
        #     second_answer=calculation_function(answer,num3)
        #
        # print(f" {answer} {user_operation} {num3} = {second_answer}")

        further_option = input(
            "To continue calculation type 'yes'. To start new calculation type 'new. Type 'no' for exit.\n")

        if further_option == "yes":
            num1 = answer

        elif further_option == "no":
            print("Goodbye")
            further = False

        else:
            further=False
            calculator()

calculator()