from flask_restful import Api

from controllers.user import UserRegister
from controllers.jobs import Job


router = Api()

# Routes
router.add_resource(UserRegister, '/register')
router.add_resource(Job, '/job')
