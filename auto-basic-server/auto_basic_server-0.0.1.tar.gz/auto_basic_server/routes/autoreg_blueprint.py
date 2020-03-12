# -*- coding: utf-8 -*-
import traceback
from common.autoreg import *
from common.return_sign import *
from flask import Blueprint, request
from common.logger import log

auto_reg = Blueprint('auto_reg', __name__, url_prefix='/auto_reg')


@auto_reg.route('/hasKey', methods=["POST", "GET"])
def has_key_route():
    try:
        res = request.get_json(force=True)
        result = has_key(key_full_name=res['keyFullName'], re_direct=res['reDirect'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/delKey', methods=["POST", "GET"])
def del_key_route():
    try:
        res = request.get_json(force=True)
        result = del_key(key_full_name=res['keyFullName'], re_direct=res['reDirect'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/addKey', methods=["POST", "GET"])
def add_key_route():
    try:
        res = request.get_json(force=True)
        result = add_key(key_full_name=res['keyFullName'], re_direct=res['reDirect'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/getKeyValue', methods=["POST", "GET"])
def get_key_value_route():
    try:
        res = request.get_json(force=True)
        result = get_key_value(key_full_name=res['keyFullName'], value_name=res['valueName'], re_direct=res['reDirect'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/getMultiKeyValue', methods=["POST", "GET"])
def get_multi_key_value_route():
    try:
        res = request.get_json(force=True)
        result = get_multi_key_value(key_full_name=res['keyFullName'], value_name=res['valueName'], re_direct=res['reDirect'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/hasKeyValue', methods=["POST", "GET"])
def has_key_value_route():
    try:
        res = request.get_json(force=True)
        result = has_key_value(key_full_name=res['keyFullName'], value_name=res['valueName'], re_direct=res['reDirect'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/setKeyValue', methods=["POST", "GET"])
def set_key_value_route():
    try:
        res = request.get_json(force=True)
        result = set_key_value(key_full_name=res['keyFullName'], value_name=res['valueName'], value_type=res['type'],
                               value=res['value'], re_direct=res['reDirect'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/delKeyValue', methods=["POST", "GET"])
def del_key_value_route():
    try:
        res = request.get_json(force=True)
        result = del_key_value(key_full_name=res['keyFullName'], value_name=res['valueName'], re_direct=res['reDirect'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/backupKey', methods=["POST", "GET"])
def back_up_key_route():
    try:
        res = request.get_json(force=True)
        backup_key(key_full_name=res['keyFullName'], backup_file_name=res['backupFileName'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/restoreKey', methods=["POST", "GET"])
def restore_key_route():
    try:
        res = request.get_json(force=True)
        restore_key(key_full_name=res['keyFullName'], backup_file_name=res['backupFileName'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/importRegFile', methods=["POST", "GET"])
def import_reg_file_route():
    try:
        res = request.get_json(force=True)
        import_reg_file(reg_file=res['regFile'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/exportKey', methods=["POST", "GET"])
def export_key_route():
    try:
        res = request.get_json(force=True)
        result = export_key(key_full_name=res['keyFullName'], export_file_name=res['exportFileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/transKeyName', methods=["POST", "GET"])
def trans_key_name_route():
    try:
        res = request.get_json(force=True)
        result = trans_key_name(key_name=res['keyName'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/getRegTreeInfo', methods=["POST", "GET"])
def get_reg_tree_info_route():
    try:
        res = request.get_json(force=True)
        result = get_reg_tree_info(key_full_name=res['keyFullName'], open_key=res['open_key'], re_direct=res['reDirect'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/enumRegValues', methods=["POST", "GET"])
def enum_reg_values_route():
    try:
        res = request.get_json(force=True)
        result = enum_reg_values(key_full_name=res['keyFullName'], re_direct=res['reDirect'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_reg.route('/reMatchRegKey', methods=["POST", "GET"])
def re_match_reg_key_route():
    try:
        res = request.get_json(force=True)
        result = re_match_reg_key(key_full_name=res['keyFullName'], re_direct=res['reDirect'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()
