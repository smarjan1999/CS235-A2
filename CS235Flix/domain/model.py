import csv
from datetime import datetime


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Director):
            return False
        return other.__director_full_name == self.__director_full_name

    def __lt__(self, other):
        if self.__director_full_name is None and other.__director_full_name is not None:
            return "None" < other.__director_full_name
        elif other.__director_full_name is None and self.__director_full_name is not None:
            return self.__director_full_name < "None"
        elif self.__director_full_name is not None and other.__director_full_name is not None:
            return self.__director_full_name < other.__director_full_name
        else:
            return "None" < "None"

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        return other.__genre_name == self.__genre_name

    def __lt__(self, other):
        if self.__genre_name is None and other.__genre_name is not None:
            return "None" < other.__genre_name
        elif other.__genre_name is None and self.__genre_name is not None:
            return self.__genre_name < "None"
        elif self.__genre_name is not None and other.__genre_name is not None:
            return self.__genre_name < other.__genre_name
        else:
            return "None" < "None"

    def __hash__(self):
        return hash(self.__genre_name)


class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__actor_colleague = list()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def actor_colleague(self) -> list:
        return self.__actor_colleague

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return other.__actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        if self.__actor_full_name is None and other.__actor_full_name is not None:
            return "None" < other.__actor_full_name
        elif other.__actor_full_name is None and self.__actor_full_name is not None:
            return self.__actor_full_name < "None"
        elif self.__actor_full_name is not None and other.__actor_full_name is not None:
            return self.__actor_full_name < other.__actor_full_name
        else:
            return "None" < "None"

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if not isinstance(colleague, Actor):
            raise Exception("Only Actors can be added as colleagues")
        self.__actor_colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if not isinstance(colleague, Actor):
            return False
        else:
            return colleague in self.__actor_colleague


class Movie:

    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if year < 1900 or type(year) is not int:
            self.__release_year = None
        else:
            self.__release_year = year
        self.__rank = None
        self.__description = ""
        self.__director = Director("")
        self.__actors = list()
        self.__genres = list()
        self.__runtime_minutes = 0
        self.__rating = None

    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def description(self) -> str:
        return self.__description

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @property
    def rating(self) -> float:
        return self.__rating

    @title.setter
    def title(self, t):
        if t == "" or type(t) is not str:
            self.__title = None
        else:
            self.__title = t.strip()

    @rank.setter
    def rank(self, r):
        if type(r) is not int:
            self.__rank = None
        else:
            self.__rank = r

    @description.setter
    def description(self, d):
        if type(d) is not str:
            self.__title = ""
        else:
            self.__description = d.strip()

    @director.setter
    def director(self, d):
        if not isinstance(d, Director):
            raise Exception("There can only be one Director per Movie")
        self.__director = d

    @actors.setter
    def actors(self, a):
        if not isinstance(a, list):
            raise Exception("Needs to be a list of actor(s)")
        self.__actors = a

    @genres.setter
    def genres(self, g):
        if not isinstance(g, list):
            raise Exception("Needs to be a list of genre(s)")
        self.__genres = g

    @runtime_minutes.setter
    def runtime_minutes(self, rm):
        if rm < 1:
            raise ValueError("Only positive numbers can be assigned to runtime minutes")
        else:
            self.__runtime_minutes = rm

    @rating.setter
    def rating(self, r):
        if type(r) is not float:
            if type(r) is int:
                self.__rating = float(r)
            else:
                self.__rating = None
        else:
            self.__rating = r

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return (other.__title == self.__title and
                other.__release_year == self.__release_year)

    def __lt__(self, other):
        return (("None" if self.__title is None else self.__title,
                 "None" if self.__release_year is None else self.__release_year)
                <
                ("None" if other.__title is None else other.__title,
                 "None" if other.__release_year is None else other.__release_year))

    def __hash__(self):
        return hash(self.__title + str(self.__release_year))


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    @property
    def dataset_of_movies(self) -> list:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> set:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> set:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            i = 0
            for row in movie_file_reader:
                # reading from csv
                movie_rank = int(row['Rank'].strip())
                title = row['Title']
                genres = row['Genre'].split(',')
                movie_description = row['Description'].strip()
                director = row['Director'].strip()
                actors = row['Actors'].split(',')
                year = int(row['Year'].strip())
                runtime = int(row['Runtime (Minutes)'].strip())
                movie_rating = float(row['Rating'].strip()) if row['Rating'].strip() != 'N/A' else row['Rating'].strip()

                # assigning to respective objects
                movie_director = Director(director)
                movie_genres = list()
                for g in genres:
                    genre = g.strip()
                    movie_genres.append(Genre(genre))
                movie_actors = list()
                for a in actors:
                    actor = a.strip()
                    movie_actors.append(Actor(actor))

                # assigning to respective datasets
                self.__dataset_of_movies.append(Movie(title, year))
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].rank = movie_rank
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].genres = movie_genres
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].description = movie_description
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].director = movie_director
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].actors = movie_actors
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].runtime_minutes = runtime
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].rating = movie_rating

                for a in movie_actors:
                    self.__dataset_of_actors.add(a)
                self.__dataset_of_directors.add(movie_director)
                for g in movie_genres:
                    self.__dataset_of_genres.add(g)
                i += 1


