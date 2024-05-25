import sqlite3
import os


database_path = "database.db"
db_creation_status = 0

if not os.path.exists(database_path):
    conn = sqlite3.connect(database_path)
    db_creation_status = 1
    # print("Database created successfully!")
else:
    conn = sqlite3.connect(database_path)
    # print("Connected to existing database.")

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
