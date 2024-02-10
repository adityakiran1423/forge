'''
Make a new file for creating a database and then import it?

one dataBase, create three tables :
1. Name Table (stores the name of the projects)
    * name (primary key)
2. Description Table (stores details about the project)
    * name (foreign key)
    * description
    * aim
    * resources
    * status
    * github link
    * tech stack 
3. Tech Table (stores the tech stack of the project)
    * name (foreign key)
    * frontend
    * backend
    * database
    * web frame work 
    * apis
    * modules
4. Resources Table (stores the resource links for project)
    * name 
    * resource
'''

import sqlite3

# trying changes
# trying changes after revert

def main():
    connection = sqlite3.connect("forge.db")
    cursor = connection.cursor()
    print("executing create_db.py")

def make_table():
    # write making new table logic here
    pass

def make_new_entry():
    # make new entries for all tables here
    pass

def edit_entry():
    # write logic for editing enrtries of all tables here
    # add logic for clearing of the entry as well
    pass

def delete_project():
    # add logic fot what needs to be done if project is deleted
    # delete from all tables
    pass

# if __name__=="__main__":
#     main()