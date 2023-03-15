import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

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

tbr_data = TBR.get_all_values()
read_data = READ.get_all_values()


title = input("Title:").strip().title()

df_tbr = pd.DataFrame(tbr_data)
df_read = pd.DataFrame(read_data)
# df_tbr_col = df_tbr[df_tbr.columns[0]]
# df_read_col = df_read[df_read.columns[0]]
tbr_title_list = df_tbr[df_tbr.columns[0]].values.tolist()
read_title_list = df_read[df_read.columns[0]].values.tolist()

if title in tbr_title_list:
    print(f'''{title} is already on your TBR list. 
    Press Y to add this Title anyway, Press N to Cancel''')
if title in read_title_list:
    print(f'''{title} is already on your TBR list. 
    Press Y to add this Title anyway, Press N to Cancel''')

# rows_tbr = len(df_tbr.axes[0]) - 1
# print("TBR:", rows_tbr)
# print(f"DataFrame:\n{df}\n") 
