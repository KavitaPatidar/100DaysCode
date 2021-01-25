number=int(input("Please enter any number:\n"))

def prime_number(number):
    is_prime=True
    for n in range(2,number):
        if number%n==0:
            is_prime=False
    if is_prime:
        print("It's a prime")
    else:
        print("It's not a prime")
prime_number(number)