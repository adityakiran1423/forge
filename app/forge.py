" welcome to Forge "

import typer
from rich import print as rprint
import sqlite3

rprint("[sandy_brown]Welcome to Forge[/sandy_brown]")

app=typer.Typer()

"use if and else to count number of args passed when running command, if 2 print welcome"
"if more than it will redirect to app.command section"

@app.command()
def create():
    rprint("[gold1]implement logic for creating template here[/gold1]")

@app.command()
def status():
    rprint("[gold1]implement logic for printing all info about project here[/gold1]")

@app.command()
def update():
    rprint("[gold1]implement logic for updating info about project here[/gold1]")

@app.command()
def show():
    rprint("[gold1]implement logic for printing specified paramenter of project here[/gold1]")

if __name__=="__main__":
    app()