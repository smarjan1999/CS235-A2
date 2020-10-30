import os
from typing import List

from werkzeug.security import generate_password_hash

from CS235Flix.adapters.repository import AbstractRepository
from CS235Flix.domain.model import Director, Genre, Actor, Movie, MovieFileCSVReader, Review, User, WatchList


class MemoryRepository(AbstractRepository):
    # Movies ordered by date, not id. id is assumed unique.

    def __init__(self):
        self.__movies_index = dict()
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = list()
        self.__dataset_of_directors = list()
        self.__dataset_of_genres = list()
        self.__users = list()
        self.__reviews = list()
        self.__dataset_of_watchlist = list()

    def add_movie(self, movie: Movie):
        self.__dataset_of_movies.append(movie)
        self.__movies_index[movie.rank] = movie

    def get_movie(self, rank: int) -> Movie:
        movie = None
        try:
            movie = self.__movies_index[rank]
        except KeyError:
            pass  # Ignore exception and return None.
        return movie

    def get_number_of_movies(self):
        return len(self.__dataset_of_movies)

    def get_first_movie(self) -> Movie:
        movie = None
        if len(self.__dataset_of_movies) > 0:
            movie = self.__dataset_of_movies[0]
        return movie

    def get_last_movie(self) -> Movie:
        movie = None
        if len(self.__dataset_of_movies) > 0:
            movie = self.__dataset_of_movies[-1]
        return movie

    def get_movies_by_rank(self, rank_list):
        ranks_list = [rank for rank in rank_list if rank in self.__movies_index]

        movies = [self.__movies_index[rank] for rank in ranks_list]
        return movies

    def get_movie_ranks_for_genre(self, genre_name: str):
        genre = next((genre for genre in self.__dataset_of_genres if genre.genre_name == genre_name), None)

        if genre is not None:
            movie_ranks = [movie.rank for movie in self.__dataset_of_movies if genre in movie.genres]
        else:
            movie_ranks = list()
        return movie_ranks

    def add_genre(self, genre: Genre):
        self.__dataset_of_genres.append(genre)

    def get_genres(self) -> List[Genre]:
        return self.__dataset_of_genres

    def add_director(self, director: Director):
        self.__dataset_of_directors.append(director)

    def get_director(self, director_name) -> Director:
        return next(
            (director for director in self.__dataset_of_directors if director.director_full_name == director_name), None)

    def add_actor(self, actor: Actor):
        self.__dataset_of_actors.append(actor)

    def get_actor(self, actor_name) -> Actor:
        return next((actor for actor in self.__dataset_of_actors if actor.actor_full_name == actor_name), None)

    def add_review(self, review: Review):
        super().add_review(review)
        self.__reviews.append(review)

    def get_reviews(self):
        return self.__reviews

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, username: str) -> User:
        return next((user for user in self.__users if user.user_name == username), None)

    def add_watchlist(self, watchlist: WatchList):
        self.__dataset_of_watchlist.append(watchlist)

    def get_watchlist(self, user: User) -> List[WatchList]:
        watchlists_list = []
        for watchlist in self.__dataset_of_watchlist:
            if watchlist.watchlist_owner == user:
                watchlists_list.append(watchlist)
        return watchlists_list


def load_movie_data(data_path: str, repo: MemoryRepository):
    data = MovieFileCSVReader(os.path.join(data_path, 'Data1000Movies.csv'))
    data.read_csv_file()

    for movie in data.dataset_of_movies:
        repo.add_movie(movie)

    for genre in data.dataset_of_genres:
        repo.add_genre(genre)

    for director in data.dataset_of_directors:
        repo.add_director(director)

    for actor in data.dataset_of_actors:
        repo.add_actor(actor)


def load_users_and_review(repo: MemoryRepository):
    review = Review(
        movie=repo.get_movie(1),
        txt='Best Movie Ever!',
        rating=10
    )
    user = User(username='smar387', password=generate_password_hash('smar387PWord'))
    user.add_review(review)
    repo.add_review(review)
    repo.add_user(user)


def load_watchlist(repo: MemoryRepository):
    movies = repo.get_movies_by_rank([1, 2, 3, 4, 5])
    watchlist = WatchList(user=repo.get_user('smar387'), watchlist_name='To-Watch')
    for movie in movies:
        watchlist.add_movie(movie)

    repo.add_watchlist(watchlist)


def populate(data_path: str, repo: MemoryRepository):
    # Load movies, genres, directors and actors into the repository.
    load_movie_data(data_path, repo)

    # Load users into the repository.
    load_users_and_review(repo)

    # Load watchlist into the repository.
    load_watchlist(repo)
