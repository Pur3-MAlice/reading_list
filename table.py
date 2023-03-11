from rich.console import Console
from rich.table import Table
from rich import box
# from rich import print
import gspread
from google.oauth2.service_account import Credentials
# import os
# import datetime
# import time

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


records = tbr_data = TBR.get_all_values()
table = Table(title="TBR List", box=box.MINIMAL_HEAVY_HEAD)

for heading in records[0]:
    table.add_column(f"{heading}")

for row in records[1::1]:
    table.add_row(*row)

console = Console()
console.print(table)
