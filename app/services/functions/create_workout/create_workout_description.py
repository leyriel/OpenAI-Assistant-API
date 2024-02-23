create_workout_function = {
    "name": "create_workout",
    "description": "Crée un nouvel enregistrement de workout dans l'application via l'API avec authentification. "
                   "Nécessite un token d'autorisation valide obtenu après l'authentification de l'utilisateur.",
    "parameters": {
        "type": "object",
        "properties": {
            "exercise": {"type": "string", "description": "Identifiant de l'exercice à récupérer via l'api avec get_exercices"},
            "rep": {"type": "integer", "description": "Nombre de répétitions"},
            "date": {"type": "string", "description": "Date et heure de l'exercice au format ISO 8601"},
            "weight": {"type": "number", "description": "Poids utilisé pour l'exercice"},
            "users_permissions_user": {"type": "string", "description": "Identifiant ou nom de l'utilisateur"},
            "token": {"type": "string", "description": "Token d'autorisation Bearer pour l'accès à l'API"}
        },
        "required": ["exercise", "rep", "date", "weight", "users_permissions_user", "token"]
    },
}
