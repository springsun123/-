class Config(object):
    SECRET_KEY = '1'

    # 关闭追踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wazyx2018@localhost:3006/flask_xjzx_2019?charset=utf8'


class ProductionConfig(Config):
    DEBUG = False


CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}