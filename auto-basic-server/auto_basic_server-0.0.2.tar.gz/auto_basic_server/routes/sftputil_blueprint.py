# -*- coding: utf-8 -*-
from common.return_sign import *
from flask import Blueprint, request
from common.sftputil import *

sftp_util = Blueprint('sftp_util', __name__, url_prefix='/sftp_util')


@sftp_util.route('/get_file', methods=["POST", "GET"])
def get_file_route():
    try:
        res = request.get_json(force=True)
        kwargs = res.get('kwargs')
        sftp_obj = Sftp(host=kwargs.get("host"), username=kwargs.get("username"), password=kwargs.get("password"))
        sftp_obj.get_file(remote_file=res.get('remote_file'), local_file=res.get('local_file'))
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@sftp_util.route('/put_file', methods=["POST", "GET"])
def put_file_route():
    try:
        res = request.get_json(force=True)
        kwargs = res.get('kwargs')
        sftp_obj = Sftp(host=kwargs.get("host"), username=kwargs.get("username"), password=kwargs.get("password"))
        sftp_obj.put_file(local_file=res.get('local_file'), remote_file=res.get('remote_file'))
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@sftp_util.route('/get_dir', methods=["POST", "GET"])
def get_dir_route():
    try:
        res = request.get_json(force=True)
        kwargs = res.get('kwargs')
        sftp_obj = Sftp(host=kwargs.get("host"), username=kwargs.get("username"), password=kwargs.get("password"))
        sftp_obj.get_dir(remote_dir=res.get('remote_dir'), local_dir=res.get('local_dir'))
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@sftp_util.route('/put_dir', methods=["POST", "GET"])
def put_dir_route():
    try:
        res = request.get_json(force=True)
        kwargs = res.get('kwargs')
        sftp_obj = Sftp(host=kwargs.get("host"), username=kwargs.get("username"), password=kwargs.get("password"))
        sftp_obj.put_dir(local_dir=res.get('local_dir'), remote_dir=res.get('remote_dir'))
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()
