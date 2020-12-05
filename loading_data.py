import pandas as pd

def loadd():
	users = pd.read_csv("data/users.csv")
	movies = pd.read_csv("data/movies.csv")
	ratings = pd.read_csv("data/ratings.csv")
	return users,movies,ratings



