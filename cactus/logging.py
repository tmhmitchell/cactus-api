"""logging - logging configuration and setup"""

import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S %z'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'cactus.app': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}


def configure():
    """Apply LOGGING_CONF config to application"""
    logging.config.dictConfig(LOGGING_CONFIG)
