# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from common.autoinput import *
from common.return_sign import *
auto_input = Blueprint('auto_input', __name__, url_prefix='/auto_input')


@auto_input.route('/clickMouse/', methods=["POST", "GET"])
def click_mouse_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        click_mouse(x=res['x'], y=res['y'], mode=res['mode'], move_wait_time=res['move_wait_time'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_input.route('/clickMouseDouble/', methods=["POST", "GET"])
def click_mouse_double_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        click_mouse_double(x=res['x'], y=res['y'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_input.route('/clickMouseRight/', methods=["POST", "GET"])
def click_mouse_right_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        click_mouse_right(x=res['x'], y=res['y'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_input.route('/moveMouse/', methods=["POST", "GET"])
def move_mouse_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        move_mouse(x=res['x'], y=res['y'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_input.route('/wheelMouse/', methods=["POST", "GET"])
def wheel_mouse_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        wheel_mouse(dw_data=res['dw_data'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_input.route('/getCursorPos/', methods=["POST", "GET"])
def get_cursor_pos_route():
    try:
        result = get_cursor_pos()
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()
