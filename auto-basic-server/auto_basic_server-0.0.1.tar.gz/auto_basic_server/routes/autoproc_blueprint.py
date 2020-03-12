# -*- coding: utf-8 -*-
import traceback
import json
from flask import Blueprint, request

from common.autoproc import *
from common.return_sign import *
from common.logger import log

auto_proc = Blueprint('auto_proc', __name__, url_prefix='/auto_proc')


@auto_proc.route('/exec_cmd', methods=["POST", "GET"])
def exec_cmd_route():
    try:
        rst = request.get_json(force=True)
        result = exec_cmd(cmd=rst['cmd'], cwd=rst.get('cwd'), is_wait=rst.get('is_wait'),
                          timeout=rst.get('timeout'))
        print(result)
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/existProcessByName', methods=["POST", "GET"])
def exist_process_by_name_route():
    try:
        res = request.get_json(force=True)
        result = exist_process_by_name(p_name=res['pname'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/existProcessByNames', methods=["POST", "GET"])
def exist_process_by_names_route():
    try:
        res = request.get_json(force=True)
        result = exist_process_by_names(pname_list=res['pname_list'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/get_process_info_by_pname', methods=["POST", "GET"])
def get_process_info_by_pname_route():
    try:
        res = request.get_json(force=True)
        result = get_process_info_by_pname(p_name=res['pname'], process_type=res["process_type"])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/get_process_info_by_pid', methods=["POST", "GET"])
def get_process_info_by_pid_route():
    try:
        res = request.get_json(force=True)
        result = get_process_info_by_pid(pid=res['pid'], process_type=res["process_type"])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/get_process_info_by_cmdline', methods=["POST", "GET"])
def get_process_info_by_cmdline_route():
    try:
        res = request.get_json(force=True)
        result = get_process_info_by_cmdline(cmd_line=res['cmd_line'], process_type=res["process_type"])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/get_process_info_list_by_name', methods=["POST", "GET"])
def get_process_info_list_by_name_route():
    try:
        res = request.get_json(force=True)
        result = get_process_info_list_by_pname(p_name=res['p_name'], process_type=res["process_type"])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/get_process_info_list_by_username', methods=["POST", "GET"])
def get_process_info_list_by_username_route():
    try:
        res = request.get_json(force=True)
        result = get_process_info_list_by_username(user_name=res['user_name'], process_type=res["process_type"])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/killProcessByName', methods=["POST", "GET"])
def kill_process_by_name_route():
    try:
        res = request.get_json(force=True)
        kill_process_by_name(p_name=res['pname'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/killProcessByNames', methods=["POST", "GET"])
def kill_process_by_names_route():
    try:
        res = request.get_json(force=True)
        kill_process_by_names(pname_list=res['pnameList'], user=res['user'])
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/kill_process_by_cmd_line', methods=["POST", "GET"])
def kill_process_by_cmd_line_route():
    try:
        res = request.get_json(force=True)
        result = kill_process_by_cmd_line(cmd_line=res['cmd_line'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_proc.route('/kill_process_by_id', methods=["POST", "GET"])
def kill_process_by_id_route():
    try:
        res = request.get_json(force=True)
        result = kill_process_by_id(pid=res['pid'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/kill_process_by_ids', methods=["POST", "GET"])
def kill_process_by_ids_route():
    try:
        res = request.get_json(force=True)
        result = kill_process_by_ids(pid_list=res['pid_list'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_proc.route('/showProcessCpuPercent', methods=["POST", "GET"])
def show_process_cpu_percent_by_id_route():
    try:
        res = request.get_json(force=True)
        result = show_process_cpu_percent_by_id(pid=res['pid'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()
