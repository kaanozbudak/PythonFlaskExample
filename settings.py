import os

basedir = os.path.abspath(os.path.dirname(__file__))

# print basedir


class DevelopmentConfig():
    SERVER_NAME = 'localhost:5000'
    TESTING = True
    host = "localhost",
    user = "root",
    passwd = ""
