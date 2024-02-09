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
'''

import sqlite3
def main():
    connection = sqlite3.connect("forge.db")

    cursor = connection.cursor()

if __name__=="__main__":
    main()