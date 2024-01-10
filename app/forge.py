" welcome to Forge "

import typer
from rich import print as rprint
import sqlite3

print()

rprint("[sandy_brown]+--------------------+[/sandy_brown]")
rprint("[sandy_brown]| Welcome to Forge🔥 |[/sandy_brown]")
rprint("[sandy_brown]+--------------------+[/sandy_brown]", end="\n\n")

app = typer.Typer()


@app.command()
def create():
    rprint("[gold3]Implementing logic for creating template here[/gold3]")
    name = input("Please enter the name of the project  :  ")

    rprint(f"[gold3]The name of the project you have entered is '{name.strip()}'[/gold3]")

    db_creation_choice = input("Please enter 'y' to proceed with creation of Database, enter 'n' to abort  :  ")

    if db_creation_choice.lower() == "y":
        rprint(f"[gold3]The name of the database is {name.replace(" ","")}[/gold3]")
        rprint("[gold3]Please enter 'y' to proceed or enter 'n' to change the name of the database[/gold3]")
        database_name_change_choice = input()

        if database_name_change_choice.lower() == "n":
            rprint("[gold3]Please enter the name of the database according to your need.[/gold3]")
            user_edited_database_name = input()
            rprint(f"[green1]Database name changed to {user_edited_database_name.replace(" ","")}[/green1]")

        elif database_name_change_choice.lower()=='y':
            rprint("[gold3]Database name retained.[/gold3]")
            exit(1)
        
        else:
            rprint("[gold3]Did not enter 'y' or 'n'.[/gold3]")
            exit(1)

        "+--------------------------------------+"
        "| implement creation of database logic |"
        "+--------------------------------------+"

    elif db_creation_choice.lower() == "n":
        rprint("[deep_pink2]Database name not changed \n Exiting because of exit(1)[/deep_pink2]")
        exit(1)

    else:
        rprint("[deep_pink2]Exiting because option enetered wasn't 'y' or 'n' and exit(1)[/deep_pink2]")
        exit(1)


@app.command()
def status():
    rprint("[gold3]Valid status codes for projects : [/gold3]", end='\n\n')
    rprint("[spring_green3]1. In Progress[/spring_green3]")
    rprint("[royal_blue1]2. Completed[/royal_blue1]")
    rprint("[yellow1]3. On Hold[/yellow1]")
    rprint("[dark_orange3]4. Dropped[/dark_orange3]")
    rprint("[grey50]5. Plan On Doing[/grey50]")
    print()
    
    status_choice=input("Please enter the status of your project :")
    status_choice=status_choice.strip()

    if status_choice.lower()=='1' or status_choice.lower()=="in progress":
        rprint('[spring_green3]Project status set to "In Progress"[/spring_green3]')
        exit(1)

    elif status_choice=='2' or status_choice.lower()=="completed":
        rprint('[royal_blue1]Project status set to "Completed"[/royal_blue1]')
        exit(1)

    elif status_choice=='3' or status_choice.lower()=="on hold":
        rprint('[yellow1]Project status set to "On Hold"[/yellow1]')
        exit(1)

    elif status_choice=='4' or status_choice.lower()=="dropped":
        rprint('[dark_orange3]Project status set to "Dropped"[/dark_orange3]')
        exit(1)

    elif status_choice=='5' or status_choice.lower()=="plan on doing":
        rprint('[grey50]Project status set to "Plan On Doing"[/grey50]')
        exit(1)

    else:
        rprint("[red3]Please enter a valid number or status number[/red3]")
        exit(1)


@app.command()
def update():
    rprint("[gold3]implement logic for updating info about project here[/gold3]")


@app.command()
def show():
    rprint("[gold3]implement logic for printing specified paramenter of project here[/gold3]")


@app.command()
def delete():
    rprint("[gold3]implement logic for deleting a project here[/gold3]")


if __name__ == "__main__":
    app()