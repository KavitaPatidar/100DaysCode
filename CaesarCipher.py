from design import caesar_cipher_logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(caesar_cipher_logo)
play_continue=True

while play_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # def encrypt(text, shift):
    #     encrypted_message=""
    #     for l in text:
    #         # if l in alphabet:
    #         i=alphabet.index(l)
    #         new_index= i+shift
    #         encrypted_message+=alphabet[new_index]
    #     print("Encoded message is: "+ encrypted_message)
    #
    #
    # def decrypt(text, shift):
    #     decrypted_message=""
    #     for l in text:
    #         # if l in alphabet:
    #         i=alphabet.index(l)
    #         new_index= i-shift
    #         decrypted_message+=alphabet[new_index]
    #     print("Decoded message is: "+ decrypted_message)
    #
    # if direction=="encode":
    #     encrypt(text, shift)
    # else:
    #     decrypt(text, shift)

    # combining both function into one:
    def caesar(text, shift, direction):
        message=""
        for l in text:
            i=alphabet.index(l)
            if direction=="encode":
                new_index= i+shift
            else:
                new_index= i-shift
            message+=alphabet[new_index]
        print(f"{direction}d message is {message}.")
    caesar(text, shift, direction)
    play_again=input("Type 'yes' if you want to go again. Otherwise type 'no': ")

    if play_again=="no":
        print("Goodbye")
        play_continue=False