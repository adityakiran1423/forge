import sqlite3
import os


'creates the db once here'
'include requirements.txt and ensure set up is complete when this file is run once'
'all dependencies should be installed and Forge should be ready to go'
'ensures that forge can be run from anywhere in the terminal'


database_path="database.db"

if not os.path.exists(database_path):
    # Create the database if it doesn't exist
    # conn = sqlite3.connect(database_path,
    #                        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = sqlite3.connect(database_path)
    print("Database created successfully!")
else:
    # Connect to the existing database
    conn = sqlite3.connect(database_path)
    print("Connected to existing database.")

# conn=sqlite3.connect(database_path)
c = conn.cursor()

create_names='''create table if not exists names(
                project_name TEXT primary key, 
                project_id TEXT,
                date TEXT,
                time TEXT 
                )'''

c.execute(create_names)


create_descriptions='''create table if not exists descriptions(
                        project_name TEXT,
                        desc TEXT, 
                        status TEXT, 
                        aim TEXT,
                        FOREIGN KEY (project_name) REFERENCES names(project_name)
                    )'''

c.execute(create_descriptions)


create_resources='''create table if not exists resources(
                    resources TEXT,
                    project_name TEXT,
                    FOREIGN KEY (project_name) REFERENCES name(project_name) 
                    )'''

c.execute(create_resources)

conn.commit()