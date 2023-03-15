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

df = pd.DataFrame(tbr_data)

rows_tbr = len(df.axes[0]) - 1

print("TBR:", rows_tbr)

print(f"DataFrame:\n{df}\n")

df2 = df[df.columns[0]]
print(df2)

title_list = df[df.columns[0]].values.tolist()
print(title_list)
