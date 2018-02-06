import sqlite3

from _config import DATABASE_PATH


with sqlite3.connect(DATABASE_PATH) as connection:
    # Gets cursor object used to execute SQL Commands

    c = connection.cursor()



    # Create the table

    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY
                AUTOINCREMENT,
                name Text NOT NULL, due_date TEXT NOT NULL, priority INTEGER
                NOT NULL,
                status INTEGER NOT NULL)""")



    # insert dummy data into the table
    c.execute(
        """INSERT INTO tasks(name, due_date, priority, status)
        VALUES("Finish this Tutorial", "03/25/2015", 10,1)"""
        )

    c.execute(
        """INSERT INTO tasks(name, due_date, priority,status)
        VALUES("Finish Real Python" , "03/25/2015", 10, 1)"""
        )
