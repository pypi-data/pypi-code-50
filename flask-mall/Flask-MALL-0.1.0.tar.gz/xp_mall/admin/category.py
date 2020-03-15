# -*- coding=utf-8 -*-

from flask import render_template,g,request, jsonify
from flask_login import login_required
from xp_mall.admin import admin_module
from xp_mall.extensions import db
from xp_mall.forms.goods import CategoryForm
from xp_mall.models.goods import Goods
from xp_mall.models.category import GoodsCategory



"""
Category 商品分类管理
"""
@admin_module.route('/category/manage/', defaults={"parent_id":0}, methods=["GET"])
@admin_module.route('/category/manage/<int:parent_id>', methods=["GET"])
@login_required
def manage_category(parent_id):
    categories = GoodsCategory.query.filter_by(parent_id=parent_id).order_by(Category.order_id).all()
    return render_template('admin/category/manage_category.html', categories=categories)

@admin_module.route('/category/new', methods=['GET', 'POST'])
@login_required
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        parent_id = form.parent_id.data
        name = form.name.data
        cate_type = form.cate_type.data
        order_id = form.order_id.data
        category = GoodsCategory(name=name, parent_id=parent_id, cate_type=cate_type, order_id=order_id)
        db.session.add(category)
        db.session.commit()
        # flash('Category created.', 'success')
        # return redirect(url_for('.manage_category'))
        return str(category.id)
    elif form.errors:
        return jsonify(form.errors)
    return render_template('admin/category/new_category.html', form=form)


@admin_module.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_category(category_id):
    form = CategoryForm()
    category = GoodsCategory.query.get_or_404(category_id)
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

@admin_module.route('/category/<int:category_id>/delete', methods=['POST'])
@login_required
def delete_category(category_id):
    category = GoodsCategory.query.get_or_404(category_id)
    category.delete()
    # return redirect(url_for('.manage_category'))
    return "ok"

@admin_module.route('/category/delete', methods=['POST'])
@login_required
def batch_delete_category():
    ids = request.form.getlist("checkID[]")

    # db.session.query(Category).filter(Category.id.in_(ids)).delete(synchronize_session=False)
    GoodsCategory.query.filter(GoodsCategory.id.in_(ids)).delete(synchronize_session=False)
    goods = Goods.query.filter(Goods.category_id)
    # if category.id == 1:
    #     flash('You can not delete the default category.', 'warning')
    #     return redirect(url_for('blog.index'))
    # category.delete()
    goods.delete()
    db.session.commit()
    # flash('Category deleted.', 'success')
    # return redirect(url_for('.manage_category'))
    return "ok"

@admin_module.route('/category/<int:parent_id>', methods=['get'])
@login_required
def get_cate(parent_id):
    sub_cates = GoodsCategory.query.filter_by(parent_id=parent_id).all()
    cate_dicts = [(sub_cate.name,sub_cate.id) for sub_cate in sub_cates]
    # print(cate_dicts)
    return jsonify(cate_dicts)
#