#!/usr/bin/python3
"""A script that lists all cities in a states
from a state given from the database"""


def main():
    """starting point"""
    import MySQLdb
    import sys

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host=host, user=user, passwd=pswd, db=db, port=port)
    cursor = db.cursor()
    query = """SELECT cities.name
                   FROM cities
                   JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = {}
                   ORDER BY cities.id ASC;""".format(state)
    cursor.execute(query)

    rows = cursor.fetchall()
    if rows:
        result = ', '.join(row[0] for row in rows)
        print(result)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
