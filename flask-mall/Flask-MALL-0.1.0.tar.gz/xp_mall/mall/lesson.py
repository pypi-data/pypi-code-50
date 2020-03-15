# -*- coding=utf-8 -*-
from flask import request, render_template, current_app, flash, url_for
from flask_login import current_user, login_required
# from xp_cms.controller import article_bp
from .. import course_module
from xp_cms.extensions import db, cache
from xp_cms.utils import redirect_back, redirect
from xp_cms.emails import send_new_comment_email, send_new_reply_email
from ..models.course import Course, CourseComment as Comment
from ..models.course import CourseLesson, LessonQuestion
from ..models.category import CourseCategory as Category
from ..forms.goods import CommentForm
from ..forms.lesson import LessonForm, QuestionForm
from ..utils import get_all_subcate, get_all_parent, can_view




@course_module.route('/lesson/detail/<int:lesson_id>', methods=['GET', 'POST'])
@cache.cached(timeout=10 * 60)
@login_required
@can_view
def show_lesson(lesson_id):

    lesson = CourseLesson.query.get_or_404(lesson_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['XPCMS_COMMENT_PER_PAGE']
    pagination = LessonQuestion.query.with_parent(lesson).filter_by(reviewed=True).order_by(LessonQuestion.timestamp.asc()).paginate(
        page, per_page)
    questions = pagination.items
    prev, _next = get_pre_next(CourseLesson, lesson)

    form = QuestionForm()
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
        author = current_user.user_id
        body = form.body.data
        question = LessonQuestion(
            author=author,  body=body,
            from_admin=from_admin, lesson=lesson, reviewed=reviewed)

        replied_id = request.args.get('reply')

        if replied_id:
            replied_answer = LessonQuestion.query.get_or_404(replied_id)
            question.replied = replied_answer
            # send_new_reply_email(replied_comment)
        db.session.add(question)
        db.session.commit()
        if current_user.is_authenticated:  # send message based on authentication status
            flash('Comment published.', 'success')
        else:
            flash('Thanks, your comment will be published after reviewed.', 'info')
            # send_new_comment_email(course)  # send notification email to admin
        return redirect(url_for('.show_lesson', lesson_id=lesson_id))
    return render_template('course/lesson/detail.html', lesson=lesson, pagination=pagination, form=form, questions=questions,
                           prev=prev,next=_next)




def get_pre_next(model, obj):
    # 前一条
    prev = model.query.filter(model.course_id == obj.course_id, model.order_id < obj.order_id). \
        order_by(model.order_id.desc()).first()
    _next = model.query.filter(model.course_id == obj.course_id, model.order_id > obj.order_id). \
        order_by(model.order_id.asc()).first()

    return prev, _next