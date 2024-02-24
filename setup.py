import sqlite3
import os


'creates the db once here'
'include requirements.txt and ensure set up is complete when this file is run once'
'all dependencies should be installed and Forge should be ready to go'

database_path="database.db"

if not os.path.exists(database_path):
    # Create the database if it doesn't exist
    conn = sqlite3.connect(database_path,
                           detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    print("Database created successfully!")
else:
    # Connect to the existing database
    conn = sqlite3.connect(database_path)
    print("Connected to existing database.")

c = conn.cursor()

create_names='''create table if not exists names(
                project_name primary key TEXT, 
                project_id TEXT, 
                time_stamp TIMESTAMP
                )'''
c.execute(create_names)

create_descriptions='''create table if not exists descriptions(
                        project_name TEXT,
                        desc TEXT, 
                        status TEXT, 
                        aim TEXT
                        FOREIGN KEY (project_name) REFERENCES names(project_name)
                    )'''
c.execute(create_descriptions)

create_resources='''create table if not exists resources(
                    resources TEXT,
                    project_name TEXT,
                    FOREIGN KEY (project_name) REFERENCES name(project_name) 
                    )'''
c.execute(create_resources)