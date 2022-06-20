

import gspread
from google.oauth2.service_account import Credentials


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

data = questions.get_all_values()

tprint("\n\nSYR - TECH - AB\n\n", font='small',chr_ignore=True)


