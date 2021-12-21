from decouple import config 
import os 

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLAlchemy_Track_MODIFICATIONS=config('SQLAlchemy_Track_MODIFICATIONS', cast=bool)


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,'dev.db')
    DEBUG=True 
    SQLAlchemy_ECHO=True 

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///test.db"
    sql_alchemy_echo=False
    TESTING=True
