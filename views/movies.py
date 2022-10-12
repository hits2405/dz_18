# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service
import flask
from flask_restx import Resource, Namespace
from dao.model.shema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MovieView(Resource):
    # GET /movie — получить все фильмы.
    def get(self):
        return movie_schema.dump(movie_service.get_movie()), 200

    # GET /movie — добавить фильм.
    def post(self):
        if movie_service.get_create_movies(**flask.request.json):
            return "Add films", 200
        else:
            return "Error add films"


@movie_ns.route("/<int:uid>")
class MoviesViews(Resource):
    # GET /movie/3 — получить фильм по ID.
    def get(self, uid):
        args = flask.request.args
        if len(args):
            return movie_schema.dump(movie_service.get_movie_by_kwargs(**args))

        return movie_schema.dump([movie_service.get_movie_by_id(uid)]), 200


@movie_ns.route("/<int:uid>")
class MoviesViews(Resource):
    # GET /movie/3 — получить фильм по ID жанра.
    def get(self, uid):
        return movie_schema.dump([movie_service.get_genre_by_id(uid)]), 200

    # put /movie/3 — обновить/редактировать фильм по ИД.
    def put(self, id):
        if movie_service.update_movies(id=id, **flask.request.json):
            return "Add upgrade films", 200
        else:
            return "Error add upgrade films"

    # put /movie/3 — удалить фильм по ИД
    def delete(self, uid):
        if movie_service.delete_movie(uid):
            return "Delete films", 200
        else:
            return "Error delete films"
