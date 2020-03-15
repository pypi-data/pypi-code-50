# -*- coding=utf-8 -*-

from flask import  request, flash, url_for

from .. import course_module
from .. models.course import CourseComment as Comment
from xp_cms.utils import redirect


@course_module.route('/reply/comment/<int:comment_id>')
def reply_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if not comment.course.can_comment:
        flash('尚未开放评论.', 'warning')
        return redirect(url_for('.show_course', post_id=comment.course.id))
    return redirect(
        url_for('.show_course', post_id=comment.course_id, reply=comment_id, author=comment.author) + '#comment-form')
