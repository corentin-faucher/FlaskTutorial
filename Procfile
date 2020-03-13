web: flask db upgrade; flask translate compile; gunicorn flask3:theapp
worker: rq worker -u $REDIS_URL coqblog-tasks