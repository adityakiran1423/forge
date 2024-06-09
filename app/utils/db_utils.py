"""
names table
    project_name
    project_id
    date
    time

descriptions table
    aim
    desc
    status
    name

resources
    name
    resource
"""


import uuid
import os
import sys

from datetime import datetime, date

parent_directory = os.path.abspath('..')
sys.path.append(parent_directory)


from setup import conn, c


def create_entry(p_name):
    p_ID = create_ID()
    today = date.today()
    dt = datetime.now()
    current_time = dt.strftime("%H:%M:%S")
    c.execute("INSERT INTO names VALUES (?, ?, ?, ?)", (p_name, p_ID, today, current_time))
    conn.commit()
    return [p_ID, today, current_time]


def create_ID() -> str:
    return str(uuid.uuid4()) 


def edit_entry():
    # write logic for editing enrtries of all tables here
    pass


def show_entry() -> list:
    project_list = []
    creation_time_list = []
    creation_date_list = []
    projectid_list = []

    query = """SELECT project_name FROM names"""
    c.execute(query)
    results = c.fetchall()  
    for row in results:
        project_list.append(row[0])

    query = """SELECT time FROM names"""
    c.execute(query)
    results = c.fetchall()
    for time in results:
        creation_time_list.append(time[0])

    query = """SELECT date FROM names"""
    c.execute(query)
    results = c.fetchall()
    for date in results:
        creation_date_list.append(date[0])

    query = """SELECT project_id FROM names"""
    c.execute(query)
    results = c.fetchall()
    for id in results:
        projectid_list.append(date[0])

    conn.commit()

    return project_list, projectid_list, creation_time_list, creation_date_list


def delete_entry(project_to_be_deleted, project_id, project_id_list) -> bool:
    if project_id in project_id_list:
        # write the code to delete it
        # if project present drop all info about it from all tables
        params=(project_id,)
        c.execute("DELETE FROM name WHERE project_id = ?", params)
        c.execute("DELETE FROM description WHERE project_id = ?", params)
        c.execute("DELETE FROM resources WHERE project_id = ?", params)     
    else:
        return False

def update_entry():
    # add logic for what needs to be done whrn the user wants to update project details
    pass
