from typing import List

from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> List[DirectorDAO]:
        return self.director_dao.get_all_director()

    def get_director_by_id(self, uid):
        return self.director_dao.get_director_by_id(uid)
