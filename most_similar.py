from content_based_filtering.helpers.movies import get_movie_id, get_movie_name, get_movie_year

def get_most_similar(movies,similarity, movie_name, year=None, top=10):
    index_movie = get_movie_id(movies, movie_name, year)
    best = similarity[index_movie].argsort()[::-1]
    return [(ind, get_movie_name(movies, ind), similarity[index_movie, ind]) for ind in best[:top] if ind != index_movie]
