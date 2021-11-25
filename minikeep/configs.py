import os 
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class Config:
    """flask config"""
    SECRET_KEY = 'secretkey'    
    SESSION_COOKIE_NAME = 'minikeep'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/minikeep?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'

class DevelopmentConfig(Config):
    """flask config dev"""
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    WTF_CSRF_ENABLED = False

class ProductionConfig(DevelopmentConfig):
    pass

class TestingConfig(DevelopmentConfig):
    __test__ = False
    TESTING  = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_PATH, "sqlite_test.db")}'
    