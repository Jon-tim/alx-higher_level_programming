#!/usr/bin/python3
""" a script that creates the State “California”
with the City “San Francisco”
from the database hbtn_0e_100_usa"""


def main():
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State, Base
    from relationship_city import City

    host = 'localhost'
    user = sys.argv[1]
    pswd = sys.argv[2]
    port = 3306
    db = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, pswd, host, port, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    newCity = City(name="San Francisco", state=State(name="California"))
    session.add(newCity)
    session.commit()


if __name__ == '__main__':
    main()
