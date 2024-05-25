import sqlite3
import os


"creates the db once here"
"include requirements.txt and ensure set up is complete when this file is run once"
"all dependencies should be installed and Forge should be ready to go"
"ensures that forge can be run from anywhere in the terminal"


database_path = "database.db"
db_creation_status = 0

if not os.path.exists(database_path):
    # Create the database if it doesn't exist
    # conn = sqlite3.connect(database_path,
    #                        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = sqlite3.connect(database_path)
    db_creation_status = 1
    # print("Database created successfully!")
else:
    # Connect to the existing database
    conn = sqlite3.connect(database_path)
    # print("Connected to existing database.")

# conn=sqlite3.connect(database_path)
c = conn.cursor()

create_names = """create table if not exists names(
                project_name TEXT primary key, 
                project_id TEXT,
                date TEXT,
                time TEXT 
                )"""

c.execute(create_names)


create_descriptions = """create table if not exists descriptions(
                        project_id TEXT,
                        desc TEXT, 
                        status TEXT, 
                        aim TEXT,
                        FOREIGN KEY (project_id) REFERENCES names(project_id)
                    )"""

c.execute(create_descriptions)


create_resources = """create table if not exists resources(
                    resources TEXT,
                    project_id TEXT,
                    FOREIGN KEY (project_id) REFERENCES name(project_id) 
                    )"""

c.execute(create_resources)

conn.commit()
