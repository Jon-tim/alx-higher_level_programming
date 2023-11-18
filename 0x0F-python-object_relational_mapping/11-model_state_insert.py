#!/usr/bin/python3
"""a script that adds the State objects "Louisiana"
to the database hbtn_0e_6_usa"""


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

    # Create an object: new data to add to the database
    newState = State(name='Louisiana')

    # Add the object to the session
    session.add(newState)

    # Commit to save the object in the database
    session.commit()

    print(newState.id)

    session.close()


if __name__ == "__main__":
    main()
