from app import db
from app.views.index import index_blu
from flask import render_template
from app.models.models import News


@index_blu.route("/index")
@index_blu.route("/")
def index():
    # 1.查询点击排行的前6个数据
    news = db.session.query(News).order_by(News.clicks.desc()).limit(6)
    
    return render_template("index/index.html", news=news)