from movie_model import MovieModel
import requests

def MovieApi():
    url = f'''
      https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=&limit=20
    '''
    response = requests.get(url)

    responseDict = response.json() 
    movies = responseDict["title"]["rating"]["small_cover_image"]["summary"] 
    return convert_model(movies)


def convert_model(movies):
    list = []

    for movie in movies:
        movie_model = MovieModel(movie["title"], movie["rating"], movie["small_cover_image"],movie["summary"])
        list.append(movie_model)

    print(list)
    return list