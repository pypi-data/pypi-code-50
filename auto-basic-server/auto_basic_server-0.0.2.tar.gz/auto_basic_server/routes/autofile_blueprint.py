# -*- coding: utf-8 -*-
import json
import traceback
from common.autofile import *
from common.return_sign import *
from flask import Blueprint, request

auto_file = Blueprint('auto_file', __name__, url_prefix='/auto_file')


@auto_file.route('/getNormalPath/', methods=["POST", "GET"])
def get_normal_path_route():
    try:
        res = request.get_json(force=True)
        result = get_normal_path(path=res['path'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/existPath/', methods=["POST", "GET"])
def exist_path_route():
    try:
        res = request.get_json(force=True)
        result = exist_path(path=res['path'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/createFolder/', methods=["POST", "GET"])
def create_folder_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = create_folder(path=res['path'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/createFile/', methods=["POST", "GET"])
def create_file_route():
    try:
        res = request.get_json(force=True)
        result = create_file(path=res['path'], content=res['content'], mode=res['mode'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/getFileSize/', methods=["POST", "GET"])
def get_file_size_route():
    try:
        res = request.get_json(force=True)
        result = get_file_size(file_path=res['filePath'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/setFileData/', methods=["POST", "GET"])
def set_file_data_route():
    try:
        res = request.get_json(force=True)
        result = set_file_data(file_path=res['file_path'], mode=res['mode'], data=res['data'], encoding=res.get('encoding'))
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/getFileData/', methods=["POST", "GET"])
def get_file_data_route():
    try:
        res = request.get_json(force=True)
        result = get_file_data(file_path=res['file_path'], mode=res['mode'], encoding=res.get('encoding'))
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/copyFile/', methods=["POST", "GET"])
def copy_file_route():
    try:
        res = request.get_json(force=True)
        result = copy_file(source_file=res['sourceFile'], dest_file=res['destFile'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/renameFile/', methods=["POST", "GET"])
def rename_file_route():
    try:
        res = request.get_json(force=True)
        result = rename_file(source_file=res['sourceFile'], dest_file=res['destFile'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/listFile/', methods=["POST", "GET"])
def list_file_route():
    try:
        res = request.get_json(force=True)
        result = list_file(remote_path=res['remotePath'], exclude=res['exclude'], is_deep=res['isDeep'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/get_newest_file_list/', methods=["POST", "GET"])
def get_newest_file_list_route():
    try:
        data = request.get_json(force=True)
        result = get_newest_file_list(remote_path=data.get('remotePath'), is_deep=data.get('isDeep'))
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/deleteFile/', methods=["POST", "GET"])
def delete_file_route():
    try:
        res = request.get_json(force=True)
        result = delete_file(path=res['path'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/copyFolder/', methods=["POST", "GET"])
def copy_folder_route():
    try:
        res = request.get_json(force=True)
        result = copy_folder(source_folder=res['sourceFolder'], dest_folder=res['destFolder'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/deleteFolder/', methods=["POST", "GET"])
def delete_folder_route():
    try:
        res = request.get_json(force=True)
        result = delete_folder(path=res['path'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/md5File', methods=["POST", "GET"])
def md5_file_route():
    try:
        res = request.get_json(force=True)
        result = md5_file(path=res['path'], size=res['size'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/sha1File', methods=["POST", "GET"])
def sha1_file_route():
    try:
        res = request.get_json(force=True)
        result = sha1_file(path=res['path'], size=res['size'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/un_zip/', methods=["POST", "GET"])
def unzip_route():
    try:
        res = request.get_json(force=True)
        unzip(source_path=res.get('source_path'), dest_path=res.get('dest_path'), pwd=res.get('pwd'))
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/download_file_by_url/', methods=["POST", "GET"])
def download_file_by_url_route():
    try:
        data = request.get_json(force=True)
        result = download_file_by_url(url=data.get('url'), file_path=data.get('file_path'))
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/read_contents_of_lipboard/', methods=["POST", "GET"])
def read_contents_of_lipboard_route():
    try:
        result = read_contents_of_lipboard()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/excel_read_file/', methods=["POST", "GET"])
def excel_read_route():
    try:
        data = request.get_json(force=True)
        result = excel_read_file(file_path=data.get('file_path'), row_index=data.get('row'), col=data.get('col'))
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/PandaExcel/', methods=["POST", "GET"])
def panda_excel_route():
    try:
        data = request.get_json(force=True)
        global df
        df = PandaExcel(excel_file_path=data.get('excel_file_path'))
        return RestResult(ERROR_SUCCESS, data=True, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_file.route('/get_rows_num/', methods=["POST", "GET"])
def get_rows_num_route():
    try:
        rows_num = df.get_rows_num()
        return RestResult(ERROR_SUCCESS, data=rows_num, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()
