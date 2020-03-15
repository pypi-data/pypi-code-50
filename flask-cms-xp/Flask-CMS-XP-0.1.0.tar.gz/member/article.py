# -*- coding=utf-8 -*-

from flask import request,session,render_template,\
                  redirect, url_for

from .member_app import member_app
from models import Article,Category
from libs import db
from flask import jsonify
from forms.article_form import ArticleForm,\
                               ArticleSearchForm

@member_app.route("/article/post", methods=['get','post'])
def article_post():
    form = set_article_form()
    if form.validate_on_submit():
        cate_id = form.data['cate']
        title = form.data['title']
        thumb = form.data['thumb']
        intro    = form.data['intro']
        content  = form.data['content']
        article = Article(
                    cate_id = cate_id,
                    title=title,
                    thumb=thumb,
                    intro=intro,
                    content=content,
                    author=session['user']
         )

        try:
            db.session.add(article)
            db.session.commit()
        except Exception as e:
            print(e)
            message = {"message": "发布失败"}
        else:
            message = {"message":"发布成功"}
        return jsonify(message)

    return render_template("member/article/article_post.html",form=form)


# 获得文章列表
@member_app.route("/article/list/<int:page>", methods=['get', "post"])
@member_app.route("/article/list", defaults={"page":1},methods=['get', "post"])
def article_list(page):
    form = ArticleSearchForm()
    print("ok" ,request.args.get("t"))
    if request.args.get("t")  == "":
        print("yes")
    else:
        print("no")
    if form.validate_on_submit():
        q = form.data['q']
        condition = {form.data['field']:q}
        if form.data['field'] == "title":
            condition = Article.title.like('%%%s%%' % q)
        else:
            condition = Article.content.like('%%%s%%' % q)
        if form.data['order'] == "1":
            order = Article.id.asc()
        else:
            order = Article.id.desc()
#       普通会员只能在后台管理自己的文章
        res = Article.query.filter(Article.author==session['user'])\
                                .filter(condition) \
                                .order_by(order)\
                                .paginate(page, 10)


    else:
        res = Article.query.filter(Article.author==session['user']).paginate(page,10)

    # 无论搜索还是默认查看，都是翻页处理
    articles = res.items
    pageList = res.iter_pages()
    pages = res.pages
    total = res.total

    return render_template("member/article/article_list.html", articles=articles,
                           pageList=pageList,
                           pages=res.pages,
                           total=total,
                           form=form
                           )


# 根据文章id删除文章
@member_app.route("/article/delete/<int:article_id>")
def article_delete(article_id):
    article = Article.query.get(article_id)
    # 只能删除自己的文章
    if article.author == session['user']:
        db.session.delete(article)
        db.session.commit()
    return redirect(url_for(".article_list"))


# 文章修改
@member_app.route("/article/edit/<int:article_id>", methods=['get', 'post'])
def article_edit(article_id):
    article = Article.query.get(article_id)
    if not article:
        return redirect(url_for(".article_list"))
    form = set_article_form()

    if form.validate_on_submit():
        # 只能修改自己的文章
        if article.author == session['user']:
            article.cate_id = form.data['cate']
            article.thumb = form.data['cate']
            article.title = form.data['title']
            article.intro = form.data['intro']
            article.content= form.data['content']
            print(article.cate_id)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                message = {"res":"fail"}
            else:
                message = {"res":"success"}
            return  jsonify(message)
    elif form.errors:
        return jsonify(form.errors)
    else:
        form.cate.data = article.cate_id
        form.title.data = article.title
        form.thumb.data = article.thumb
        form.intro.data = article.intro
        form.content.data = article.content
        print(dir(form.thumb))
    return render_template("member/article/article_edit.html", form=form)

def set_article_form():
    form = ArticleForm()
    form.cate.choices = [(cateOption.cate_id, cateOption.cate_name) for cateOption in Category.query.all()]
    return form