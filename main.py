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


def get_list_genres(g_movies, type):
    type_movie = g_movies[g_movies['type'].isin([type])]

    list_genres_movies = []
    for row in type_movie['genres'].tolist():
        list_genres_movies += row[1:-1].split(', ')
    list_genres_movies.sort()
    result = pd.DataFrame(list_genres_movies, columns=['genres'])

    return result


def show_count_genre(df_titles):
    df_titles.sort_values('imdb_score', inplace=True, ascending=False)
    good_movies = df_titles[:1000]

    get_shows = get_list_genres(good_movies, 'SHOW')
    get_movies = get_list_genres(good_movies, 'MOVIE')

    x1 = np.arange(0, 20) + 0.2
    x2 = np.arange(0, 20) - 0.2
    y1 = np.array(get_shows['genres'].value_counts(sort=False).tolist())
    y2 = np.array(get_movies['genres'].value_counts(sort=False).tolist())

    fig, ax = plt.subplots()

    ax.bar(x1, y1, width=0.4)
    ax.bar(x2, y2, width=0.4)

    fig.set_figwidth(10)
    fig.set_figheight(8)
    plt.xticks(x1 - 0.2, get_movies['genres'].unique(), rotation=90)

    plt.show()


def run_fifth_task(df_titles):
    show_count_genre(df_titles)


run_first_task(df_titles)
run_second_task(df_titles)
run_third_task(df_titles)
run_fourth_task(df_titles, df_credits)
run_fifth_task(df_titles)
