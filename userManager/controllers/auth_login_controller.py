from flask_restful import Resource
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from flask_restful import Resource,reqparse
from userManager.models import user_model
from userManager import  utils

class LoginUser(Resource):
    def post(self):
        try:
            #Obtener y parsear los argumentos.
            parser = reqparse.RequestParser()
            parser.add_argument('mobile_phone', type=str, location="json")
            parser.add_argument('password', type=str, location="json")
            args = parser.parse_args()

            obj_mobile_phone = args['mobile_phone']
            obj_password = args['password']

            #Buscar si el usuario existe
            user = user_model.User.query.filter_by(mobile_phone=obj_mobile_phone).first()

            #Validar datos de inicio de sesion
            if user and check_password_hash(user.password, obj_password):

                access_token = create_access_token(identity=user.id)
                user_schema = user_model.UserSchema()
                user_data = user_schema.dump(user)
                user_data.pop('password',None)
                user_data['Token']=access_token
                user_data['Token_type']="bearer"

                return utils.make_response_ok_success('Login successful',user_data)

            else:
                return utils.make_error_validate_response('Incorrect credentials')

        except Exception as e:
                return utils.make_error_response(f'Error while logging')
