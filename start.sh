gunicorn youerbackend.wsgi \
        --name youer_django \
        --max-requests 2000 \
        --max-requests-jitter 500 \
        --access-logfile ./logs/access.log \
        --error-logfile ./logs/error.log \
        --bind 0.0.0.0:8000 & 
         
