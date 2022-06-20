

import gspread
from google.oauth2.service_account import Credentials

import colorama
from colorama import Fore, Back, Style

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

questions = SHEET.worksheet('questions')
customer = SHEET.worksheet('customers')

customer_details = []

tprint("\n\nWelcome!\n\n", font='small',chr_ignore=True)
tprint("\n\nSYR - TECH - AB\n", font='small',chr_ignore=True)



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


def main():
    user_name()

    customer.append_row(customer_details)


if __name__ == "__main__":
    main()