import requests


def create_workout(exercise, rep, date, weight, user_id, token):
    url = "http://localhost:1337/api/workouts"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "data": {
            "exercise": exercise,
            "rep": rep,
            "date": date,
            "weight": weight,
            "users_permissions_user": user_id
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
