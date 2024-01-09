" welcome to Forge "

import typer
from rich import print as rprint
import sqlite3

print()

rprint("[sandy_brown]+------------------+[/sandy_brown]")
rprint("[sandy_brown]| Welcome to Forge |[/sandy_brown]")
rprint("[sandy_brown]+------------------+[/sandy_brown]", end='\n\n')

app = typer.Typer()

@app.command()
def create():
    rprint("[gold3]Implementing logic for creating template here[/gold3]")
    name=input("Please enter the name of the project  :  ")
    rprint(f"[gold3]The name of the project you have entered is {name.replace(" ","")}[/gold3]")
    db_creation_choice=input("Please enter 'y' to proceed with creation of Database, enter 'n' to abort  :  ")
    if db_creation_choice.lower()=='y':
        rprint(f"[gold3]The name of the database is {name.replace(" ","")}[/gold3]")
        rprint("[gold3]Please enter 'y' to proceed.[/gold3]")
        rprint("[gold3]Enter 'n' to change the name of the databse.[/gold3]")
        database_name_change=input()
        if database_name_change=='n':
            rprint("[gold3]Please enter the name of the database according to your need.[/gold3]")
            user_edited_database_name=input()
            rprint(f"[green1]Database name changed to {user_edited_database_name.replace(" ","")}[/green1]")

        " ------------------------------------ "
        " implement creation of database logic "
        " ------------------------------------ "

    elif db_creation_choice.lower()=='n':
        rprint("[deep_pink2]Database name not changed[/deep_pink2]")
        exit(1)
    else:
        exit(1)

@app.command()
def status():
    rprint("[gold3]implement logic for printing all info about project here[/gold3]")


@app.command()
def update():
    rprint("[gold3]implement logic for updating info about project here[/gold3]")


@app.command()
def show():
    rprint("[gold3]implement logic for printing specified paramenter of project here[/gold3]")


if __name__ == "__main__":
    app()