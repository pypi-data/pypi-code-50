# -*- coding=utf-8 -*-
from flask import request, render_template, current_app, flash, url_for
from flask_login import current_user
# from xp_cms.controller import article_bp
from .. import course_module
from xp_cms.extensions import db, cache
from xp_cms.utils import redirect_back, redirect
from xp_cms.emails import send_new_comment_email, send_new_reply_email
from ..models.course import Course, CourseComment as Comment
from ..models.category import CourseCategory as Category
from ..forms.goods import CommentForm
from ..utils import get_all_subcate, get_all_parent


@course_module.route('/')
@cache.cached(timeout=10 * 60)
def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['XPCMS_ARTICLE_PER_PAGE']
    pagination = Course.query.order_by(Course.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    categories = Category.query.order_by(Category.id).first()

@course_module.route("/search")
def search():
    q = request.args.get('q', '')
    if q == '':
        flash('请输入搜索关键字')
        return redirect_back()
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['XPCMS_ARTICLE_PER_PAGE']

    pagination = Course.query.whooshee_search(q).paginate(page, per_page)
    courses = pagination.items
    return render_template("article/search.html", q=q, courses=courses, pagination=pagination)


@course_module.route('/detail/<int:category_id>/<int:course_id>', methods=['GET', 'POST'])
@cache.cached(timeout=10 * 60)
def show_course(category_id, course_id):

    course = Course.query.get_or_404(course_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['XPCMS_COMMENT_PER_PAGE']
    pagination = Comment.query.with_parent(course).filter_by(reviewed=True).order_by(Comment.timestamp.asc()).paginate(
        page, per_page)
    comments = pagination.items
    category_tree = get_all_parent(course.category_id)  #
    category_tree.sort(key=lambda x: x[1], reverse=False)
    categories = Category.query.filter_by(id=category_tree[0][1]).order_by(Category.order_id).first()
    prev, _next = get_pre_next(Course, course)

    form = CommentForm()
    if current_user.is_authenticated:
        # form = AdminCommentForm()
        # form.author.data = current_user.username
        # form.email.data = current_app.config['XPCMS_EMAIL']
        # form.site.data = url_for('.index')
        # from_admin = True
        # reviewed = True
        pass
    else:

        from_admin = False
        reviewed = False

    if form.validate_on_submit():
        author = form.author.data
        email = form.email.data
        site = form.site.data
        body = form.body.data
        comment = Comment(
            author=author, email=email, site=site, body=body,
            from_admin=from_admin, course=course, reviewed=reviewed)

        replied_id = request.args.get('reply')

        if replied_id:
            replied_comment = Comment.query.get_or_404(replied_id)
            comment.replied = replied_comment
            send_new_reply_email(replied_comment)
        db.session.add(comment)
        db.session.commit()
        if current_user.is_authenticated:  # send message based on authentication status
            flash('Comment published.', 'success')
        else:
            flash('Thanks, your comment will be published after reviewed.', 'info')
            send_new_comment_email(course)  # send notification email to admin
        return redirect(url_for('.show_course', course_id=course_id))
    return render_template('course/detail.html', course=course, pagination=pagination, form=form, comments=comments,
                           category=categories,category_tree=category_tree,
                           prev=prev,next=_next)


@course_module.route('/course_category/<int:category_id>/',methods=["GET"])
@cache.cached(timeout=10 * 60)
def category_course(category_id):
    return category_lists(category_id, "article")

@course_module.route('/manual_category/<int:category_id>/', methods=["GET"])
@cache.cached(timeout=10 * 60)
def category_manual(category_id):
    return category_lists(category_id, "manual")

def category_lists(category_id, order_type):
    category_tree = get_all_parent(category_id)  #
    category_tree.sort(key=lambda x: x[1], reverse=False)
    categories = Category.query.filter_by(id=category_tree[0][1]).order_by(Category.order_id).first()
    sub_categories = get_all_subcate(category_id, [])

    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['XPCMS_ARTICLE_PER_PAGE']
    pagination = Course.query.filter(Course.category_id.in_(sub_categories)).order_by(Course.timestamp.desc() if
                                                                                  order_type=="course" else Course.order_id).paginate(page,
                                                                                                                  per_page=per_page)
    courses = pagination.items

    return render_template('course/lists.html', pagination=pagination, courses=courses, category=categories,
                           category_tree=category_tree)

def get_pre_next(model, obj):
    # 前一条
    if obj.category.cate_type == "course":
        prev = model.query.filter(model.category_id == obj.category_id, model.order_id < obj.order_id). \
            order_by(model.order_id.desc()).first()
        _next = model.query.filter(model.category_id == obj.category_id, model.order_id > obj.order_id). \
            order_by(model.order_id.asc()).first()
    else:
        prev = model.query.filter(model.category_id == obj.category_id, model.id < obj.id). \
            order_by(model.id.desc()).first()
        _next = model.query.filter(model.category_id == obj.category_id, model.id > obj.id). \
            order_by(model.id.asc()).first()
    return prev, _next