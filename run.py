

import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore

from art import tprint


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')    
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('syr-technologies')

customer = SHEET.worksheet('customers')

customer_details = []

tprint("\n\nWelcome!\n\n", font='small', chr_ignore=True)
tprint("\n\nSYR - TECH - AB\n", font='small', chr_ignore=True)



def user_name():
    """
    User inputs their name, and function checks if
    the user name is valid, without space, no numbers.
    It also checks if the name is less than 2 or more than 25 character
    """
    while True:
        try:
            user_name.name = input(Fore.BLUE + "\nEnter your \
username: ").capitalize()
            if not user_name.name.isalpha():
                print(Fore.RED + f"{user_name.name } is not a valid username. Try again")
                continue
            elif len(user_name.name) <= 2 or len(user_name.name) > 25:
                print(Fore.RED + f"Your name '{user_name.name}' should be between 3 to \
12 characters. Try again.")
                continue
            else:
                customer_details.append(user_name.name)
                break
        except IndexError:
            print(f"\nWelcome to SYR-Tech AB {user_name.name}")
        break
    return user_name.name


MENU = {"a","b","c"}


def get_order():
    print()
    print(f"\nHello and welcome {user_name.name}, are you facing problems regarding our services? Choose an option below!")
    print()
    current_order = []
    while True:
        print("What do you need help with?")
        print()
        print("a) Account/Password, b) Software Error, c) Expired License")
        order = input()
        if order in MENU:
            current_order.append(order)
        else:
            print("I'm sorry, we can't help you with that.")
            continue
        if order == "a":
            print("Have you tried the below solutions? yes/no")
            print()
            print("a) Logging out and in again. b) Reset your password. c) Try logging in on another device/browser or app. d) Erasing browser cache.")

        elif order == "b":
            print("Have you tried the below solutions? yes/no")
            print()
            print("a) Restarting your computer? b) Delete and re-install the application? c) Did you give permission for the app on your settings? d) Use the Web version and see if it works?")  

        elif order == "c":
            print("Have you tried the below solutions? yes/no")
            print()
            print("a) Do you have a valid License? b) Have you checked if it expired? c) Can you use your account in another browser or app? d) Can you log in to your account?")        

        choice = input()    
        if choice == ("yes"):
            print("Please contact our support desk.")
            print()
            
        elif choice == ("no"):   
            print("Please try suggested solutions and comeback again.")
            print()

            
        else: 
            raise Exception("invalid input")   
            break

        if is_order_complete():
            return current_order

def is_order_complete():
    print("Do you need help with anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")

def output_order(order_list):
    print("Thank you for visiting us and have a great day")
    print()
    for order in order_list:
        print("Chosen ticket for support")
        print(order) 

def main():
    user_name()
    order = get_order()
    output_order(order)

    customer.append_row(customer_details)



if __name__ == "__main__":
    main()