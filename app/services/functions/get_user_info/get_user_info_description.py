get_user_infos_function = {
    "name": "get_user_info",
    "description": "Récupère les informations de l'utilisateur actuel en fonction du token d'authentification. La "
                   "requête nécessite un header 'Authorization' avec le token Bearer de l'utilisateur.",
    "parameters": {
        "type": "object",
        "properties": {
            "token": {"type": "string", "description": "Token d'autorisation Bearer de l'utilisateur"}
        },
        "required": ["token"]
    },
}
