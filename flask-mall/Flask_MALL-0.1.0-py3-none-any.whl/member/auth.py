# -*- coding: utf-8 -*-
import json
from flask import request, render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user

from ..forms.member import LoginForm, RegisterForm, ForgetPasswordForm, ResetPasswordForm
from ..models.member import Member
from xp_mall.utils import redirect_back
from xp_mall.extensions import db
from xp_mall.utils import generate_token, validate_token
from xp_mall.settings import Operations


member_module = Blueprint('member', __name__)


@member_module.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('article.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = Member.query.filter_by(username=username).first()

        if user:

            if username == user.username and user.validate_password(password):
                login_user(user, remember)
                flash('Welcome back.', 'info')
                print("login")
                return redirect_back()
            else:
                flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('member/auth/login.html', form=form)

@member_module.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('article.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        username = form.username.data
        password = form.password.data
        user = Member(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return "success"
    elif form.errors:
        return json.dumps(form.errors)
    return render_template('member/auth/register.html', form=form, next=request.args.get('next', ''))

@member_module.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect_back()

@member_module.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))

    if validate_token(user=current_user, token=token, operation=Operations.CONFIRM):
        flash("Account confirmed.", 'success')
        return redirect(url_for('main.index'))
    else:
        flash('Invalid or expried token.', 'danger')
        return redirect(url_for('.resend_confirmation'))

@member_module.route('resend-confirm-email')
@login_required
def resend_confirm_email():
    if current_user.confirmed:
        return redirect(url_for('main.index'))

    token = generate_token(user=current_user, opration=Operations.CONFIRM)
    resend_confirm_email(user=current_user, token=token)
    flash("New email sent, check you inbox.",  'info')
    return redirect(url_for("main.index"))

@member_module.route('/login', methods=['GET', 'POST'])
def forget_password():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = ForgetPasswordForm()
    if form.validate_on_submit():
        username = form.data.username
        user = Member.query.filter_by(username=username).first()
        if user:
            token = generate_token(user=user, operation=Operations.RESET_PASSWORD)
            # send_reset_password_email(user=user, token=token)
            flash('Password reset email sent, check yourinbox', 'info')
            return redirect(url_for('.login'))
        flash('Invalid email', 'warning')

@member_module.route('reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("article.index"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        username = form.data.username
        new_password = form.data.newpassword
        user = Member.query.filter_by(username=username).first()
        if user is None:
            flash("No account.", "warning")
            return redirect(url_for("index"))
        if validate_token(user=user, token=token, operation=Operations.RESET_PASSWORD,
                          new_password=new_password):
            flash('Password update.', 'success')
            return redirect(url_for("article.inidex"))
        else:
            flash('Invalid or expired token.', 'danger')
            return redirect(url_for('.forget_password'))
    return render_template('member/auth/reset_password.html', form=form)


