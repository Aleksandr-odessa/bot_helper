import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(message)s- %(module)s',
        },
        'detailed': {
            'format': '%(asctime)s - %(module)s - %(lineno)d - %(message)s',
        },
        'simple': {
            'format': '%(asctime)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
        "file_error": {
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'formatter': 'detailed',
            'delay': 'True',
        },
        "file_info": {
            'class': 'logging.FileHandler',
            'filename': 'info.log',
            'formatter': 'simple',
            'delay': 'True',
        }
    },
    'loggers': {
        'log_error': {
            'handlers': ['file_error'],
            'propagate': False,
            'level': 'ERROR',
        },
       'log_debug': {
                'handlers': ['console'],
                'propagate': False,
                'level': 'DEBUG',
       },
       'log_info': {
            'handlers': ['file_info'],
           'propagate': False,
           'level': 'INFO'
       },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)