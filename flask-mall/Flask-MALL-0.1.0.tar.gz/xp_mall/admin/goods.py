# -*- coding=utf-8 -*-

from flask import render_template, request, current_app, flash
from flask import jsonify, json
from flask_login import login_required

from xp_mall.extensions import db
from xp_mall.utils import redirect_back
from xp_mall.admin.admin_module import admin_module
from xp_mall.models.goods import Goods, GoodsComments
from xp_mall.models.category import GoodsCategory
from xp_mall.models.tags import tags_goods, GoodsTags
from xp_mall.forms.goods import GoodsForm
import json as sys_json

@admin_module.route('/manage/goods', defaults={'category_id': None})
@admin_module.route('/manage/goods/<int:category_id>', methods=['GET'])
@login_required
def manage_goods(category_id=None):
    page = request.args.get('page', 1, type=int)
    if not category_id:
        pagination = Goods.query.order_by(Goods.timestamp.desc()).paginate(
        page, per_page=current_app.config['XPMALL_MANAGE_GOODS_PER_PAGE'])
    else:
        pagination = Goods.query.filter_by(category_id=category_id).order_by(Goods.timestamp.desc()).paginate(
            page, per_page=current_app.config['XPMALL_MANAGE_GOODS_PER_PAGE'])
    goods = pagination.items

    return render_template('admin/goods/manage_goods.html', page=page, pagination=pagination, goods=goods)


@admin_module.route('/manage/goods/new', methods=['GET', 'POST'])
@login_required
def new_goods():
    form = GoodsForm()
    if form.validate_on_submit():
        title = form.title.data
        order_id = form.order_id.data
        thumb = form.thumb.data
        intro = form.intro.data
        body = form.body.data
        category = GoodsCategory.query.get(form.category.data)
        tags = form.tags.data.replace("，",",")
        price = form.price.data
        course = Goods(title=title, body=body, category=category, intro=intro, thumb=thumb, tags_list=tags,
                    order_id=order_id, total_price=price)

        tags_list_id = add_tags(tags)
        # same with:
        # category_id = form.category.data
        # post = Post(title=title, body=body, category_id=category_id)
        course.tags = tags_list_id
        db.session.add(course)
        db.session.commit()
        # flash('Post created.', 'success')
        # return redirect(url_for('blog.show_post', post_id=post.id))
        return jsonify({"course_id":course.id})
    elif request.method == 'POST' and form.errors:
        return jsonify(form.errors)

    return render_template('admin/goods/new_goods.html', form=form)



@admin_module.route('/goods/<int:goods_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_goods(goods_id):
    form = GoodsForm()
    goods = Goods.query.get_or_404(goods_id)
    if form.validate_on_submit():
        goods.title = form.title.data
        goods.intro = form.intro.data
        goods.order_id = form.order_id.data
        goods.body  = form.body.data
        goods.thumb = form.thumb.data
        goods.category = GoodsCategory.query.get(form.category.data)
        tags = form.tags.data.replace(" ","").replace("，", ",")
        goods.tags_list = tags
        tags_list_id = add_tags(tags)
        for item in goods.tags:
            if tags.find(item.name) == -1:
                goods.tags.remove(item)
        print("-------------------")
        goods.tags = tags_list_id
        goods.price = form.price.data
        db.session.commit()

        # flash('Post updated.', 'success')
        # return redirect(url_for('blog.show_post', post_id=post.id))
    elif form.errors:
        print("************")
        print(form.errors)
    form.title.data = goods.title
    form.order_id.data = goods.order_id
    form.intro.data = goods.intro
    form.body.data = goods.body
    form.thumb.data = goods.thumb
    thumb = str(goods.thumb)
    form.category.data = goods.category_id
    form.tags.data = goods.tags_list
    form.video_url.data = goods.video_url
    form.price.data = goods.price
    return render_template('admin/goods/edit_goods.html', form=form, thumb=thumb)


@admin_module.route('/goods/delete/<int:goods_id>', methods=['POST'])
@login_required
def delete_goods(goods_id):
    goods = Goods.query.get_or_404(goods_id)
    db.session.delete(goods)
    db.session.commit()
    # return redirect_back()
    return "ok"

@admin_module.route("/manage/course/delete", methods=['POST'])
@login_required
def batch_delete_course():
    ids = request.form.getlist("checkID")
    print(list(request.form.lists()))
    print(ids)
    delete = tags_goods.delete().where(tags_goods.c.course_id.in_(ids))
    db.get_engine().connect().execute(delete)
    Goods.query.filter(Goods.id.in_(ids)).delete(synchronize_session="fetch")
    GoodsComments.query.filter(GoodsComments.course_id.in_(ids)).delete(synchronize_session="fetch")
    # print(dir(tags_articles))
    db.session.commit()

    return "ok"


@admin_module.route('/manage/commment/set/<int:course_id>', methods=['POST'])
@login_required
def set_comment(course_id):
    course = Goods.query.get_or_404(course_id)
    if course.can_comment:
        course.can_comment = False
        flash('Comment disabled.', 'success')
    else:
        course.can_comment = True
        flash('Comment enabled.', 'success')
    db.session.commit()
    # return redirect_back()
    return "ok"

@admin_module.route('/manage/comment/')
@login_required
def manage_comment():
    filter_rule = request.args.get('filter', 'all')  # 'all', 'unreviewed', 'admin'
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['XPCMS_COMMENT_PER_PAGE']
    if filter_rule == 'unread':
        filtered_comments = GoodsComments.query.filter_by(reviewed=False)
    elif filter_rule == 'admin':
        filtered_comments = GoodsComments.query.filter_by(from_admin=True)
    else:
        filtered_comments = GoodsComments.query

    pagination = filtered_comments.order_by(GoodsComments.timestamp.desc()).paginate(page, per_page=per_page)
    comments = pagination.items
    return render_template('article/admin/article/manage_comment.html', comments=comments, pagination=pagination)


@admin_module.route('/manage/comment/approve/<int:comment_id>', methods=['POST'])
@login_required
def approve_comment(comment_id):
    comment = GoodsComments.query.get_or_404(comment_id)
    comment.reviewed = True
    db.session.commit()
    flash('Comment published.', 'success')
    return redirect_back()


@admin_module.route('/manage/comment/delete/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = GoodsComments.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted.', 'success')
    # return redirect_back()
    return "ok"

@admin_module.route("/manage/comment/delete", methods=['POST'])
@login_required
def batch_delete_comment():
    print("------"*10)
    ids = request.form.getlist("checkID[]")
    print(ids)
    GoodsComments.query.filter(GoodsComments.id.in_(ids)).delete(synchronize_session="fetch")
    db.session.commit()
    return "ok"

def add_tags(tags):
    tags_list = tags.split(",")
    tags_list_id = []
    for tag in tags_list:
        exit_tag = db.session.query(GoodsTags).filter_by(name=tag).one_or_none()
        if not exit_tag:
            new_tag = GoodsTags(name=tag)
            db.session.add(new_tag)
            db.session.commit()
            if new_tag.id:
                tags_list_id.append(new_tag)
        else:
            tags_list_id.append(exit_tag)
    return tags_list_id
