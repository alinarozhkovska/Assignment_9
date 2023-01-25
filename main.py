import pandas as pd
import matplotlib.pyplot as plt

df_titles = pd.read_csv("titles.csv")
df_credits = pd.read_csv("credits.csv")


def show_movies_hist(df_titles):
    movies = df_titles[df_titles["type"] == 'MOVIE']
    movie_scores = movies['imdb_score']
    plt.hist(movie_scores, bins=40)
    plt.show()

    print(f"The best movie:\n{movies[movies['imdb_score'] == movies['imdb_score'].max()]['title']}")


def show_shows_hist(df_titles):
    shows = df_titles[df_titles["type"] == 'SHOW']
    shows_scores = shows['imdb_score']

    plt.hist(shows_scores, bins=40)
    plt.show()

    print(f"The best show:\n{shows[shows['imdb_score'] == shows['imdb_score'].max()]['title']}")


def run_first_task(df_titles):
    show_movies_hist(df_titles)
    show_shows_hist(df_titles)


def shows_age_certification_pie(df_titles):
    shows = df_titles[df_titles["type"] == 'SHOW']
    age_certifications = shows['age_certification']
    age_certifications_names = age_certifications.value_counts().keys()
    age_certifications_values = age_certifications.value_counts().values

    plt.pie(age_certifications_values, labels=age_certifications_names)
    plt.show()


def run_second_task(df_titles):
    shows_age_certification_pie(df_titles)


def show_procents_good_movies(df_titles):
    new_films = df_titles[df_titles['release_year'] >= 2000]

    years = list(new_films['release_year'].unique())
    years.sort()

    good_movies_procents = []

    for year in years:
        movies_count = len(df_titles[df_titles['release_year'] == year])
        movies_good_rate_count = len(df_titles[(df_titles['release_year'] == year) & (df_titles['imdb_score'] >= 8)])
        procent_of_good_movies = movies_good_rate_count / (movies_count / 100)
        good_movies_procents.append(procent_of_good_movies)

    plt.plot(years, good_movies_procents)
    plt.show()

    best_procent = max(good_movies_procents)

    index_best_procents = good_movies_procents.index(best_procent)

    print(f"Best year is {years[index_best_procents]}")


def run_third_task(df_titles):
    show_procents_good_movies(df_titles)


def show_actors_good_movies(df_titles, df_credits):
    df_titles.sort_values('imdb_score', inplace=True, ascending=False)
    good_movies = df_titles[:1000]
    actors_good_movies = df_credits[df_credits['id'].isin(good_movies['id'].tolist())]
    count_movies_for_actor = actors_good_movies['name'].value_counts(sort=True)

    print('Best actor: \n', count_movies_for_actor[:10])


def run_fourth_task(df_titles, df_credits):
    show_actors_good_movies(df_titles, df_credits)


run_first_task(df_titles)
run_second_task(df_titles)
run_third_task(df_titles)
run_fourth_task(df_titles, df_credits)
