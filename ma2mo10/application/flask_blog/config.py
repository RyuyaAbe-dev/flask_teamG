import os

SQLALCHEMY_DATABASE = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
    "user":os.getenv("DB_USER", "root"),
    "password":os.getenv("DB_PASSWORD", "mysql"),
    "host":os.getenv("DB_HOST", "localhost"),
    "database":os.getenv("DB_DATABASE", "ENSHU")
})
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
SECRET_KEY = 'kd5hew1od%kkdape3jemo@'
USERNAME = 'ma2mo10'
PASSWORD = 'hogehoge'