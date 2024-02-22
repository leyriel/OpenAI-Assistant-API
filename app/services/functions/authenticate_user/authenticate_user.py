import requests


def authenticate_user(identifier, password):
    url = "http://localhost:1337/api/auth/local"
    data = {
        "identifier": identifier,
        "password": password
    }
    response = requests.post(url, json=data)
    return response.json()
