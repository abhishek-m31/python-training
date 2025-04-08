import sqlite3
from sqlite3 import Error

def get_connection(db_path):
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        print('Data base connection is successful')
    except Error as er:
        print(er)
    return connection


def execute_query(con, query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        print('Query executed successfully')
    except Error as er:
        print(er) 

def execute_read_query(con, query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        db_records = cursor.fetchall()
        print('Query Executed Successfully')   
        return db_records
    except Error as er:
        print(er)

def close_connection(con):
    try:
        if con:
            con.close()
            print('Connection closed successfully')
    except Error as er:
        print(er)

create_table = """CREATE TABLE IF NOT EXISTS user
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
nationality TEXT);"""

add_users = """
INSERT INTO
user (name, age, gender, nationality)
VALUES
('James', 25, 'male', 'USA'),
('Leila', 32, 'female', 'France'),
('Brigitte', 35, 'female', 'England'),
('Mike', 40, 'male', 'Denmark'),
('Elizabeth', 21, 'female', 'Canada');
"""

select_users = """SELECT * FROM user"""
 
update_user = """
UPDATE 
user
SET
age = 22
WHERE 
name = 'Mike'
"""
 
delete_user = """
DELETE from user WHERE id = 5"""
 
path = "C:\Users\SFNKDOV\Desktop\Python Training\Day_5\files\Users.sqlite"
connect = get_connection(path)
records = execute_read_query(connect, select_users)
for record in records:
    print(record)
execute_query(connect, update_user)
execute_query(connect, delete_user)

print('------------------------')
records = execute_read_query(connect, select_users)
for record in record:
    print(record)
close_connection(connect)    