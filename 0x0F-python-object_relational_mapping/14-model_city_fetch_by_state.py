#!/usr/bin/python3
""" A Script that lists all cities by state
from the database hbtn_0e_0_usa"""


def main():
    """create a connection and get all cities"""
    import sys
    from model_state import State
    from model_city import City
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

    query = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    main()
