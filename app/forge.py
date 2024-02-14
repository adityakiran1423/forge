" welcome to Forge "

import typer
from rich import print as rprint
from rich.prompt import Prompt as prompt

# import create_db

"""
all the data that needs to be stored will be stored via functions declared in database.py
"""

print()
rprint("[indian_red1]+------------+[/indian_red1]")
# rprint("[indian_red1]|[/indian_red1][dark_orange] Forge ⚒️ 🔥 [/dark_orange][indian_red1]|[/indian_red1]")
rprint("[indian_red1]|[/indian_red1][gold3] Forge ⚒️ 🔥 [/gold3][indian_red1]|[/indian_red1]")
rprint("[indian_red1]+------------+[/indian_red1]", end="\n\n")

app = typer.Typer()

@app.command()
def welcome():
    rprint("[dark_orange]Welcome to Forge ⚒️ 🔥 [/dark_orange]")
    print()
    rprint("[yellow2]The last project tracker app you'll ever need \n\nHave a perfect project idea you're worried you might forget? \nJust run the[/yellow2] [indian_red1]'forge create'[/indian_red1] [yellow2]command and store all relevant details!!\n[/yellow2]")
    rprint("[yellow2]Never worry about forgetting your next project idea ever again!!\n[/yellow2]")

@app.command()
def create():
    "whenever project is created successfuly all three tables for that project should be created"
    name = prompt.ask("[gold3]Please enter the name of your project[/gold3]")
    rprint(f"[gold3]The name of the project you have entered is '{name}'[/gold3]")   
    # enter row addition code here
    rprint("[gold3]Proceed with project creation? [Y/n][/gold3] ", end='') 
    "[Y/n] works but [y/N] doesn't work"
    # print("[y/N]")

    while True:
        db_creation_choice = input()

        if db_creation_choice.lower() == "" or db_creation_choice.lower() == "y":
            rprint(f"[chartreuse3]Success ✨[/chartreuse3]")
            rprint(f"[chartreuse3]The name of the project is '{name.strip()}'[/chartreuse3]")
            # enter row addition code here
            break

        elif db_creation_choice.lower() == "n":
            rprint(f"[light_salmon1]Project '{name.strip()}' not created ❌[/light_salmon1]")
            rprint("[light_salmon1]Do you want to rename or abort project creation? [r/A][/light_salmon1]")
            # print("[r/A]")
            while True:
                abort_rename_choice = input()

                if abort_rename_choice.lower() == "r":
                    rprint("[light_salmon1]Please enter renamed name of the project[/light_salmon1]")
                    renamed_name = input()
                    rprint(f"[chartreuse3]Success ✨[/chartreuse3]")
                    rprint(f"[chartreuse3]Renamed name of the project is '{renamed_name.strip()}'[/chartreuse3]")

                    # enter row addition code here
                    break

                elif abort_rename_choice.lower() == ""or abort_rename_choice.lower() == "a":
                    rprint("[red3]Aborting project creation process[/red3]")
                    break

                else:
                    rprint("[red3]Did not enter 'r' or 'A'❗[/red3]")

            break
            
        else:
            rprint("[red3]Did not enter 'y' or 'N'❗[/red3]")


@app.command()
def update():
    # update row info every time there 
    name=[
        {"desc" : "Includes description of the project"},
        {"aim" : "Includes the aim of the project"},
        {"resc" : "Includes list of all the links to be used as references"},
        {"status" : "Shows the status of the project"},
        {"repo_link" : "Stores the GitHub repo link of the project if exists or else stores NULL"}
    ]
    # "desc", "aim", "resc", "status", "repo_link"
    Name=[{"name" : "Stores the name of the project"}]
    # tech_stack=[] implement this as well
    resources=[{"name" : "Stores the name of the project"},
               {"resc" : "Includes list of all the links to be used as references"}
            ]
    
    rprint("[gold3]Enter project in which you want to update details[/gold3]")
    rprint("[gold3]Please enter the table you want to update[/gold3]") # use rich prompt to ask for table name
    # once you get the table name, print all table entries and ask which entry you want to change
    
    "update contents of the table of a specific table"
    # add another parameter in the function parameter list
    # that var is project in which they want to make changes




@app.command()
def show():
    rprint("[gold3]implement logic for printing specified paramenter of project here[/gold3]")
    "will display only the names of the project names"
    "after identifying which project's details are needed, it will output relevant info"


@app.command()
def delete():
    rprint("[gold3]implement logic for deleting a project here[/gold3]")
    "used for deleting projects once they are created"

'add one more command for listing what all commands are there and a brief description'

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