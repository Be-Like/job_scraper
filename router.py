from flask_restful import Api

from controllers.user import UserRegister


router = Api()

# Routes
router.add_resource(UserRegister, '/register')
