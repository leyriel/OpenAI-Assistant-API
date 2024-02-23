get_workouts_function = {
    "name": "get_workouts",
    "description": "Récupère une liste de workouts associés à un utilisateur spécifique de l'application via l'API. "
                   "La fonction nécessite un token d'autorisation valide et l'identifiant de l'utilisateur. Les "
                   "workouts sont filtrés pour correspondre à l'ID de l'utilisateur spécifié.",
    "parameters": {
        "type": "object",
        "properties": {
            "token": {
                "type": "string",
                "description": "Token d'autorisation Bearer pour accéder à l'API"
            },
            "user_id": {
                "type": "integer",
                "description": "Identifiant de l'utilisateur pour lequel les workouts doivent être récupérés"
            }
        },
        "required": ["token", "user_id"]
    }
}

