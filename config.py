import logging

class Config:
    """ Common configurations """

class DevelopmentConfig(Config):
    """ Development configurations """
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123456@127.0.0.1/USERS'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_BINDS = {
        "otra_conexion": "mysql+pymysql://credenciales",
    }
    logging.basicConfig(level=logging.INFO)


class QualityConfig(Config):
    """ QA Ambient configurations """
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123456@127.0.0.1/USERS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        "otra_conexion": "mysql+pymysql://credenciales",
    }

class ProductionConfig(Config):
    """ Production configurations """
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123456@127.0.0.1/USERS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        "otra_conexion": "mysql+pymysql://credenciales",
    }

app_config = {
    'dev': DevelopmentConfig,
    'qa':QualityConfig,
    'pro': ProductionConfig
}

#modelos
#flask-sqlacodegen --flask --outfile tareas_model.py --tables tareas mysql+pymysql://root:admin123456@127.0.0.1/CRUD_TD

