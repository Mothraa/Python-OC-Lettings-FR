# image de base
FROM python:3.12-slim

# def des variables d'environnement
# desactive la mise en buffer de stdout et stderr
ENV PYTHONUNBUFFERED=1

# install des dependances système
# on passe par apt-get dans le cas ou les lib ont des dépendances systeme
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     --no-install-recommends && \
#     rm -rf /var/lib/apt/lists/*

# on précise le répertoire de travail
WORKDIR /app

# Installation des lib python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# on copie le reste de l'app
COPY . .

# Donner les permissions d'exécution au script
RUN chmod +x /app/entrypoint.sh

# on passe sur un utilisateur non-root
RUN useradd -m appuser
RUN chown -R appuser:appuser .
USER appuser

# expose le port 8080
EXPOSE 8080

# on exec le script entrypoint.sh pour init et démarrer l'app
CMD ["sh", "entrypoint.sh"]