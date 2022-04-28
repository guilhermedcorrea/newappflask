from flask import Blueprint

api_routes = Blueprint('api_routes', __name__)


@api_routes.route("/aaa",methods=['GET','POST'])
def apifull():
    return 'olaaa'