#Tara M. Pattilachan
#COP3502C - Software Engineering (Password Encoder/Decoder)
# Lab Partner Norma Marin
#10/20/2023
#Lab 6 - Assignment

#Encoding the password by addding all digits by 3s
def encode(password):
    return ''.join(str((int(num) + 3) % 10) for num in str(password))


#Norma's decode portion completed
def decode(password):
    #decodes password
    decode_pass = ""
    for i in encode:
        decoded = str((int(i) - 3) % 10)
        decode_pass = decoded
    return decode_pass
#Main function 
def main():
    #Setting encode_pass to string
    encode_pass = ""

    #While the loop is running, print menu and elif options
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        
        #Prompts user for menu selection
        menu_selection = input("Please enter an option: ")
        #If option 1, user must create an 8-digit password, and will have it encoded
        if menu_selection == '1':
            password = (input("Please enter your password to encode: "))
            if len(password) == 8 and all(char in '0123456789' for char in password):
                encode_pass = encode(password)
                print("Your password has been encoded and stored!\n")
            else:
                print("Please enter a valid 8-digit password.\n")
        #If option 2, decoder is selected, conditionally requires an encoded password
        elif menu_selection == '2':
            if encode_pass:
                print(f"The encoded password is {encode_pass}.\n")
            else:
                print("You need a password encoded first!\n")
        #If option 3 is selected
        elif menu_selection == '3':
            break
        #If no menu selections are valid
        else:
            print("Please input a valid menu selection.\n")

#Runs this main function to directly execute in this file
if __name__ == "__main__":
    main()