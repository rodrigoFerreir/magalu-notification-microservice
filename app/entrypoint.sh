#!/bin/bash



set -e
set -u



echo Iniciando projeto...
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
        sleep 2
    done
        echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

if [ $DEBUG = 1 ]; then 
    echo "Rodando aplicação no modo de desenvolvimento"
    
    echo "Criando migrations..."
    python manage.py makemigrations --noinput

    echo "Aplicando migrations ..."
    python manage.py migrate --noinput
    
    echo "Executando testes..."
    python -m pytest
    
fi

echo Project run on port 8000 🚀
python manage.py runserver 0.0.0.0:8000


