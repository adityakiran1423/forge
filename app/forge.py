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
    rprint("[gold3]Please enter the name of the project  :[/gold3]")
    name = input()

    rprint(f"[gold3]The name of the project you have entered is '{name.strip()}'[/gold3]")

    # proceed with database creation?
    rprint("[gold3]Proceed with project creation? 'y'/'N'[/gold3]")
    while True:
        db_creation_choice=input()

        if db_creation_choice.lower() == "y":
            rprint(f"[gold3]The name of the database is {name.replace(" ","")}.db[/gold3]")

            # proceed to change database name?
            rprint("[gold3]Do you want to change the name of the database? 'y'/'N'[/gold3]")
            # print("running while here")
            while True:
                database_name_change_choice = input()
                if database_name_change_choice.lower() == 'y':
                    rprint("[gold3]Enter name of database.[/gold3]")
                    user_edited_database_name = input()
                    rprint(f"[green1]Success ✨[/green1]")
                    rprint(f"[green1]Database name changed to {user_edited_database_name.replace(" ","")}.db[/green1]")
                    break

                elif database_name_change_choice.lower()=='n':
                    rprint("[gold3]Database name retained.[/gold3]")
                    break
                
                else:
                    rprint("[red3]Did not enter 'y' or 'n'.[/red3]")
                    # exit(1)

                "+--------------------------------------+"
                "| implement creation of database logic |"
                "+--------------------------------------+"
            break

        elif db_creation_choice.lower() == "n":
            rprint(f"[deep_pink2]Project '{name.strip()}' not created \nExiting because of exit(1)[/deep_pink2]")
            rprint("[deep_pink2]Do you want to rename your project or abort creation?[/deep_pink2]")
            rprint("[deep_pink2]Press 'r' to rename and 'a' to abort project creation[/deep_pink2]")

            abort_rename_choice=input()

            if abort_rename_choice.lower()=='r':
                rprint("[deep_pink2]Please enter renamed name of the project[/deep_pink2]")
                renamed_name=input()
                rprint(f"[deep_pink2]Renamed name of the project is {renamed_name.strip()}[/deep_pink2]")
                break

            elif abort_rename_choice.lower()=='a':
                rprint("[deep_pink2]Aborting project creation process[/deep_pink2]")
                break
            else:
                rprint("[red3]Did not enter 'a' or 'r'[/red3]")

            break
            # exit(1)

        else:
            rprint("[deep_pink2]Did not enter 'y' or 'N'[/deep_pink2]")
            # exit(1)


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