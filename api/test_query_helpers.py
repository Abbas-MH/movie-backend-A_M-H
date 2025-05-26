from database import SessionLocal
from query_helpers import *

db = SessionLocal()

#movies = get_movies(db, limit=5)
#for film in movies:
    #print(f"ID : {film.movieId}, Titre : {film.title}, Genres : {film.genres}")


#rating = get_rating(db, movie_id=1, user_id=1)
#print(f"User ID : {rating.userId}, Movie ID: {rating.movieId}, Rating : {rating.rating}, Timestamp : {rating.timestamp} ")

#ratings = get_ratings(db, min_rating=3.5, limit=10, user_id=1)
#for film in ratings:
   # print(f"ID : {film.movieId}, Note : {film.rating}")


#tag = get_tag(db, user_id=2, movie_id=60756, tag_text="funny")
#print(tag)
#print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}")

n_movies = get_movie_count(db)
print(f"Nombre de films : {n_movies}")


db.close()