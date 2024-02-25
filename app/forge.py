" welcome to Forge "

import typer
from rich import print as rprint
from rich.prompt import Prompt as prompt

from database import create_entry, edit_entry, show_entry, delete_entry

"""
all the data that needs to be stored will be stored via functions declared in database.py
"""

print()
rprint("[indian_red1]+------------+[/indian_red1]")
# rprint("[indian_red1]|[/indian_red1][dark_orange] Forge ⚒️ 🔥 [/dark_orange][indian_red1]|[/indian_red1]")
rprint("[indian_red1]|[/indian_red1][yellow3] Forge ⚒️ 🔥 [/yellow3][indian_red1]|[/indian_red1]")
rprint("[indian_red1]+------------+[/indian_red1]", end="\n\n")

app = typer.Typer()


@app.command()
def welcome():
    "welcome to Forge!!!"
    rprint("[dark_orange]Welcome to Forge ⚒️ 🔥 [/dark_orange]")
    print()
    rprint("[gold3]Unleash your inner innovator with Forge, [/gold3]")
    rprint("[gold3]the ultimate terminal app for capturing and nurturing your project ideas[/gold3]\n")

    rprint("[gold3]Say goodbye to scattered notes and forgetful details.[/gold3]", end="")
    rprint("[gold3] Forge keeps your ideas organized, with clear aims, descriptions, and resources[/gold3]")
    rprint("[gold3]Focus on what truly matters - bringing your dreams to life.[/gold3]\n")

    rprint("[gold3]Forge empowers you to streamline your workflow and turn those sparks into reality.[/gold3]\n")


@app.command()
def create():
    "whenever project is created successfuly all three tables for that project should be created"
    name = prompt.ask("[gold3]Enter the name of your project[/gold3]")
    rprint(f"[gold3]The name of the project you have entered is '{name}'[/gold3]")
    # enter row addition code here
    rprint("[gold3]Proceed with creation? [Y/n][/gold3] ", end="")

    while True:
        db_creation_choice = input()

        if db_creation_choice.lower() == "" or db_creation_choice.lower() == "y":
            rprint(f"[chartreuse3]Project '{name.strip()}' created  successfully ✨[/chartreuse3]")
            create_entry(name.strip())
            break

        elif db_creation_choice.lower() == "n":
            rprint(f"[light_salmon1]Project '{name.strip()}' not created[/light_salmon1]")
            rprint("[light_salmon1]Do you want to rename or abort project creation? [r/A][/light_salmon1]")

            while True:
                abort_rename_choice = input()

                if abort_rename_choice.lower() == "r":
                    rprint("[light_salmon1]Enter the name of the project[/light_salmon1]")
                    renamed_name = input()
                    rprint(f"[chartreuse3]Project '{renamed_name.strip()}' created successfully ✨[/chartreuse3]")
                    create_entry(renamed_name.strip())
                    break

                elif abort_rename_choice.lower() == "" or abort_rename_choice.lower() == "a":
                    rprint("[red3]Aborting ...[/red3]")
                    break

                else:
                    rprint("[red3]Did not enter 'r' or 'A'[/red3]")

            break

        else:
            rprint("[red3]Did not enter 'y' or 'N'[/red3]")


@app.command()
def update():
    "updates aspects of a particular project"


@app.command()
def show():
    "shows details about specific projects"
    rprint("[gold3]implement logic for printing specified paramenter of project here[/gold3]")


@app.command()
def delete():
    "deletes projects"
    rprint("[gold3]implement logic for deleting a project here[/gold3]")
    "used for deleting projects once they are created"


if __name__ == "__main__":
    app()


"logic for project status column"
# rprint("[spring_green3]1. In Progress[/spring_green3]")
# rprint("[royal_blue1]2. Completed[/royal_blue1]")
# rprint("[yellow1]3. On Hold[/yellow1]")
# rprint("[dark_orange3]4. Dropped[/dark_orange3]")
# rprint("[grey50]5. Plan On Doing[/grey50]")
# print()

# status_choice = input("Please enter the status of your project :")
# status_choice = status_choice.strip()

# rprint("[gold3]Please enter the name of the project  :[/gold3]")

# if status_choice.lower() == "1" or status_choice.lower() == "in progress":
#     rprint('[spring_green3]Project status set to "In Progress"[/spring_green3]')
#     exit(1)

# elif status_choice == "2" or status_choice.lower() == "completed":
#     rprint('[royal_blue1]Project status set to "Completed"[/royal_blue1]')
#     exit(1)

# elif status_choice == "3" or status_choice.lower() == "on hold":
#     rprint('[yellow1]Project status set to "On Hold"[/yellow1]')
#     exit(1)

# elif status_choice == "4" or status_choice.lower() == "dropped":
#     rprint('[dark_orange3]Project status set to "Dropped"[/dark_orange3]')
#     exit(1)

# elif status_choice == "5" or status_choice.lower() == "plan on doing":
#     rprint('[grey50]Project status set to "Plan On Doing"[/grey50]')
#     exit(1)

# else:
#     rprint("[red3]Please enter a valid number or status number[/red3]")
#     exit(1)
