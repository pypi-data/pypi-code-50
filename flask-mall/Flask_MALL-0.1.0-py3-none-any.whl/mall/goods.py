# -*- coding=utf-8 -*-

from flask import request, render_template, current_app, flash, url_for
from flask_login import current_user
from xp_mall.controller import article_bp
from xp_mall.controller import mall_bp
from xp_mall.extensions import db, cache
from xp_mall.models.post import Post, Comment
from xp_mall.models.category import Category
from xp_mall.utils import redirect_back, redirect

from xp_mall.models.goods import *
from xp_mall.forms.goods import GoodsForm, GoodsCategoryForm



@admin_bp.route('/category/new', methods=['GET', 'POST'])
@login_required
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        parent_id = form.parent_id.data
        name = form.name.data
        cate_type = form.cate_type.data
        order_id = form.order_id.data
        category = Category(name=name, parent_id=parent_id, cate_type=cate_type, order_id=order_id)
        db.session.add(category)
        db.session.commit()
        # flash('Category created.', 'success')
        # return redirect(url_for('.manage_category'))
        return str(category.id)
    elif form.errors:
        return jsonify(form.errors)
    return render_template('admin/category/new_category.html', form=form)


@admin_bp.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_category(category_id):
    form = CategoryForm()
    category = Category.query.get_or_404(category_id)
    g.category_id = category_id
    g.category_name = category.name
    # if category.id == 1:
        # flash('You can not edit the default category.', 'warning')
        # return redirect(url_for('blog.index'))
    if form.validate_on_submit():

        category.name = form.name.data
        category.parent_id = form.parent_id.data
        category.cate_type = form.cate_type.data
        category.order_id = form.order_id.data
        db.session.commit()
        return "success"
    # else:
    #     print(form)
    #     # return "false"
    #     print(form.errors)
    #     return "false"

    form.name.data = category.name
    form.parent_id.data = category.parent_id
    form.cate_type.data = category.cate_type
    form.order_id.data = category.order_id
    return render_template('admin/category/edit_category.html', form=form)

@admin_bp.route('/category/<int:category_id>/delete', methods=['POST'])
@login_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    category.delete()
    # return redirect(url_for('.manage_category'))
    return "ok"



@mall_bp.route('/goods/add', methods=['GET', 'POST'])
def goods_add():
    form = GoodsForm()
    errors = None
    if form.validate_on_submit():
        goods_name = form.goods_name.data
        goods_price = form.goods_price.data
        goods_detail = form.goods_detail.data
        goods = Goods(
            goods_name = goods_name,
            goods_price = goods_price,
            goods_detail = goods_detail
        )
        db.session.add(goods)
        db.session.commit()
    elif form.errors:
        pass
    return render_template('admin/mall/add_goods.html', form=form, errors=errors)
