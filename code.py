import sys
import random

logindata = ("Admin", "Admin1")
card1 = ("1234 1234 1234 1234", "John Doe", "02/01/1999")
card2 = ("1234 4321 1234 4321", "Jane Doe", "01/02/1999")
card3 = ("1111 2222 3333 4444", "Matthew Dover", "07.25.05")
end = ("y")
n = ("n")
username = input("Enter your username: ")
password = input("Enter your password: ")

if username and password in logindata:
    print("Correct Login!")

if username and password not in logindata:
    while username and password not in logindata:
        print('Invalid login!')
        sys.exit()
        

        
accountNumber = input("Enter Account Number: ")
name = input("Enter your name: ")
DOB = input("Enter Date of Birth: ")
if accountNumber and name and DOB in card1:
    print("Information is valid.")
    print("Your Current Balance is: $19421")
if accountNumber and name and DOB in card2:
    print("Information is valid.")
    print("Your Current Balance is: $1241")
if accountNumber and name and DOB in card3:
    print("Information is valid.")
    print("Your Current Balance is: $91403243")
    
if accountNumber and name and DOB not in card1:
    while accountNumber and name and DOB not in card1:
        if accountNumber and name and DOB not in card2:
            while accountNumber and name and DOB not in card2:
                if accountNumber and name and DOB not in card3:
                    while accountNumber and name and DOB not in card3:
                        print("Information is invalid.")
                        sys.exit()
