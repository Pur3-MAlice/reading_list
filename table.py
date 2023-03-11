from rich.console import Console
from rich.table import Table

table = Table(title="List")

table.add_column("Date Added", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Author", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "j")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "poo")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)