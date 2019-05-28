from app import db
from app.views.index import index_blu
from flask import render_template, request, jsonify
from app.models.models import News


@index_blu.route("/index")
@index_blu.route("/")
def index():
    # 1.查询点击排行的前6个数据
    news = db.session.query(News).order_by(News.clicks.desc()).limit(6)
    
    return render_template("index/index.html", news=news)


@index_blu.route('/newslist')
def newslist():
    # 0.提取数据
    page = request.args.get('page', 1)
    cid = request.args.get('cid', 0)
    per_page = request.args.get('per_page', 10)

    page = int(page) if page.isalnum() else 1
    cid = int(cid) if cid.isalnum() else 0
    per_page = int(per_page) if per_page.isalnum() else 10

    # 1. 先从数据库中查询
    if cid == 0:
        paginate = db.session.query(News).order_by(News.create_time.desc()).paginate(page, per_page, False)
    else:
        paginate = db.session.query(News).filter(News.category_id == cid).paginate(page, per_page, False)
    news_list = paginate.items

    # 2. 将查询出来的数据模型转换为需要的字典格式
    ret = {
        'totalpage': paginate.pages,
        'newsList': [news.to_dict() for news in news_list]
    }

    # 3.将字典格式的数据转换为json格式，返回给前端
    return jsonify(ret)


@index_blu.route('/detail/<int:news_id>')
def detail(news_id):
    return render_template('index/detail.html')
