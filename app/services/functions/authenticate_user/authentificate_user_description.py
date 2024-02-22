authenticate_user_function = {
    "name": "authenticate_user",
    "description": "Authentifie un utilisateur dans l'application via l'API. Envoie une requête POST avec "
                   "l'identifiant et le mot de passe de l'utilisateur et retourne une réponse de l'API. Cette requête "
                   "retourne un objet contenant 'jwt' et 'user'",
    "parameters": {
        "type": "object",
        "properties": {
            "identifier": {"type": "string", "description": "L'identifiant de l'utilisateur qui est sont addresse "
                                                            "email "},
            "password": {"type": "string", "description": "Le mot de passe de l'utilisateur"}
        },
        "required": ["identifier", "password"]
    },
}
