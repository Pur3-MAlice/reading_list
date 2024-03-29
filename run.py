import os
import random
import string
import datetime
import time
import gspread
from google.oauth2.service_account import Credentials
from rich.console import Console
from rich.table import Table
from rich import box
import pyfiglet
import pandas as pd


# This code is taken from the code insitute love sandwiches code
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Some of the below code is taken from the code institute's love sandwiches
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('reading_list')
TBR = SHEET.worksheet('TBR')
READ = SHEET.worksheet('READ')


def cls():
    """
    function to clear the console for user using clear/cls command
    this code was taken from import os
    """
    os.system('cls' if os.name == 'nt' else 'clear')


current_date = datetime.date.today()  # from datetime
tbr_data = TBR.get_all_values()
read_data = READ.get_all_values()


def add_book(which_list):
    """
    Fucntion to add in book title and author to the
    selected worksheet. Selected at the home() function
    """
    title = input("Title:").strip().title()
    author = input("Author:").strip().title()
    random_num = random.randint(1, 100)  # from random
    random_letter = random.choice(string.ascii_letters)  # from string

    book_input = []
    book_input.append(str(title))
    book_input.append(str(author))
    book_input.append(str(current_date))
    book_input.append(str(random_num) + str(random_letter))

    df_tbr = pd.DataFrame(tbr_data)  # dataframe from pandas
    df_read = pd.DataFrame(read_data)
    tbr_title_list = df_tbr[df_tbr.columns[0]].values.tolist()
    read_title_list = df_read[df_read.columns[0]].values.tolist()

    if len(title) < 1 or len(author) < 1:
        print("The Title and Author must contain atleast 1 character")

    else:
        while True:
            if title in tbr_title_list:
                title_prompt = f'''{title} is already on your TBR list.
                Press Y to add this Title anyway, Press N to Cancel\n'''
            elif title in read_title_list:
                title_prompt = f'''{title} is already on your READ list.
                Press Y to add this Title anyway, Press N to Cancel\n'''
            else:
                title_prompt = ""
            if title_prompt:
                add_dupe = input(title_prompt).strip().upper()
                if add_dupe == "Y":
                    print(f"Adding {title} by {author} on {current_date}\n")
                    worksheet_update = SHEET.worksheet(f'{which_list}')
                    worksheet_update.append_row(book_input)
                    break
                elif add_dupe == "N":
                    print("Please choose another Title")
                    break
                else:
                    print(f"'{add_dupe}' is not valid option. try again")
            else:
                print(f"Adding {title} by {author} on {current_date}\n")
                worksheet_update = SHEET.worksheet(f'{which_list}')
                worksheet_update.append_row(book_input)
                break


def list_book(which_list):
    """
    fucntion to create table of entries to mimick the sheet
    in the command centre. Also return back to list_choice
    after a pause.
    """
    print(f"displaying {which_list}\n")
    if which_list == "TBR":
        records = TBR.get_all_values()
        table = Table(  # Table code inspired by example code from rich
            title="TBR List",
            box=box.MINIMAL_HEAVY_HEAD,
            show_lines=True,
            header_style="dark_green")
    elif which_list == "READ":
        records = READ.get_all_values()
        table = Table(
            title="READ List",
            box=box.MINIMAL_HEAVY_HEAD,
            show_lines=True,
            header_style="dark_green")
    else:
        print("Oh no! Somthing went wrong. Please try again.")

    for heading in records[0]:
        table.add_column(f"{heading}")

    for row in records[1::1]:
        table.add_row(*row)

    console = Console()
    console.print(table)
    time.sleep(2)  # all time.sleep events are taken from time


def list_choice(which_list):
    """
    Function for user to check their list in table format
    It's focuses on being used for both the TBR & READ worksheets
    """
    prompt = f'''Welcome back to your reading list!
    Press "C" to Check your {which_list}.
    Press "A" to Add to your {which_list}.
    Or press "H" to go to Home
    '''

    user_choice = input(prompt).strip().lower()

    while user_choice != " ":
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
            time.sleep(.5)
        else:
            print(f"'{user_choice}' is not valid option. Please try again")
            list_choice(which_list)
        break


def about():
    """
    Function called by user selction at home()
    Tells user about the app and how to use.
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
    elif about_leave == "N":
        cls()
        print("You chose not to leave the about page")
        about()
    else:
        print(f"'{about_leave}' is not valid option. Taking you home")


def delete_row(title_delete):
    """
    delete row based on title
    """
    sheet = TBR
    cell = sheet.find(title_delete)
    if cell is not None:
        row_number = cell.row
        sheet.delete_rows(row_number)
        print(f"{title_delete} has been deleted.")
    else:
        print(f"{title_delete} not found in To Be Read list.")


def select_title():
    """
    Function to get the user to select the unique code
    of the book input
    """
    title_prompt = "Please input the title:\n"
    title_delete = input(title_prompt).strip().title()
    print(title_delete)
    delete_row(title_delete)


def home():
    """
    Function for the initalisation home() helps user
    get through the code and is the backstop of thier
    usage.
    """
    menu_prompt = '''Welcome back to your reading list!
    Press "T" to go to your TBR.
    Press "R" to go to your Read list.
    Press "B" to go to the About Section.
    Press "D" to remove a row from your TBR.
    Or Press "X" to cancel.
    '''
    selected_option = input(menu_prompt).strip().lower()

    while selected_option != " ":
        if selected_option == "t":
            cls()
            print("Going to TBR list...\n")
            time.sleep(.5)
            list_choice("TBR")
        elif selected_option == "r":
            cls()
            print("Going to READ list..\n")
            time.sleep(.5)
            list_choice("READ")
        elif selected_option == "b":
            cls()
            print("Going to About Section...\n")
            time.sleep(.5)
            about()
        elif selected_option == "d":
            print("Going to Delete Section...\n")
            time.sleep(.5)
            select_title()
        elif selected_option == "x":
            print("Canceling...\n")
            time.sleep(.5)
            cls()
            print("Cancelled")
            break
        else:
            print(f"'{selected_option}' is not valid option. try again")
        selected_option = input(menu_prompt).strip().lower()


def banner():
    """
    Prints the ascii art as a banner. From pyfiglet
    Code from https://www.devdungeon.com
    """
    ascii_banner = pyfiglet.figlet_format("Reading List")
    print(ascii_banner)


banner()
home()
