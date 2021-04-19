import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from db import db

load_dotenv()


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)


print(os.environ['FLASK_APP'])

@app.before_first_request
def create_tables():
  db.create_all()


db.init_app(app)


if __name__ == '__main__':
  app.run()
