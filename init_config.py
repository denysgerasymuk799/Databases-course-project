from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from db_config import Config


# create main app
app = Flask(__name__)

# config for security in forms and other things
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect data base
db = SQLAlchemy(app, session_options={
    'expire_on_commit': False
})
db.init_app(app)
