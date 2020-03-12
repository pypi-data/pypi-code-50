"""
文件名：timesync_blueprint.py
Created on 2019年04月29日
@author: 马红亮
"""
import json
import traceback

from flask import Blueprint, request

from common.return_sign import *
from common.timesync import *
from common.logger import log

time_sync = Blueprint('time_sync', __name__, url_prefix='/timesync')


@time_sync.route('/get_current_time', methods=["POST", "GET"])
def get_current_time_route():
    try:
        res = request.get_json(force=True)
        result = get_current_time(days=res.get('days'), time_format=res.get('time_format'))
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Exec_Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@time_sync.route('/syn_time_from_timeserver', methods=["POST", "GET"])
def syn_time_from_time_server_route():
    try:
        syn_time_from_timeserver()
        return RestResult(ERROR_SUCCESS, data=True, msg="Exec_Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@time_sync.route('/setCurrentTime', methods=["POST", "GET"])
def set_current_time_route():
    try:
        res = request.get_json(force=True)
        result = set_current_time(s_date=res['sDate'], s_time=res['sTime'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@time_sync.route('/edit_time', methods=["POST", "GET"])
def edit_time_route():
    try:
        res = request.get_json(force=True)
        edit_time(days=res.get('days'), hours=res.get('hours'), minutes=res.get('minutes'), seconds=res.get('seconds'))
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


