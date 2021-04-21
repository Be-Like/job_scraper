import os

from dotenv import load_dotenv
from flask import Flask
# from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt import JWT

from db import db
from router import router
from security import authenticate, identity

load_dotenv()


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
  db.create_all()

jwt = JWT(app, authenticate, identity)

db.init_app(app)
router.init_app(app)


# migrate = Migrate()
# migrate.init_app(app, db)


print(os.environ['FLASK_APP'])


if __name__ == '__main__':
  app.run()
