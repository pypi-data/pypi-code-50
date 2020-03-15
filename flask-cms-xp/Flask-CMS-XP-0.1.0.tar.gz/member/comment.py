# -*- coding=utf-8 -*-

from flask import request,session,render_template,\
                  redirect, url_for

from .member_app import member_app
from models import Article,Category, Comment
from libs import db
from flask import jsonify
from forms.article_form import CommentForm


@member_app.route("/comment/publish", methods=["post"])
def publish():
    form = CommentForm()
    message = {"res":"fail"}
    if form.validate_on_submit():
        comment_data = form.data['comment']
        article_id = form.data['article_id']
        article = Article.query.get(article_id)
        if article:
            comment = Comment(**{
                "body":comment_data,
                "observer": session['user'],

            })

            try:
                article.comments.append(comment)
                db.session.commit()
            except Exception as e:
                print(e)
            else:
                message['res'] = "success"

    return jsonify(message)





