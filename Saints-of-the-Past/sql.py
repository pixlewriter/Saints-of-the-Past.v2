import sqlite3

connection = sqlite3.connect("db.sqlite3")

crsr = connection.cursor()
sql_command = """ ALTER TABLE saints_website_entry
        ADD text STRING;"""
crsr.execute(sql_command)


connection.commit()
  
connection.close()
