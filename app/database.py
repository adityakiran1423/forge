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

from setup import conn, c

def main():
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


def create_ID()-> str:
    """
    generate a random number, if it is divisible by 2, set flag to true, else false
    if true, id starts with a letter, alternating with 
    """


def create_entry(p_name) -> None:
    # make new entries for all tables here
    query='''insert into names(project_name) values(?)'''
    c.execute(query, p_name)
    pass

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