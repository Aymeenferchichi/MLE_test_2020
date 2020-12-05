import sys
import pandas as pd
from loading_data import loadd
from similarity_generation import sim_gen
from most_similar import get_most_similar
from content_based_filtering.helpers.movies import get_movie_id, get_movie_name, get_movie_year

def get_recommendations(user_id):
    top_movies = ratings[ratings['user_id'] == user_id].sort_values(by='rating', ascending=False).head(3)['movie_id']
    index=['movie_id', 'title', 'similarity']

    most_similars = []
    for top_movie in top_movies:
        most_similars += get_most_similar(movies,similarity, get_movie_name(movies, top_movie), get_movie_year(movies, top_movie))

    return print(pd.DataFrame(most_similars, columns=index).drop_duplicates().sort_values(by='similarity', ascending=False).head(5))

if __name__=="__main__":
	users,movies,ratings=loadd()
	similarity=sim_gen(users,movies,ratings)
	get_recommendations(int(sys.argv[1]))



