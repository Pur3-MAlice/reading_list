import gspread
from google.oauth2.service_account import Credentials
import os
import datetime
import time
from rich.console import Console
from rich.table import Table
from rich import box

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('reading_list')
TBR = SHEET.worksheet('TBR')
READ = SHEET.worksheet('READ')


def cls():
    """
    function to clear the console for user using clear/cls command
    """
    os.system('cls' if os.name == 'nt' else 'clear')


CurrentDate = datetime.date.today()


tbr_data = TBR.get_all_values()


read_data = READ.get_all_values()


def add_book(which_list):
    """
    docstring
    """
    title = input("Title:").strip().title()
    author = input("Author:").strip().title()

    book_input = []
    book_input.append(title)
    book_input.append(author)
    book_input.append(str(CurrentDate))

    print(f"Adding {title} by {author} on {CurrentDate}\n")
    worksheet_update = SHEET.worksheet(f'{which_list}')
    worksheet_update.append_row(book_input)
    # prompt to add another or to go home


def list_book(which_list):
    """
    docstring
    """
    # if TBR empty print "your reading list is empty"
    print(f"displaying {which_list}\n")
    for book in which_list:
        print(f"{book['title']}, by {book['author']}")


def list_choice(which_list):
    """
    This function helps the user check their lists and add to their lists
    It's focuses on being used for both the TBR & READ worksheets
    """
    prompt = f'''Welcome back to your reading list!
    Press "C" to Check your {which_list}.
    Press "A" to Add to your {which_list}.
    Or press "H" to go to Home
    '''

    user_choice = input(prompt).strip().lower()

    while user_choice != "":
        if user_choice == "c":
            cls()
            print(f"Here is you current {which_list} list \n")
            list_book(which_list)
        elif user_choice == "a":
            cls()
            print(f"Going to {which_list} book entry..\n")
            add_book(which_list)
        elif user_choice == "h":
            cls()
            print("Going to Home...\n")
            home()
        else:
            print(f"'{user_choice}' is not valid option. Please try again")
            user_choice = input(prompt).strip().lower()
        break


def about():
    """
    docstring
    """
    print('''Your TBR (To Be Read) will store new titles input.
Your Read List will compile all books finished.

If you want to get started with your reading list.
Just follow the instructions on the home menu.
For example: Press "T" for TBR
Type "T" and press Enter.
Then you can interact with your TBR list''')
    time.sleep(2)
    home_prompt = "\nDo you want to go to the Home Screen?\nEnter: Y or N\n"
    about_leave = input(home_prompt).strip().upper()
    if about_leave == "Y":
        cls()
        home()
    elif about_leave == "N":
        cls()
        print("You chose not to leave the about page")
        about()
    else:
        print(f"'{about_leave}' is not valid option. try again")
        about_leave = input(home_prompt).strip().upper()


def home():
    """
    home page function
    """
    menu_prompt = '''Welcome back to your reading list!
    Press "T" to go to your TBR.
    Press "R" to go to your Read list.
    Or press "B" to go to the About Section
    '''
    selected_option = input(menu_prompt).strip().lower()

    while selected_option != "":
        if selected_option == "t":
            cls()
            print("Going to TBR list...\n")
            list_choice("TBR")
            break
        elif selected_option == "r":
            cls()
            print("Going to READ list..\n")
            list_choice("READ")
            break
        elif selected_option == "b":
            cls()
            print("Going to About Section...\n")
            about()
            break
        else:
            print(f"'{selected_option}' is not valid option. try again")
            selected_option = input(menu_prompt).strip().lower()
        break


home()

# # MAIN FUNCTION HERE THAT IS DEPLOYED AT END
# # main()
