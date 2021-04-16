import os

from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


load_dotenv()


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


print(os.environ['APP_SETTINGS'])


if __name__ == '__main__':
  app.run()
