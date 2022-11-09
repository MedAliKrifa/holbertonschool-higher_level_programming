#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys  
if __name__ == "_main_":
     db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
     curs = db.cursor()
     curs.execute("SELECT id, name FROM states ORDER BY id;")
     for t in curs.fetchall():
         print(t)

     curs.close()
     db.close()