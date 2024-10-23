# Rae Lancaster - Lab 6: Version Control

# encoder stores encoded password to new variable with each digit being shifted up by 3 numbers
def encode(password): # encode function
    str_result = "" # empty string result
    for digit in password:
        digit_as_int = int(digit) # convert digit to integer
        digit_as_int = (digit_as_int + 3) % 10 # add 3 to each digit, wrapping around via % to not exceed 9
        digit_as_string = str(digit_as_int) # convert digit back to string
        str_result += digit_as_string # add digit to string result
    return str_result

# decoder undoes encoded password and returns original password
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        # Shift each digit down by 3 and handle wraparound with modulo 10
        decoded_digit = (int(digit) - 3) % 10
        decoded_password += str(decoded_digit)
    return decoded_password




def main(): # main function

    password = None # initial value for variable 'password'
    encoded_password = None # initial value for variable 'encoded_password'

    while True:  # looping menu with encoder and decoder options

        print("\nMenu"
              "\n-------------"
              "\n1. Encode"
              "\n2. Decode"
              "\n3. Quit")

        menu_choice = int(input("\nPlease enter an option: ")) # prompt user to choose from menu

        # check if user input is 1
        if menu_choice == 1:
            # user can input 8-digit password in string format, integers only
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        # check if user input is 2
        elif menu_choice == 2:
            # check if password has been entered by user
            if password is None:
                print("No password stored. Please select menu option 1 to input a password to encode.")
                continue # reset loop
            else: # decode previously encoded password
                # pass encoded password through encoder function
                decoded_password = decode(encoded_password)
                password = decoded_password
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        # check if user input is 3
        elif menu_choice == 3:
            print("Goodbye!")
            break  # end program

        # check if user input is not 1, 2, 3
        else:
            print("Please enter valid menu option!")

if __name__ == "__main__":
    main()

