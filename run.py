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
print(tbr_data)

read_data = READ.get_all_values()
print(read_data)

# USER TO CHOOSE ADD TO LIST, LOOK AT LIST?
# AFTER THIS THEN WHICH LIST

# USER TO ADD DATA TO READ
# TITLE, ATHOUR, DATE, NUMBER

# USER TO ADD DATA TO TBR
# TITLE, ATHOUR, DATE, NUMBER


# MAIN FUNCTION HERE THAT IS DEPLOYED AT END
# main()
