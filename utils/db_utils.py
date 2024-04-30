'''
new tables (updated)

*names table
    project_name
    project_id
    date_of_creation
    time_of_creation

*descriptions table
    aim
    desc
    status
    name

*resources
    name
    resource
'''


import uuid

from datetime import datetime, date
# from datetime import date

from app.setup import conn, c

def main():
    pass

def create_entry(p_name):
    p_ID=create_ID()
    today=date.today()
    dt = datetime.now()

    current_time = dt.strftime('%H:%M:%S')

    c.execute("INSERT INTO names VALUES (?, ?, ?, ?)", (p_name, p_ID, today, current_time))
    conn.commit()

    return [p_ID,today, current_time]


def create_ID()-> str:
    ID = str(uuid.uuid4())
    return ID


def edit_entry():
    # write logic for editing enrtries of all tables here
    pass

def show_entry():
    # shows aspects of project
    query='''SELECT project_name FROM names'''
    c.execute(query)

def delete_entry():
    # add logic fot what needs to be done if project is deleted
    pass

# if __name__=="__main__":
#     main()

# def confirmentry():
#     query='''SELECT project_name FROM names ORDER BY project_name DESC LIMIT 1'''

#     c.execute(query)
#     rows = c.fetchall()

#     if rows:
#             for row in rows:
#                 print(row)
#     else:
#         print("logic failure")

#     conn.commit()