class Review:

    def __init__(self, movie: Movie, txt: str, rating: int):
        if type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie
        if type(txt) is not str:
            self.__review_text = None
        else:
            self.__review_text = txt.strip()
        if rating < 1 or rating > 10 or type(rating) is not int:
            self.__rating = None
        else:
            self.__rating = rating
        self.__timestamp = datetime.now()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__review_text}, {self.__rating}, {self.__timestamp}>"

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return (other.__movie == self.__movie and
                other.__review_text == self.__review_text and
                other.__rating == self.__rating and
                other.__timestamp == self.__timestamp)


class User:

    def __init__(self, username: str, password: str):
        if username == "" or type(username) is not str:
            self.__user_name = None
        else:
            self.__user_name = username.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__watched_movies = list()
        self.__reviews = list()

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.__user_name == self.__user_name

    def __lt__(self, other):
        return (("None" if self.__user_name is None else self.__user_name)
                <
                ("None" if other.__user_name is None else other.__user_name))

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if not isinstance(movie, Movie):
            raise Exception("Only Movies can be added")
        self.__watched_movies.append(movie)

    def add_review(self, review):
        if not isinstance(review, Review):
            raise Exception("Only Reviews can be added")
        self.__reviews.append(review)


class WatchList:

    def __init__(self, user: User, watchlist_name: str):
        if not isinstance(user, User):
            raise Exception("Invalid User")
        else:
            self.__watchlist_owner = user
        if type(watchlist_name) is not str or watchlist_name == "":
            self.__watchlist_name = "New Watchlist"
        else:
            self.__watchlist_name = watchlist_name.strip()
        self.__watchlist = list()

    @property
    def watchlist(self):
        return self.__watchlist

    @property
    def watchlist_owner(self):
        return self.__watchlist_owner

    @property
    def watchlist_name(self):
        return self.__watchlist_name

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__watchlist):
            result = self.__watchlist[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration

    def add_movie(self, movie):
        if not isinstance(movie, Movie):
            raise Exception("Only Movies can be added to the watchlist")
        elif movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if not isinstance(movie, Movie):
            raise Exception("Only Movies can be removed from the watchlist")
        elif movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if not isinstance(index, int):
            return None
        elif index < 0 or index > (len(self.__watchlist) - 1):
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) == 0:
            return None
        else:
            return self.__watchlist[0]

    def clear_watchlist(self):
        self.__watchlist.clear()

    def share_watchlist(self, user):
        if not isinstance(user, User):
            raise Exception("A valid User is required")
        else:
            new_watchlist = WatchList(user, "")
            for movie in self.__watchlist:
                new_watchlist.add_movie(movie)
            return new_watchlist

    def sort_watchlist_by_title(self):
        def get_movie_title(movie):
            return movie.title
        return sorted(self.__watchlist, key=get_movie_title)

    def sort_watchlist_by_year(self):
        def get_movie_year(movie):
            return movie.release_year
        return sorted(self.__watchlist, key=get_movie_year)

    def sort_watchlist_by_runtime(self):
        def get_movie_runtime(movie):
            return movie.runtime_minutes
        return sorted(self.__watchlist, key=get_movie_runtime)

    def change_watchlist_name(self, new_name):
        if isinstance(new_name, str) or new_name != "":
            self.__watchlist_name = new_name

    def get_recommendations(self, filename):
        if not isinstance(filename, str):
            raise Exception("Invalid filename")
        elif len(self.__watchlist) == 0:
            raise Exception("No new recommendations")
        else:
            new_watchlist = WatchList(self.watchlist_owner, "Movie Recommendations")
            movie_file_reader = MovieFileCSVReader(filename)
            movie_file_reader.read_csv_file()
            for new_movie in movie_file_reader.dataset_of_movies:
                for current_movie in self.__watchlist:
                    if sorted(new_movie.genres) == sorted(current_movie.genres):
                        new_watchlist.add_movie(new_movie)
            return new_watchlist


class ModelException(Exception):
    pass
