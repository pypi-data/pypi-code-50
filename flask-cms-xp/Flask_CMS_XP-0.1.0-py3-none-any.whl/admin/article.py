# -*- coding=utf-8 -*-

from flask import request,session,render_template,\
                  redirect, url_for

from .admin_app import admin_app
from models import Article,Category
from libs import db
import json
from flask import jsonify

@admin_app.route("/article/post", methods=['get','post'])
def article_post():
    if request.method == "POST":
        cate_id = request.form['cate']
        title = request.form['title']
        intro    = request.form['intro']
        content  = request.form['content']
        article = Article(
                    cate_id = cate_id,
                    title=title,
                    intro=intro,
                    content=content,
                    author=session['user']
         )


        db.session.add(article)
        db.session.commit()
        message = {"message":"发布成功"}
        return json.dumps(message)

    return render_template("admin/article/article_post.html")


# 获得文章列表
@admin_app.route("/article/list/<int:page>", methods=['get', "post"])
@admin_app.route("/article/list", defaults={"page":1},methods=['get', "post"])
def article_list(page):
    if request.method == "POST":
        q = request.form['q']
        condition = {request.form['field']:q}
        if request.form['field'] == "title":
            condition = Article.title.like('%%%s%%' % q)
        else:
            condition = Article.content.like('%%%s%%' % q)
        if request.form['order'] == "1":
            order = Article.id.asc()
        else:
            order = Article.id.desc()

        res = Article.query.filter(condition)\
                                .order_by(order)\
                                .paginate(page, 10)


    else:
        res = Article.query.paginate(page,10)

    # 无论搜索还是默认查看，都是翻页处理
    articles = res.items
    pageList = res.iter_pages()
    pages = res.pages
    total = res.total

    return render_template("admin/article/article_list.html", articles=articles,
                           pageList=pageList,
                           pages=pages,
                           total=total
                           )


# 根据文章id删除文章
@admin_app.route("/article/delete", methods=['post'])
def article_delete():
    article_id = int(request.form.get("article_id"))
    message = {"res":"fail","id":article_id, "type":"del"}
    if article_id:
        article = Article.query.get(article_id)
        if article:
            try:
                db.session.delete(article)
                db.session.commit()
            except Exception as e:
                print(e)
            else:
                message['res'] = "success"
    return jsonify(message)



# 文章推荐
@admin_app.route("/article/recommend", methods=["post"])
def article_recommend():
    article_id = int(request.form.get("article_id"))
    message = {"res":"fail","id":article_id,"type":"recommend"}
    if article_id:
        article = Article.query.get(article_id)
        if article:
            article.is_recommend = 1
            try:
                db.session.commit()
            except Exception as e:
                print(e)
            else:
                message['res'] = "success"
    return jsonify(message)

