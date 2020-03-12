# -*- coding: utf-8 -*-

from flask import Blueprint, request
from common.autocfg import *
from common.return_sign import *
from common.logger import log
import traceback


auto_cfg = Blueprint('auto_cfg', __name__, url_prefix='/auto_cfg')

@auto_cfg.route('/GetCookiesPath', methods=["POST", "GET"])
def get_cookies_path_route():
    try:
        res = request.get_json(force=True)
        result = get_cookies_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetLocalApp', methods=["POST", "GET"])
def get_local_app_route():
    try:
        res = request.get_json(force=True)
        result = get_local_app(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetTempPath', methods=["POST", "GET"])
def get_temp_path_route():
    try:
        res = request.get_json(force=True)
        result = get_temp_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetWindowsTempPath', methods=["POST", "GET"])
def get_windows_temp_path_route():
    try:
        res = request.get_json(force=True)
        result = get_windows_temp_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetPublicPath', methods=["POST", "GET"])
def get_public_path_route():
    try:
        res = request.get_json(force=True)
        result = get_public_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetCommonApp', methods=["POST", "GET"])
def get_common_app_route():
    try:
        res = request.get_json(force=True)
        result = get_common_app(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetDesktopPath', methods=["POST", "GET"])
def get_desktop_path_route():
    try:
        res = request.get_json(force=True)
        result = get_desktop_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetStartMenuPath', methods=["POST", "GET"])
def get_start_menu_path_route():
    try:
        res = request.get_json(force=True)
        result = get_start_menu_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetCommonStartMenuPath', methods=["POST", "GET"])
def get_common_ctart_cenu_path_route():
    try:
        res = request.get_json(force=True)
        result = get_common_start_menu_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetFavoritePath', methods=["POST", "GET"])
def get_favorite_path_route():
    try:
        res = request.get_json(force=True)
        result = get_favorite_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetPersonalPath', methods=["POST", "GET"])
def get_personal_path_route():
    try:
        res = request.get_json(force=True)
        result = get_personal_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetDesktopDirectoryPath', methods=["POST", "GET"])
def get_desktop_directory_path_route():
    try:
        res = request.get_json(force=True)
        result = get_desktop_directory_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetCommonDesktopDirectoryPath', methods=["POST", "GET"])
def get_common_desktop_directory_path_route():
    try:
        res = request.get_json(force=True)
        result = get_common_desktop_directory_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetFontsPath', methods=["POST", "GET"])
def get_fonts_path_route():
    try:
        res = request.get_json(force=True)
        result = get_fonts_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetProGramsPath', methods=["POST", "GET"])
def get_programs_path_route():
    try:
        res = request.get_json(force=True)
        result = get_pro_grams_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetInternetCachePath', methods=["POST", "GET"])
def get_internet_cache_path_route():
    try:
        res = request.get_json(force=True)
        result = get_internet_cache_path(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetAppData', methods=["POST", "GET"])
def get_app_data_route():
    try:
        res = request.get_json(force=True)
        result = get_app_data(file_name=res['fileName'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@auto_cfg.route('/GetQuickLaunchPath', methods=["POST", "GET"])
def get_quick_launch_path_route():
    try:
        result = get_quick_launch_path()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()
