import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "SECRET_KEY"
    host = "ec2-3-218-71-191.compute-1.amazonaws.com"
    database = "d32ujljp516vbh"
    user = "USER"
    password = "PASSWORD"

    SQLALCHEMY_DATABASE_URI = "DATEBASE_URL"
