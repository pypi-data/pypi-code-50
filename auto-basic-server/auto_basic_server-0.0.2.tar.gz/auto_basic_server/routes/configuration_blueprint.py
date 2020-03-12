#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
文件名：configuration_blueprint.py
Created on 2019年07月12日
@author: 梁彦鹏
"""
import traceback
from common.configuration import *
from common.return_sign import *
from flask import Blueprint, request

configurate = Blueprint('configurate', __name__, url_prefix='/configurate')

@configurate.route('/get_ini_sections', methods=["POST", "GET"])
def get_ini_sections_route():
    try:
        res = request.get_json(force=True)
        result = get_ini_sections(ini_file=res.get('ini_file'))
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@configurate.route('/get_ini_options/', methods=["POST", "GET"])
def get_ini_options_route():
    try:
        res = request.get_json(force=True)
        result = get_ini_options(ini_file=res.get('ini_file'), section=res.get('section'))
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@configurate.route('/get_ini_option_val/', methods=["POST", "GET"])
def get_ini_option_val_route():
    try:
        res = request.get_json(force=True)
        result = get_ini_option_val(ini_file=res.get('ini_file'), section=res.get('section'), option=res.get('option'))
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()

@configurate.route('/set_ini_option_val/', methods=["POST", "GET"])
def set_ini_option_val_route():
    try:
        res = request.get_json(force=True)
        result = set_ini_option_val(ini_file=res.get('ini_file'), section=res.get('section'), option=res.get('option'),
                                    value=res.get('value'))
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except:
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()
