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


def cls():
    '''
    function to clear the console for user using clear/cls command
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def home():
    '''
    home page function
    '''
    menu_prompt = '''Welcome back to your reading list!
    Press "T" to go to your TBR.
    Press "R" to go to your Read list.
    Or press "B" to go to the About Section
    '''
    selected_option = input(menu_prompt).strip().lower()

    while selected_option != "":
        if selected_option == "t":
            # cls()
            print("Going to TBR list...\n")
            # list_choice("TBR")
            break
        elif selected_option == "r":
            # cls()
            print("Going to READ list..\n")
            # list_choice("READ")
            break
            break
        elif selected_option == "b":
            cls()
            print("Going to About Section...\n")
            break
        else:
            print(f"'{selected_option}' is not valid option. Please try again")
            selected_option = input(menu_prompt).strip().lower()
        break 


home()


# tbr_data = TBR.get_all_values()
# # print(tbr_data)

# read_data = READ.get_all_values()
# # print(read_data)


# def list_choice(which_list):
#     '''
#     This function helps the user check their lists and add to their lists
#     It's focuses on being used for both the TBR & READ worksheets
#     '''
#     prompt = (f'''Welcome back to your reading list!
#     Press "C" to Check your {which_list}.
#     Press "A" to Add to your {which_list}.
#     Or press "H" to go to Home''')

#     user_choice = input(prompt).strip().lower()

#     while user_choice != "":
#         if user_choice == "c":
#             cls()
#             print(f"Here is you current {which_list} list \n")
#             list_book(which_list)
#         elif user_choice == "a":
#             cls()
#             print(f"Going to {which_list} book entry..\n")
#             add_book(which_list)
#         elif user_choice == "h":
#             cls()
#             print("Going to Home...\n")
#             # call main funct?
#             break
#         else:
#             print(f"'{selected_option}' is not valid option. Please try again")
#             user_choice = input(prompt).strip().lower()
#         break


# def add_book(which_list):
#     '''
#     docstring
#     '''
#     title = input("Title:").strip().title()
#     author = input("Author:").strip().title()
#     print(f"Adding {title} written by {author}\n")


# def list_book(which_list):
#     '''
#     docstring
#     '''
#     # if TBR empty print "your reading list is empty"
#     # print(f"displaying {list_name}\n")
#     # for book in reading_list:
#     # print(f"{book['title']}, by "{book['author']})

# # MAIN FUNCTION HERE THAT IS DEPLOYED AT END
# # main()
