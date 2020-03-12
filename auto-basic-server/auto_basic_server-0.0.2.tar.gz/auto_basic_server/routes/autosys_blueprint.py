# -*- coding: utf-8 -*-
import traceback
from common.autosys import *
from common.autoutil import grab_screen
from common.return_sign import *
from flask import Blueprint, request, make_response, send_file
from common.logger import log

auto_sys = Blueprint('auto_sys', __name__, url_prefix='/auto_sys')


@auto_sys.route('/isWinSystem', methods=["POST", "GET"])
def is_win_system_route():
    try:
        result = is_win_system()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception as e:
        log.error(e)
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_sys.route('/getHostName', methods=["POST", "GET"])
def get_host_name_route():
    try:
        result = get_host_name()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_sys.route('/get_system_type', methods=["POST", "GET"])
def get_system_type_route():
    try:
        result = get_system_type()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_sys.route('/isWin64', methods=["POST", "GET"])
def is_win64_route():
    try:
        result = is_win64()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_sys.route('/getOSName', methods=["POST", "GET"])
def get_os_name_route():
    try:
        result = get_os_name()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_sys.route('/getOSVersion', methods=["POST", "GET"])
def get_os_version_route():
    try:
        result = get_os_version()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_sys.route('/GetPhysMemorySize', methods=["POST", "GET"])
def get_phys_memory_size_route():
    try:
        result = get_phys_memory_size()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_sys.route('/save_screenshot', methods=["POST"])
def save_screenshot():
    try:
        data = request.get_json(force=True)
        save_path = data.get('pic_path')
        # result = take_screen_shot(save_path)
        result = grab_screen(path=save_path)
        if result:
            response = make_response(send_file(save_path))
            response.headers["Content-Disposition"] = "attachment; filename={};".format(os.path.basename(save_path))
            return response
        else:
            return make_response(('save image failed', 201))
    except:
        log.error(traceback.format_exc())