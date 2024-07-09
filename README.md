# Resolvendo o Desafio Backend da Magalu usando Django:

# install dependences
`pip install -r requements.txt`

# run migrations
`python3 manage.py makemigrations`

`python3 manage.py migrate`

# run celery
`python3 -m celery -A config.celery worker -B -E -Q celery -l INFO`

# run project
`python3 manage.py runserver`

# run docker services
`docker-compose up`