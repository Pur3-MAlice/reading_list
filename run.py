import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('reading_list')
TBR = SHEET.worksheet('tbr')
READ = SHEET.worksheet('read')
MENU_PROMT = '''Welcome back to your reading list!
Press "T" to go to your TBR.
Press "R" to go to your Read list.
Or press "B" to go to the About Section
'''

selected_option = input(MENU_PROMT).strip().lower()


def cls():
    '''
    function to clear the console for user using clear/cls command
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


tbr_data = TBR.get_all_values()
# print(tbr_data)

read_data = READ.get_all_values()
# print(read_data)


def list_choice(which_list):
    '''
    This function helps the user check their lists and add to their lists
    It's focuses on being used for both the TBR & READ worksheets
    '''
    print(f'''Welcome back to your reading list!
    Press "C" to Check your {which_list}.
    Press "A" to Add to your {which_list}.
    Or press "H" to go to Home''')
    
    # while selected_option != "":
    #     print()


def add_book(which_list):
    '''
    docstring
    '''
    title = input("Title:").strip().title()
    author = input("Author:").strip().title()
    print(f"Adding {title} written by {author}\n")


def list_book():
    '''
    docstring
    '''
    # if TBR empty print "your reading list is empty"
    # print(f"displaying {list_name}\n")
    # for book in reading_list:
    # print(f"{book['title']}, by "{book['author']})


while selected_option != "":
    if selected_option == "t":
        cls()
        print("Going to TBR list...\n")
        list_choice("TBR")
    elif selected_option == "r":
        cls()
        print("Going to READ list..\n")
        list_choice("READ")
        break
    elif selected_option == "b":
        cls()
        print("Going to About Section...\n")
        break
    else:
        print(f"'{selected_option}' is not valid option. Please try again")

    selected_option = input(MENU_PROMT).strip().lower()


# MAIN FUNCTION HERE THAT IS DEPLOYED AT END
# main()
