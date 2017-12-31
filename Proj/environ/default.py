##########################################
#  default environment: testing
#

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'gz-cdb-5bq6jaql.sql.tencentcdb.com',
        'NAME': 'wedsvr',
        'USER': 'root',
        'PASSWORD': 'TXY#root#2018',
        'PORT': 63420,
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s | %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file_handler': {
             'level': 'DEBUG',
             'class': 'logging.handlers.TimedRotatingFileHandler',
             'filename': 'D:\\Node\\logs\\wedsvr\\logging.log',
             'formatter':'standard'
        },
    },
    'loggers': {
        'wed': {
            'handlers': ['console', 'file_handler'],
            'level': 'DEBUG',
        }
    }
}
