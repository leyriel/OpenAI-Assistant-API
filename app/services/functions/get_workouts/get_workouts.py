import requests


def get_workouts(token, user_id):
    url = f"http://localhost:1337/api/workouts?filters[users_permissions_user][id][$eq]={user_id}&populate=exercise"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

