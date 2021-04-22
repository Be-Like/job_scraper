import os

from flask import Flask, jsonify
from flask_restful import Api
# from flask_jwt_extended import JWTManager

from db import db
from router import router


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


router.init_app(app)

@app.before_first_request
def create_tables():
  db.create_all()


# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(StoreList, '/stores')
# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')
# api.add_resource(UserRegister, '/register')
# api.add_resource(UserLogin, '/login')
# api.add_resource(User, '/user/<int:user_id>')
# api.add_resource(TokenRefresh, '/refresh')
# api.add_resource(UserLogout, '/logout')
db.init_app(app)

with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run(port=5000, debug=True)







# import os

# from dotenv import load_dotenv
# from flask import Flask
# from flask_migrate import Migrate
# from flask_restful import Api
# from flask_jwt import JWT

# from db import db
# from router import router
# from security import authenticate, identity

# load_dotenv()


# app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.secret_key = 'jake'

# db.init_app(app)

# # @app.before_first_request
# # def create_tables():
# with app.app_context():
#   db.create_all()

# jwt = JWT(app, authenticate, identity)

# router.init_app(app)


# migrate = Migrate()
# migrate.init_app(app, db)


# print(os.environ['FLASK_APP'])


# if __name__ == '__main__':
#   app.run()
