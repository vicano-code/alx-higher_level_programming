#!/usr/bin/python3

'''
lists all cities from the database hbtn_0e_4_usa
'''
import sys
import MySQLdb


conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT cities.name FROM cities
            INNER JOIN states ON cities.state_id=states.id
            WHERE states.name=%s", (sys.argv[4],))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
