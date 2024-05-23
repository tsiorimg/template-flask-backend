FROM python:3.11-slim

# Installer les dépendances système nécessaires pour psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev

WORKDIR /app

# Copier uniquement requirements.txt pour tirer parti du cache Docker
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get install -y iputils-ping

# Copier le reste des fichiers
COPY . .

CMD ["python", "run.py"]
