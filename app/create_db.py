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

connection = sqlite3.connect("forge.db")

cursor = connection.cursor()

# cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")

cursor.execute("CREATE TABLE name (name TEXT)")

# cursor.execute("CREATE TABLE desc (name TEXT, description TEXT, aim TEXT, resources TEXT, status TEXT, gh_link TEXT)")

# cursor.execute("CREATE TABLE fish (name TEXT, frontend TEXT, backend TEXT, db TEXT, framework TEXT, api TEXT, module TEXT)")
