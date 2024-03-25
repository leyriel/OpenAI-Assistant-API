import requests


def get_exercises():
    url = "http://localhost:1337/api/exercises?pagination[page]=1&pagination[pageSize]=10000"
    response = requests.get(url)

    return response.json()
