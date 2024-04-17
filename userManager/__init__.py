import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_jwt_extended import JWTManager


from config import app_config

app = Flask(__name__)
api = Api(app)

ma = SQLAlchemyAutoSchema()

config_name = os.getenv('FLASK_ENV')
app.config.from_object(app_config[config_name])
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = 'clavesecreta'
jwt = JWTManager(app)


from userManager.routes import user_manager_routes
from userManager.controllers import user_manager_controller



