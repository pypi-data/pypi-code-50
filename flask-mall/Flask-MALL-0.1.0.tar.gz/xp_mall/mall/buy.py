# -*- coding=utf-8 -*-
import time, math

from flask import current_app, render_template, redirect, request, jsonify, url_for
from flask_login import current_user, login_required
from xp_cms.extensions import db,csrf
from .. import course_module
from ..forms.buy import OrderForm
from ..models.deal import Order, OrderCourse, Cart, OrderCourseLesson
from ..models.course import Course, CourseLesson



@course_module.route('/buy_course/<int:course_id>')
def buy_course(course_id):
    course = Course.query.get_or_404(course_id)
    print(course)
    form = OrderForm()
    if form.validate_on_submit():

        ordercourse = OrderCourse(
            course_id=course_id,
            price= get_total_price(1, course_id),
            order_price = get_total_price(1, course_id),
            amout = 1,
            discount=1
        )
        order = Order(
            order_no = get_order_no(),
            total_price = 0,
            status = "0",
            seller = "python-xp",
            buyer = current_user.user_id,
            payment = "",
        )
        order.courses.append(ordercourse)
        db.session.add(order)
        db.session.commit()

    return render_template('course/deal/buy.html', form=form, course=course)

@course_module.route('/buy_lesson/<int:lesson_id>')
@login_required
def buy_lesson(lesson_id):
    lesson = CourseLesson.query.get_or_404(lesson_id)
    form = OrderForm()
    orderlesson = OrderCourseLesson(
        lesson_id=lesson_id,
        course_id=lesson.course_id,
        lesson_price=lesson.price,
        user_id=current_user.user_id
    )
    order = Order(
        order_no=get_order_no(),
        total_price=lesson.price,
        status="0",
        seller="python-xp",
        buyer=current_user.user_id,
        payment="",
        subject = lesson.title
    )
    order.lessons.append(orderlesson)
    db.session.add(order)
    db.session.commit()
    return render_template('course/deal/buy.html', form=form, course=None, lesson=lesson, order_id=order.id)

@course_module.route('/pay_order/<int:order_id>', methods=['GET', 'POST'])
@login_required
def pay_order(order_id):
    payment = request.form.get('payment')
    import importlib
    paymodel_path = "xp_cms.pay."+payment+".create_pay"
    module = importlib.import_module(paymodel_path)
    PayMethod = getattr(module, payment.title())
    print(paymodel_path)

    # exec("pay="+payment.title()+"()")
    # from xp_cms.pay.alipay.controller.create_pay import Alipay
    pay = PayMethod()
    order = Order.query.filter_by(id=order_id, status=0, buyer=current_user.user_id).first()
    if not order:
        return redirect(url_for('.index'))
    elif order.status == 1:
        return redirect(url_for('.show_lesson', lesson_id=order.lessons[0].id))

    # status 0:等待付款， 1：已付款，2：已发货，3 已收货
    if payment == "alipay":
        url = pay.pay_order(order)
        print(url)
        return redirect(url)
    else:
        res =  pay.pay_order(order)
        if res[0]:
            return jsonify(success=True, out_trade_no=order.order_no, code_url=res[1]['code_url'])
        else:
            return jsonify(success=False)

@csrf.exempt
@course_module.route('/pay/<string:payment>/<string:call_type>', methods=['GET', 'POST'])
def pay_confirm(payment, call_type):
    import importlib
    paymodel_path = "xp_cms.pay." + payment + ".create_pay"
    module = importlib.import_module(paymodel_path)
    PayMethod = getattr(module, payment.title())
    pay = PayMethod()
    res, order_info, out_html = pay.confirm_pay(request)
    if res:
        if call_type == "return":
            return "支付成功"
        elif call_type == "notify":
            out_trade_no = order_info['out_trade_no']
            order = Order.query.filter_by(order_no=out_trade_no,  status=0).first()
            total_price = order_info['total_price']
            if math.isclose(order.total_price,total_price):
                order.status=1
                order.payment=payment
                db.session.commit()
            return  out_html
    else:
        if call_type == "return":
            return "尚未到账，请稍后刷新页面"
        elif call_type == "notify":
            return  out_html

@course_module.route("/pay/status/<string:out_trade_no>", methods=['GET'])
@login_required
def get_order_status(out_trade_no):
    order = Order.query.filter_by(order_no=out_trade_no, buyer=current_user.user_id).first()
    print(order)
    print(order.id)
    print(order.status)
    if order.status == "1":
        print('ok')
        return jsonify(success='success')
    else:
        return jsonify(success="wait")






def get_order_no():
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+ str(time.time()).replace('.', '')[-7:]
    return order_no

def get_total_price(amout, course_id, discount=1):
    course = Course.query.get_or_404(id=course_id)
    total_price = amout * course.price
    return total_price, total_price, None