import gspread
from google.oauth2.service_account import Credentials

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

tbr_data = TBR.get_all_values()
# print(tbr_data)

read_data = READ.get_all_values()
# print(read_data)

MENU_PROMT = '''Welcome back to your reading list! 
Press "T" to go to your TBR. Press "R" to go to your Read list.
Or press "B" to go to the About Section
'''

selected_option = input(MENU_PROMT).strip().lower()

while selected_option != "b":
    if selected_option == "t":
        print("Going to TBR list...\n")
        break
    elif selected_option == "r":
        print("Going to READ list..\n")
        break
    else:
        print(f"'{selected_option}' is not valid option. Please try again")

    selected_option = input(MENU_PROMT).strip().lower()    


# USER TO CHOOSE ADD TO LIST, LOOK AT LIST?
# AFTER THIS THEN WHICH LIST

# USER TO ADD DATA TO READ
# TITLE, ATHOUR, DATE, NUMBER

# USER TO ADD DATA TO TBR
# TITLE, ATHOUR, DATE, NUMBER


# MAIN FUNCTION HERE THAT IS DEPLOYED AT END
# main()
