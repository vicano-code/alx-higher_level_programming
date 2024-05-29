#!/usr/bin/python3

'''
lists all cities from the database hbtn_0e_4_usa
'''
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cmd = """SELECT cities.name
             FROM cities
             INNER JOIN states ON cities.state_id=states.id
             WHERE states.name LIKE %s
             ORDER BY cities.id ASC"""
    cur.execute(cmd, (sys.argv[4],))

    print(', '.join(["{:s}".format(row[0]) for row in cur.fetchall()]))

    cur.close()
    conn.close()
