import os

class Config():
    # путь ло директории с результатами работы default='result'
    OS_PATH_RESULT = 'result'
    # путь ло директории с логами default='logs'
    OS_PATH_LOG = 'logs'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

