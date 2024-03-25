# Utilisez une image de base officielle Python 3.10
FROM python:3.10

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier des dépendances dans le conteneur
COPY requirements.txt ./

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste du code source de l'application dans le conteneur
COPY . .

# Définissez la commande pour exécuter l'application via Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
