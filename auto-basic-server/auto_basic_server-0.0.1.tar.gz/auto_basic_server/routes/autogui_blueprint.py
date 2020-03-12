# -*- coding: utf-8 -*-
import json
import traceback
from flask import Blueprint, request
from common.autogui import *
from common.return_sign import *

auto_gui = Blueprint('auto_gui', __name__, url_prefix='/auto_gui')


@auto_gui.route('/clickWindow/', methods=["POST"])
def click_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = click_window(h_wnd=res['hwnd'], clk_cfg=res['clkCfg'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/clickWindowFor/', methods=["POST"])
def click_window_for_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = click_window_for(res['hwnd'], res['timeout'], res['cond'], res['clkCfg'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/clickWindowForClose/', methods=["POST"])
def click_window_for_close_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = click_window_for_close(res['hwnd'], res['timeout'], res['tgtHwnd'], res['clkCfg'])
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/clickWindowForCloseSelf/', methods=["POST", "GET"])
def click_window_for_close_self_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = click_window_for_close_self(h_wnd=res['hwnd'], timeout=res['timeout'], clk_cfg=res['clkCfg'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/clickWindowForFind/', methods=["POST", "GET"])
def click_window_for_find_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = click_window_for_find(h_wnd=res['hwnd'], timeout=res['timeout'], title_cfg=res['titleCfg'],
                                       clk_cfg=res['clkCfg'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/clickWindowForFindChild/', methods=["POST", "GET"])
def click_window_for_find_child_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = click_window_for_find_child(h_wnd=res['hwnd'], timeout=res['timeout'], title_cfg=res['titleCfg'],
                                             clk_cfg=res['clkCfg'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/clickWindowForHidden/', methods=["POST", "GET"])
def click_window_for_hidden_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = click_window_for_hidden(h_wnd=res['hwnd'], timeout=res['timeout'], tgt_hwnd=res['tgtHwnd'],
                                         clk_cfg=res['clkCfg'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/clickWindowForHiddenSelf/', methods=["POST", "GET"])
def click_window_for_hidden_self_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = click_window_for_hidden_self(h_wnd=res['hwnd'], timeout=res['timeout'], clk_cfg=res['clkCfg'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/findRawWindow/', methods=["POST", "GET"])
def find_raw_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = find_raw_window(title=res['title'], parent_title=res['parentTitle'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/findRawWindows/', methods=["POST", "GET"])
def find_raw_windows_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = find_raw_windows(title=res['title'], parent_title=res['parentTitle'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/findWindow/', methods=["POST", "GET"])
def find_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = find_window(title=res['title'], parent_title=res['parentTitle'], is_raw=res['isRaw'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/findWindows/', methods=["POST", "GET"])
def find_windows_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = find_windows(title=res['title'], parent_title=res['parentTitle'], is_raw=res['isRaw'],
                              return_first=res['returnFirst'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/getDesktopRect/', methods=["POST", "GET"])
def get_desktop_rect_route():
    try:
        result = get_desktop_rect()
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/getParentWindow/', methods=["POST", "GET"])
def get_parent_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = get_parent_window(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/getWindowClass/', methods=["POST", "GET"])
def get_window_class_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = get_window_class(res['hwnd'], res['buf'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/getWindowRect/', methods=["POST", "GET"])
def get_window_rect_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = get_window_rect(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/getWindowSize/', methods=["POST", "GET"])
def get_window_size_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = get_window_size(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/findWindowWithSize/', methods=["POST", "GET"])
def find_window_with_size_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = find_window_with_size(title=res['title'], size=res['size'], parent_title=res['parentTitle'],
                                       is_raw=res['isRaw'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/getWindowText/', methods=["POST", "GET"])
def get_window_text_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = get_window_text(res['hwnd'], res['buf'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/setWindowText/', methods=["POST", "GET"])
def set_window_text_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = set_window_text(h_wnd=res['hwnd'], text=res['text'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/isRawWindow/', methods=["POST", "GET"])
def is_raw_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = is_raw_window(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/normalWindow/', methods=["POST", "GET"])
def normal_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = normal_window(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/maxWindow/', methods=["POST", "GET"])
def max_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = max_window(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/minWindow/', methods=["POST", "GET"])
def min_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = min_window(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/showWindow/', methods=["POST", "GET"])
def show_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = show_window(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/topWindow/', methods=["POST", "GET"])
def top_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = top_window(h_wnd=res['hwnd'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/moveWindow/', methods=["POST", "GET"])
def move_window_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = move_window(h_wnd=res['hwnd'], x=res['x'], y=res['y'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/moveWindowByClick/', methods=["POST", "GET"])
def move_window_by_click_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = move_window_by_click(h_wnd=res['hwnd'], x=res['x'], y=res['y'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/alertMessage/', methods=["POST", "GET"])
def alert_message_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = alert_message(msg=res['msg'], text=res['text'], style=res['style'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/alertError/', methods=["POST", "GET"])
def alert_error_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = alert_error(error=res['error'], text=res['text'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/alertChoice/', methods=["POST", "GET"])
def alert_choice_route():
    try:
        data = request.get_data()
        res = json.loads(data)
        result = alert_choice(choice=res['choice'], text=res['text'])
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/GUICtrlTreeView_SelectItem/', methods=["POST", "GET"])
def gui_ctrl_tree_view_select_item_route():
    try:
        data = request.get_json(force=True)
        result = gui_ctrl_tree_view_select_item(h_wnd=data.get('hWnd'), h_item=data.get('hItem'), i_flag=data.get('iFlag'))
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/GUICtrlTreeView_FindItemEx/', methods=["POST", "GET"])
def gui_ctrl_tree_view_find_item_ex_route():
    try:
        data = request.get_json(force=True)
        result = gui_ctrl_tree_view_find_item_ex(tree_wnd=data.get('tree_wnd'), target_path=data.get('target_path'))
        if isinstance(result, bytes):
            result = result.decode()
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()


@auto_gui.route('/window_click_button/', methods=["POST", "GET"])
def window_click_button_route():
    try:
        data = request.get_json(force=True)
        result = window_click_button(str_class=data.get('str_class'), str_caption=data.get('str_caption'), str_button_text=data.get('str_button_text'))
        return RestResult(ERROR_SUCCESS, data=result, msg="Success").to_json()
    except Exception:
        log.error(traceback.format_exc())
        return RestResult(ERROR_RUN_EXCEPT, data=False, msg=traceback.format_exc()).to_json()
