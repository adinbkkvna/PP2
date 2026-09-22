movies = [
{"name": "Usual Suspects", "imdb": 7.0,"category": "Thriller"},
{"name": "Hitman","imdb": 6.3,"category": "Action"},
{"name": "Dark Knight","imdb": 9.0,"category": "Adventure"},
{"name": "The Help","imdb": 8.0,"category": "Drama"},
{"name": "The Choice","imdb": 6.2,"category": "Romance"},
{"name": "Colonia","imdb": 7.4,"category": "Romance"},
{"name": "Love","imdb": 6.0,"category": "Romance"},
{"name": "Bride Wars","imdb": 5.4,"category": "Romance"},
{"name": "AlphaJet","imdb": 3.2,"category": "War"},
{"name": "Ringing Crime","imdb": 4.0,"category": "Crime"},
{"name": "Joking muck","imdb": 7.2,"category": "Comedy"},
{"name": "What is the name","imdb": 9.2,"category": "Suspense"},
{"name": "Detective","imdb": 7.0,"category": "Suspense"},
{"name": "Exam","imdb": 4.2,"category": "Thriller"},
{"name": "We Two","imdb": 7.2,"category": "Romance"}
]

def is_good_movie(movie):
    return movie ["imdb"]>5.5
print(is_good_movie(movies[0]))

def get_good_movies(movie_list):
    good_movies = []
    for movie in movie_list:
        if movie["imdb"] > 5.5:
            good_movies.append(movie)

    return good_movies

good_movies = get_good_movies(movies)
for movie in good_movies:
    print(movie["name"])


def get_movies_by_category(movie_list, category):
    category_movies = []
    for movie in movie_list:
        if movie["category"].lower() == category.lower():
            category_movies.append(movie)
    return category_movies



romance_movies = get_movies_by_category(movies, "Romance")
for movie in romance_movies:
    print(movie["name"])




# Here is a function that calculates the average IMDB score.
def average_imdb(movie_list):
    total_score = 0

    for movie in movie_list:
        total_score += movie["imdb"]

    return total_score / len(movie_list)


def category_average_imdb(movie_list, category):
    category_movies = get_movies_by_category(movie_list, category)

    return average_imdb(category_movies)
result = category_average_imdb(movies, "Romance")

print("Romance average IMDB:", result)