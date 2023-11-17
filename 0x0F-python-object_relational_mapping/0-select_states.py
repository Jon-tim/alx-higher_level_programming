#!/usr/bin/python3

""" A Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

host = "localhost"
port = 3306
user = sys.argv[1]
pswd = sys.argv[2]
db = sys.argv[3]


def main():
    """create a connection and get all states"""
    db = MySQLdb.connect(host=host, user=user, passwd=pswd, db=db, port=port)
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states
    ORDER BY states.id asc;""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
