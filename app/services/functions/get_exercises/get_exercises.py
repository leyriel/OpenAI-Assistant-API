import requests


def get_exercises():
    url = "http://localhost:1337/api/exercises"
    response = requests.get(url)

    return response.json()
