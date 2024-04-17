from userManager import db, app, utils
from flask_restful import Resource,reqparse
from userManager.models import user_model
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required


class CreateUser(Resource):
    @jwt_required()
    def post(self):
        try:
            #Obtener y parsear los argumentos.
            parser = reqparse.RequestParser()
            parser.add_argument('first_name', type=str, location="json")
            parser.add_argument('last_name', type=str, location="json")
            parser.add_argument('date_birth', type=str, location="json")
            parser.add_argument('mobile_phone', type=str, location="json")
            parser.add_argument('email', type=str, location="json")
            parser.add_argument('password', type=str, location="json")
            parser.add_argument('address', type=str, location="json")

            args = parser.parse_args()

            #Validacion de rqueridos (agregar al dict los campos requeridos).
            required = dict(
                first_name = "Firs Name", last_name = "Last Name", date_birth = "Date Birth",
                mobile_phone = "Mobile Phone", password = "Password", address = "Address"
            )

            for key in required.keys():
                value = args[key]
                if not value or not str(value).strip():
                    return utils.make_error_validate_response(f"{required[key]} is required")

            obj_first_name= args['first_name']
            obj_last_name= args['last_name']
            obj_date_birth= args['date_birth']
            obj_mobile_phone= args['mobile_phone']
            obj_email= args['email']
            obj_password= args['password']
            obj_address= args['address']

            validate_mobile = user_model.User.query.filter_by(mobile_phone=obj_mobile_phone).first()

            #validar que el numero de movil ya este registrado
            if validate_mobile:
                    return utils.make_error_validate_response(f"Phone number already registered.")

            hashed_password = generate_password_hash(obj_password)

            #Crear Usuario
            user = user_model.User(
            first_name = obj_first_name,
            last_name = obj_last_name,
            date_birth = obj_date_birth,
            address = obj_address,
            password = hashed_password,
            mobile_phone = obj_mobile_phone,
            email = obj_email
            )
            db.session.add(user)
            db.session.flush()
            db.session.commit()

            #Serializacion y respuesta
            user_schema = user_model.UserSchema()
            user_data = user_schema.dump(user)

            return utils.make_response_create_success('User created successfully',user_data)

        except Exception as e:
            return utils.make_error_response(f'Error creating user')

class UpdateUser(Resource):
    @jwt_required()
    def put(self):
        try:
            #Obtener y parsear los argumentos.
            parser = reqparse.RequestParser()
            parser.add_argument('id_user', type=int, location='json')
            parser.add_argument('first_name', type=str, location='json')
            parser.add_argument('last_name', type=str, location='json')
            parser.add_argument('date_birth', type=str, location='json')
            parser.add_argument('mobile_phone', type=str, location='json')
            parser.add_argument('email', type=str, location='json')
            parser.add_argument('password', type=str, location='json')
            parser.add_argument('address', type=str, location='json')

            args = parser.parse_args()

            obj_user_id = args['id_user']
            obj_first_name= args['first_name']
            obj_last_name= args['last_name']
            obj_date_birth= args['date_birth']
            obj_mobile_phone= args['mobile_phone']
            obj_email= args['email']
            obj_password= args['password']
            obj_address= args['address']

            #Buscar usuario que sera actualizado
            user = user_model.User.query.filter_by(id=obj_user_id).first()
            if not user:
                return utils.make_error_validate_response('User not found')

            #(agregar al diccionario los campos actualizables). Solo se actualizan los campos que si llegan
            fields_to_update = {
                'first_name': obj_first_name,
                'last_name': obj_last_name,
                'date_birth': obj_date_birth,
                'mobile_phone': obj_mobile_phone,
                'email': obj_email,
                'password': obj_password,
                'address': obj_address
            }

            #Actualizacion de campos recibidos en el diccionario
            for field, value in fields_to_update.items():
                if value:
                    setattr(user, field, value)

            db.session.commit()

            #Serializacion y respuesta
            user_schema = user_model.UserSchema()
            user_data = user_schema.dump(user)

            return utils.make_response_ok_success('User updated successfully', user_data)

        except Exception as e:
            return utils.make_error_response(f'Error updating user')

class GetUsers(Resource):
    def get(self):
        try:
            #Buscar todos los usuarios
            users = user_model.User.query.filter_by().all()

            users_schema = user_model.UserSchema(many=True)
            users_data = users_schema.dump(users)

            return utils.make_response_ok_success('Users List',users_data)

        except Exception as e:
            return utils.make_error_response('Interval Server Error')

class GetUser(Resource):
    @jwt_required()
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id_user', type=int, location="json")

            args = parser.parse_args()
            obj_user_id = args['id_user']

            #Buscar usuario por id
            user = user_model.User.query.filter_by(id=obj_user_id).first()

            if not user:
                return utils.make_error_validate_response('User not found')

            user_schema = user_model.UserSchema()
            user_data = user_schema.dump(user)

            return utils.make_response_ok_success('User found', user_data)

        except Exception as e:
            # Manejar cualquier excepción
            return utils.make_error_response('Internal Server Error')

class DeleteUser(Resource):
    @jwt_required()
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, location='json')

            args = parser.parse_args()
            obj_user_id = args['id']

            #Buscar usuario a eliminar
            user = user_model.User.query.filter_by(id=obj_user_id).first()

            if not user:
                return utils.make_error_validate_response('User not found')

            #Eliminar usuario
            db.session.delete(user)
            db.session.commit()

            user_schema = user_model.UserSchema()
            user_data = user_schema.dump(user)

            return utils.make_response_ok_success('User deleted successfully',user_data)

        except Exception as e:
            return utils.make_error_response(f'Error deleting user')

