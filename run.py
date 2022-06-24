"""
Import gspread to work with google API
"""
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore

from art import tprint


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("syr-technologies")

customer = SHEET.worksheet("customers")

# Records the username input by customers in sheets
customer_details = []

# Prints logo and welcome sign
tprint("\n\nWelcome!\n\n", font="small", chr_ignore=True)
tprint("\n\nSYR - TECH - AB\n", font="small", chr_ignore=True)


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
                print(
                    Fore.RED + f"{user_name.name } is not valid. Try again"
                )
                continue
            elif len(user_name.name) <= 2 or len(user_name.name) > 25:
                print(Fore.RED + f"Your name '{user_name.name}'\
                should be between 3 to 12 characters. Try again.")
                continue
            else:
                customer_details.append(user_name.name)
                break
        except IndexError:
            print(f"\nWelcome to SYR-Tech AB {user_name.name}")
        break
    return user_name.name


TICKET_MENU = {"a", "b", "c"}


def ticket_order():
    """
    User selects ticket type and function recommends solutions
    It also forwards if the solution is not relevant for customer
    """
    print()
    print(
        f"\nHello and welcome {user_name.name}, Choose an option below!"
    )
    print()
    current_order = []
    while True:
        print("What do you need help with?")
        print()
        print("a) Account/Password, b) Software Error, c) Expired License")
        order = input()
        if order in TICKET_MENU:
            current_order.append(order)
        else:
            print("I'm sorry, choose a, b or c.")
            continue
        if order == "a":
            print("Have you tried the solutions below? yes/no")
            print()
            print("-Log out and in again and reset your password.")
            print("-Try logging in on another device/browser or app.")
            print("-Check if your internet connection is stable.")
            print("-Check if your account is outdated.")
            print()

        elif order == "b":
            print("Have you tried the solutions below? yes/no")
            print()
            print("-Restart your computer, delete & re-install software.")
            print("-Did you give permissions for the app on the settings?")
            print("-Use the Web version and see if it works?")
            print("-Try troubleshooting methods.")
            print()

        elif order == "c":
            print("Have you tried the solutions below? yes/no")
            print()
            print("-Do you have a valid license? Has it expired?")
            print("-Can you use your account in another browser or app?")
            print("-Can you log in to your account?")
            print("-Is it the first time you are facing such problem?")
            print()

        choice = input()
        if choice == ("yes"):
            print("Please contact our support desk; support@syrtech.com")
            print("syrtech.com, supportline; +4611223376")
            print()

        elif choice == ("no"):
            print("Please try suggested solutions and come back again.")
            print()

        else:
            print()
            print("You need to enter yes or no")
            continue

        if order_complete():
            return current_order


def order_complete():
    print("Do you need help with anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        print()
        print("You need to enter yes or no")
        return order_complete()


def output_order(order_list):
    print("Thank you for visiting us and have a great day!")
    print()
    for order in order_list:
        print("Chosen ticket for support")
        print(order)


def main():
    user_name()
    order = ticket_order()
    output_order(order)

    customer.append_row(customer_details)


if __name__ == "__main__":
    main()
