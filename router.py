from flask_restful import Api

from controllers.user import UserRegister
from controllers.jobs import Job
from controllers.fetch_jobs import FetchJobs


router = Api()

# Routes
router.add_resource(UserRegister, '/register')
router.add_resource(Job, '/job')
router.add_resource(FetchJobs, '/fetch-jobs')
