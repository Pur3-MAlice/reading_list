from rich.console import Console
from rich.table import Table
from rich import print


table = Table(title="List")

table.add_column("Date Added", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Author", style="green")

table.add_row('date', 'title', 'author')
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "poo")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")


print("Welcome to [bold magenta]YOUR[/bold magenta] a smart reading list!")


print(''' Your TBR (To Be Read) will store new titles input.
Your Read List will compile all books finished.

If you want to get started with your reading list.
Just follow the instructions on the home menu.
For example: Press "T" for TBR
Type "T" and press Enter.
Then you can interact with your TBR list''')


print("Welcome to guru99 Python Tutorials")

print("This message will be printed after a wait of 5 seconds")

console = Console()
console.print(table)
