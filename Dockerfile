FROM python:3.11-slim

# Installer les dépendances système nécessaires pour psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    iputils-ping

WORKDIR /app

# Copier uniquement requirements.txt pour tirer parti du cache Docker
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Copier le reste des fichiers
COPY . .

CMD ["gunicorn", "-c", "gunicorn_config.py", "run:app"]