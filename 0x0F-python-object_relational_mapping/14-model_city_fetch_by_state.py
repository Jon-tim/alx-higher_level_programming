#!/usr/bin/python3

""" A Script that lists all cities by state
from the database hbtn_0e_0_usa"""


def main():
    """create a connection and get all states"""
    import MySQLdb
    import sys
    from model_state import Base, State

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host=host, user=user, passwd=pswd, db=db, port=port)
    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN {}
                   ON cities.state_id = states.id
                   ORDER BY cities.id ASC;""".format(State.__table__.name)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print('{}: ({}) {}'.format(
            row[2], row[0], row[1]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
