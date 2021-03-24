import time

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from utils.base import Base


class SQLBackend(object):
    """ SQLBackend manages the database connection, sessions and bootstraping. """

    def __init__(self, connection_string):
        self.engine = None
        self.Session = sessionmaker(autocommit=False, expire_on_commit=False)
        self.setup_session(connection_string)

    def setup_session(self, connection_string=None):
        """ Setup the engine and session. If the engine is already setup, then return. """

        # TODO : Mention what is an engine
        if self.engine:
            return

        # TODO : Mention what does create_engine do
        self.engine = create_engine(connection_string, echo=False,
                                    pool_recycle=3600)

        # The Session object is used as the interface to the database.
        self.Session.configure(bind=self.engine)

    def bootstrap(self):
        """ Bootstraping creates database and tables.
        Assumes no databases have been setup.
        Retries until connection is established. """

        connection = None

        for i in range(2):
            try:
                connection = self.engine.connect()
            except:
                print("DB is probably not up yet, Retrying ...")
                time.sleep(i * 5)
                continue

        if not connection:
            raise Exception("Couldn't connect to DB even after retries!")

        # TODO : Mention what does create_all do
        Base.metadata.create_all(bind=self.engine)
        connection.close()
