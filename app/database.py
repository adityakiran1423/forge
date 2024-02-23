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


def make_new_entry():
    # make new entries for all tables here
    pass

def edit_entry():
    # write logic for editing enrtries of all tables here
    # add logic for clearing of the entry as well
    pass

def delete_project():
    # add logic fot what needs to be done if project is deleted
    # delete from all tables
    pass

# if __name__=="__main__":
#     main()