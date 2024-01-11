" welcome to Forge "

import typer
from rich import print as rprint

# import sqlite3

print()

rprint("[red]+-----------------------+[/red]")
rprint("[red]|[/red][dark_orange] Welcome to Forge ⚒️ 🔥 [/dark_orange][red]|[/red]")
rprint("[red]+-----------------------+[/red]", end="\n\n")

app = typer.Typer()

@app.command()
def colours():
    print("Command to see how the colour looks in the terminal")
    rprint("[gold3]gold3[/gold3]")
    rprint("[red]red[/red]")
    rprint("[orange_red1]orange_red1[/orange_red1]")
    rprint("[dark_orange]dark_orange[/dark_orange]")
    rprint("[orange3]orange3[/orange3]")
    rprint("[light_salmon1]light_salmon1[/light_salmon1]")
    rprint("[grey27]grey27[/grey27]")
    rprint("[cyan1]cyan1[/cyan1]")
    rprint("[cyan]cyan[/cyan]")
    rprint("[turquoise4]turquoise4[/turquoise4]")
    

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
            rprint(f"[chartreuse3]Success ✨[/chartreuse3]")
            rprint(f"[chartreuse3]The name of the project is '{name.strip()}'[/chartreuse3]")
            break

        elif db_creation_choice.lower() == "n":
            rprint(f"[light_salmon1]Project '{name.strip()}' not created[/light_salmon1]")
            rprint("[light_salmon1]Do you want to rename your project or abort creation?[/light_salmon1]")
            rprint("[light_salmon1]Press 'r' to rename and 'a' to abort project creation[/light_salmon1]")
            while True:
                abort_rename_choice=input()

                if abort_rename_choice.lower()=='r':
                    rprint("[light_salmon1]Please enter renamed name of the project[/light_salmon1]")
                    renamed_name=input()
                    rprint(f"[chartreuse3]Success ✨[/chartreuse3]")
                    rprint(f"[chartreuse3]Renamed name of the project is {renamed_name.strip()}[/chartreuse3]")
                    break

                elif abort_rename_choice.lower()=='a':
                    rprint("[red3]Aborting project creation process[/red3]")
                    break

                else:
                    rprint("[red3]Did not enter 'a' or 'r'[/red3]")

            break
            # exit(1)

        else:
            rprint("[red3]Did not enter 'y' or 'N'[/red3]")
            # exit(1)


@app.command()
def status():
    rprint("[gold3]Valid status codes for projects : [/gold3]", end='\n')
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