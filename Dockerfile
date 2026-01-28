# 1. Utiliser une image légère de Python
FROM python:3.9-slim

# 2. Définir le répertoire de travail dans le conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier le reste du code source
COPY . .

# 5. Exposer le port sur lequel l'API tourne
EXPOSE 5000

# 6. Lancer l'application
CMD ["python", "app.py"]