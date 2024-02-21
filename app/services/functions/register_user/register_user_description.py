register_user_function = {
    "name": "register_user",
    "description": "Enregistre un utilisateur dans l'application via l'API en envoyant une demande POST à l'URL "
                   "spécifiée. Prend en entrée les informations de l'utilisateur telles que le nom d'utilisateur, "
                   "l'email et le mot de passe.",
    "parameters": {
        "type": "object",
        "properties": {
            "username": {"type": "string", "description": "Le nom d'utilisateur pour l'inscription"},
            "email": {"type": "string", "description": "L'adresse email de l'utilisateur"},
            "password": {"type": "string", "description": "Le mot de passe pour l'inscription"}
        },
        "required": ["username", "email", "password"]
    }
}
