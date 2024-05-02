"""
new tables (updated)

*names table
    project_name
    project_id
    date
    time

*descriptions table
    aim
    desc
    status
    name

*resources
    name
    resource
"""


import uuid

from datetime import datetime, date

from app.setup import conn, c


def create_entry(p_name):
    p_ID = create_ID()
    today = date.today()
    dt = datetime.now()

    current_time = dt.strftime("%H:%M:%S")

    c.execute("INSERT INTO names VALUES (?, ?, ?, ?)", (p_name, p_ID, today, current_time))
    conn.commit()

    return [p_ID, today, current_time]


def create_ID() -> str:
    ID = str(uuid.uuid4())
    return ID


def edit_entry():
    # write logic for editing enrtries of all tables here
    pass


def show_entry():
    project_list = []
    creation_time_list = []
    creation_date_list = []

    query = """SELECT project_name FROM names"""
    c.execute(query)

    results = c.fetchall()  # fetch all results
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

    conn.commit()

    return project_list, creation_time_list, creation_date_list


def delete_entry():
    # add logic fot what needs to be done if project is deleted
    pass


# if __name__=="__main__":
#     main()
