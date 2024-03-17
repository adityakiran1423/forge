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

import string
import random
from datetime import datetime

from setup import conn, c

def main():
    pass

def create_entry(p_name) -> None:
    # make new entries for all tables here
    query='''insert into names(project_name) values(?,?,?,?)'''
    p_ID=create_ID()
    date=date.today()
    c = datetime.now()
    current_time = c.strftime('%H:%M:%S')
    c.execute(query, p_name, p_ID, date, current_time)
    c.commit()
    c.close()
    confirmentry()

def confirmentry():
    query='''select * from names'''
    c.execute(query)
    c.commit()
    c.close()


def create_ID()-> str:
    char1,char2,char3= '','',''
    while char1!=char2!=char3:
        char1=random_char()
        char2=random_char()
        char3=random_char()

    rand1, rand2=0,0
    while rand1!=rand2:
        rand1=random_number()
        rand2=random_number()

    ID=char1+chr(rand1)+char2+chr(rand2)+char3

    return ID
    

def random_char()->str:
    alphabets_list=string.ascii_lowercase
    random_char = random.choice(alphabets_list)
    return random_char


def random_number()->int:
    numbers_list=['1','2','3','4','5','6','7','8','9']
    random_num = random.choice(numbers_list)
    return random_num


def edit_entry():
    # write logic for editing enrtries of all tables here
    pass

def show_entry():
    # shows aspects of project
    pass

def delete_entry():
    # add logic fot what needs to be done if project is deleted
    pass

# if __name__=="__main__":
#     main()