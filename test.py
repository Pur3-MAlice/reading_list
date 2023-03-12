import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np

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

df = pd.DataFrame(tbr_data, index=None)

rows_tbr = len(df.axes[0]) - 1


print("TBR:", rows_tbr)

    


print(df)
df = df.drop_duplicates(subset=0)
print(df)
