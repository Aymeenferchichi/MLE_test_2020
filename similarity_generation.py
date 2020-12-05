def sim_gen(users,movies,ratings):

	
	genre_cols = ["Animation", "Children's", 
	       'Comedy', 'Adventure', 'Fantasy', 'Romance', 'Drama',
	       'Action', 'Crime', 'Thriller', 'Horror', 'Sci-Fi', 'Documentary', 'War',
	       'Musical', 'Mystery', 'Film-Noir', 'Western']

	genre_and_title_cols = ['title'] + genre_cols 

	similarity = movies[genre_cols].values.dot(movies[genre_cols].values.T)
	return similarity


