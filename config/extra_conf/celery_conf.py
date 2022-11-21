CELERY_BROKER_URL = "redis://redis:6379/0"
# CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_IMPORTS = ('tasks.spam',)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
