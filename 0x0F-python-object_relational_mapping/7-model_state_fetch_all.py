#!/usr/bin/python3
"""a script that lists all State objects from the
database hbtn_0e_6_usa"""


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
    query = session.query(State).order_by(State.id).all()

    for state in query:
        print('{}: {}'.format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    main()
