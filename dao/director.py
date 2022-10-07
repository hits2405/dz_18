from dao.model.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_director(self):
        return self.session.query(Director).all()

    def get_director_by_id(self, uid):
        return self.session.query(Director).filter(Director.id == uid).one()
    
