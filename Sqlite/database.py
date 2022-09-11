# ------------< import sqlite3 >------------
import sqlite3 as sq
# --------< make connection to db >---------
connect = sq.connect('user.db')
# ----------< creating a cursor >-----------
c = connect.cursor()

# ----------< the sqlite3 datatypes >---------------------------|
#   [1] NULL           -----> for not exist                     |
#   [2] INTEGER        -----> for integer numbers [0-9]         |
#   [3] REAL           -----> for decimal numbers <float>       |   
#   [4] TEXT           -----> for string and text               |
#   [5] BLOB           -----> for files , img , audio and video |    
# --------------------------------------------------------------|


# ---------------------< Creating a table >----------------------|
#                                                                |
# c.execute("""                                                  |
#           CREATE TABLE Users (                                 |
#               first_name text,                                 | 
#               last_name text,                                  | 
#               email text,                                      | 
#               job text                                         |     
#           )""")                                                |
#                                                                | 
#----------------------------------------------------------------|                                                  


# --------------< Insert a Tuble Data into Table >---------------|
#                                                                | 
# c.execute("INSERT INTO Users VALUES('Karim',                   | 
#                                     'Aboelazm',                | 
#                                     'karim@gmail.com',         |  
#                                     'engineer')")              |  
#                                                                |
# ---------------------------------------------------------------| 



# ------------< Insert Many Tuble Data into Table >--------------|
#                                                                | 
# many_users = [('Sarah','Mohamed','sarah@gmail.com','student'), |
#               ('Manar','Mohamed','manar@gmail.com','doctor'),  | 
#               ('Abdo','Ahmed','body@gmail.com','student'),     | 
#               ('Yasin','Ahmed','yassin@gmail.com','child')]    | 
#                                                                | 
#                                                                |  
# c.executemany("INSERT INTO Users VALUES (?,?,?,?)", many_users)|  
#                                                                | 
# ---------------------------------------------------------------|

c.execute("SELECT * FROM Users WHERE job = 'engineer' ")

all_records = c.fetchall()
one_record = c.fetchone()
many_records = c.fetchmany()
print(all_records)

connect.commit()
connect.close()


