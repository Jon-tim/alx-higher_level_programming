#!/usr/bin/python3
"""a script that changes the name of a State objects
from the database hbtn_0e_6_usa"""


def main():
    """starting point"""
    import sys
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy import create_engine
    from model_state import Base, State

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, pswd, host, port, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    # Update a data in the DB
    query = session.query(State).filter(State.id == 2).first()
    query.name = 'New Mexico'

    # Commit to save the object in the database
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
