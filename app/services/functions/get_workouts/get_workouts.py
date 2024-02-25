import requests
import json


from app.services.functions.get_user_info.get_user_info import get_user_info


def get_workouts(token):
    response = get_user_info(token, serialized_response=False)
    raw_content = response.text
    user = json.loads(raw_content)

    url = f"http://localhost:1337/api/workouts?filters[users_permissions_user][id][$eq]={user['id']}&populate=exercise"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()
