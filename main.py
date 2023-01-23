import pandas as pd
import matplotlib.pyplot as plt

df_titles = pd.read_csv("titles.csv")
df_credits = pd.read_csv("credits.csv")

def show_movies_hist(df_titles):
    movies = df_titles[df_titles["type"] == 'MOVIE']
    movie_scores = movies['imdb_score']
    plt.hist(movie_scores, bins = 40)
    plt.show()

    print(f"The best movie {movies[movies['imdb_score'] == movies['imdb_score'].max()]['title']}")

def show_shows_hist(df_titles):
    shows = df_titles[df_titles["type"] == 'SHOW']
    shows_scores = shows['imdb_score']

    plt.hist(shows_scores, bins = 40)
    plt.show()

    print(f"The best show {shows[shows['imdb_score'] == shows['imdb_score'].max()]['title']}")

def run_first_task(df_titles):
    show_movies_hist(df_titles)
    show_shows_hist(df_titles)

run_first_task(df_titles)
