DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '../ndov-in-a-box.sqlite3',                      # Or path to database file if using sqlite3.
    }
}

INTERNAL_IPS = ('127.0.0.1', '10.0.1.1')

MEDIA_ROOT = '/home/joel/ndov'