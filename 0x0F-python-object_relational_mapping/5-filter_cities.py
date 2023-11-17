#!/usr/bin/python3
"""A script that lists all states with a name starting
with N (uppercase) from the database"""


def main():
    """create a connection and get all states with 'N'"""
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
    query = """SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
                   FROM cities
                   JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC;"""
    cursor.execute(query, (state,))

    rows = cursor.fetchone()[0]
    print(rows)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
