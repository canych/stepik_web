﻿# $ gunicorn -c /absolute/path/to/this/file

CONFIG = {
    'working_dir': '/home/box/web/ask',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=2',
        '--timeout=60',
        'ask.wsgi',
    ),
}