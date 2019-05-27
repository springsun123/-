from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from config import CONFIG

db = SQLAlchemy()


def create_app(create_name):

    from app.views.index import index_blu

    # 创建flask对象
    app = Flask(__name__)

    # 对flask对象进行配置
    app.config.from_object(CONFIG.get(config_name))

    # 注册蓝图
    app.register_blueprint(index_blu)

    # 对db进行配置
    db.init_app(app)

    # 注册过滤器
    app.add_template_filter(show_index_colorful, 'show_index_colorful')

    return app