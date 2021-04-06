from sqlalchemy.exc import IntegrityError


def handle_session(f):
    """ Handle session for DB transactions """

    def wrapper(self, *args, **kwargs):
        session = self.Session()
        try:
            result = f(self, session, *args, **kwargs)
            return result
        except IntegrityError:
            session.rollback()
            raise Exception("Error")
        finally:
            session.expunge_all()
            session.close()
    return wrapper
