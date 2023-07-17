#  encode each digit by 3
def encode_password(password):   # Kwailan Rosell
    encoded_password = ""
    for char in password:
        encoded_char = str(int(char) + 3)
        encoded_password += encoded_char

    return encoded_password


def decode_password(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        decoded_char = str(int(char) - 3)
        decoded_password += decoded_char
    
    return decoded_password


def main():
    encoded_password = ""
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("\nPlease enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            decoded_password = decode_password(encoded_password)
            print("The encoded password is " + encoded_password +", and the original password is " + decoded_password + ".")

        elif option == "3":
            break


if __name__ == '__main__':
    main()


