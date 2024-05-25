" welcome to Forge "
import sys
from pathlib import Path

import typer
from rich import print as rprint
from rich.prompt import Prompt as prompt

# from utils import db_utils

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils import db_utils

print()

app = typer.Typer()


@app.command()
def create():
    "whenever project is created successfuly all three tables for that project should be created"

    project_name = prompt_name()
    if project_name != None:
        entry_creation_details_list = db_utils.create_entry(project_name)

        rprint(f"[chartreuse3]Project '{project_name}' created  successfully ✨[/chartreuse3]")
        print()
        rprint("Project details :")
        print()
        rprint(f"[gold3]Project Name : {project_name}[/gold3]")
        rprint(f"[gold3]Project ID : {entry_creation_details_list[0]}[/gold3]")
        rprint(f"[gold3]Date of creation : {entry_creation_details_list[1]}[/gold3]")
        rprint(f"[gold3]Time of creation : {entry_creation_details_list[2]}[/gold3]")
    
    else:
        print("No name was given to the project")

# try to make this a module function
def prompt_name() -> str:
    name = prompt.ask("[gold3]Enter the name of your project[/gold3]")
    rprint(f"[gold3]The name of the project you have entered is '{name}'[/gold3]")
    rprint("[gold3]Proceed with creation? [Y/n][/gold3] ", end="")

    while True:
        db_creation_choice = input()

        if db_creation_choice.lower() == "" or db_creation_choice.lower() == "y":
            name = name.strip()
            return name

        elif db_creation_choice.lower() == "n":
            rprint(f"[light_salmon1]Project '{name.strip()}' not created[/light_salmon1]")
            rprint("[light_salmon1]Do you want to rename or abort project creation? [R/a][/light_salmon1]")

            while True:
                abort_rename_choice = input()

                if abort_rename_choice.lower() == "r":
                    rprint("[light_salmon1]Enter the name of the project[/light_salmon1]")
                    renamed_name = input()
                    renamed_name.strip()
                    return renamed_name

                elif abort_rename_choice.lower() == "" or abort_rename_choice.lower() == "a":
                    rprint("[red3]Aborting ...[/red3]")
                    break

                else:
                    rprint("[red3]Did not enter 'R' or 'a'[/red3]")
            break
        else:
            rprint("[red3]Did not enter 'y' or 'N'[/red3]")


@app.command()
def destroy():
    "deletes projects"
    projects, projectid, times, dates = db_utils.show_entry()

    name_id = dict(zip(projects, projectid))

    rprint("[gold3]Do you want to list all existing projects? [Y/n][/gold3]")

    while True:
        list_projects_input = input()
        if list_projects_input.lower()=='y':
            for i in range(len(projects)):
                print(f"{projects[i]} created at {times[i]} on {dates[i]}")
                break
        elif list_projects_input.lower()=='n':
                break
        else:
            print("Please enter Y or n")

    rprint("[gold3]Enter the project you want to delete : [/gold3]")
    project_to_be_deleted = input()

    id_project_to_be_deleted = name_id[project_to_be_deleted]
    destroy_operation_status = db_utils.delete_entry(project_to_be_deleted, id_project_to_be_deleted, projectid)

    if destroy_operation_status:
        print(f"Project {project_to_be_deleted} has been deleted")
    else:
        print("Project not found!!!")
        print("Project could not be deleted")


@app.command()
def update():
    "updates aspects of a particular project"


@app.command()
def show():
    "shows details about specific projects"
    rprint("[gold3]The following projects have been created : [/gold3]")
    projects, _, times, dates = db_utils.show_entry()
    for i in range(len(projects)):
        print(f"{projects[i]} created at {times[i]} on {dates[i]}")


@app.command()
def welcome():
    "welcome to Forge!!!"

    print(r"""
      ___         ___           ___           ___           ___     
     /  /\       /  /\         /  /\         /  /\         /  /\    
    /  /:/_     /  /::\       /  /::\       /  /:/_       /  /:/_   
   /  /:/ /\   /  /:/\:\     /  /:/\:\     /  /:/ /\     /  /:/ /\  
  /  /:/ /:/  /  /:/  \:\   /  /:/~/:/    /  /:/_/::\   /  /:/ /:/_ 
 /__/:/ /:/  /__/:/ \__\:\ /__/:/ /:/___ /__/:/__\/\:\ /__/:/ /:/ /\\
 \  \:\/:/   \  \:\ /  /:/ \  \:\/:::::/ \  \:\ /~~/:/ \  \:\/:/ /:/
  \  \::/     \  \:\  /:/   \  \::/~~~~   \  \:\  /:/   \  \::/ /:/ 
   \  \:\      \  \:\/:/     \  \:\        \  \:\/:/     \  \:\/:/  
    \  \:\      \  \::/       \  \:\        \  \::/       \  \::/   
     \__\/       \__\/         \__\/         \__\/         \__\/    
    """)

    print("")
    print("")

    rprint("[dark_orange]Welcome to Forge ⚒️ 🔥 [/dark_orange]")
    print()
    rprint("[gold3]Unleash your inner innovator with Forge, [/gold3]")
    rprint("[gold3]The ultimate terminal app for capturing your project ideas[/gold3]\n")

    rprint("[gold3]Say goodbye to scattered notes and forgetful details.[/gold3]", end="")
    rprint("[gold3] Forge keeps your ideas organized, with aims, descriptions, and resources[/gold3]")
    rprint("[gold3]Focus on what truly matters ~> building your projects to successfully.[/gold3]\n")


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
