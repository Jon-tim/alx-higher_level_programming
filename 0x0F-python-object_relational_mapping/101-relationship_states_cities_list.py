#!/usr/bin/python3
"""a script that lists all State objects, and corresponding
City objects, contained in the database
hbtn_0e_101_usa"""


def main():
    """list all realtionships"""
    import sys
    from relationship_state import State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
        user, pswd, host, port, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)

    for state in query:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
    session.close()


if __name__ == '__main__':
    main()
