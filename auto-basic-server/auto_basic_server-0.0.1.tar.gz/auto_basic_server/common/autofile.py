# -*- coding: utf-8 -*-
"""
常用文件操作
"""
import hashlib
import shutil
import os
import zipfile
from common.logger import log
from common.autosys import Local_Ip

def get_normal_path(path):
    """
    替换路径中的环境变量为正常路径
    path: 路径，其中可以包含系统环境变量，如%appdata%等
    """
    import win32api
    tmp_path = os.path.expandvars(path)
    if os.path.exists(tmp_path):
        tmp_path = win32api.GetLongPathName(tmp_path)
    return tmp_path


def exist_path(path):
    """判断文件是否存在"""
    print("version:2.0.0")
    return os.path.exists(path)


def create_folder(path):
    """创建文件夹"""
    if not os.path.exists(path):
        os.makedirs(path)
    if os.path.exists(path):
        return True
    raise Exception("IP:{local_ip}创建文件夹：{0}失败".format(path, local_ip=Local_Ip))


def create_file(path, content='', mode='w'):
    """创建文件"""
    index = path.rfind(os.sep)
    if index > 0:
        if not exist_path(path[0:index]):
            os.makedirs(path[0:index])
    with open(path, mode) as f:
        if content:
            f.write(content)
    return path


def get_file_size(file_path):
    """获取文件大小"""
    return os.path.getsize(file_path)


def set_file_data(file_path, data, mode="w", encoding="utf-8"):
    """设置文件"""
    if not os.path.exists(file_path):
        log.error('IP:{local_ip}不存在路径:{0}'.format(file_path, local_ip=Local_Ip))
        raise Exception('IP:{local_ip}不存在路径:{0}'.format(file_path, local_ip=Local_Ip))
    with open(file_path, mode=mode, encoding=encoding) as file:
        file.write(data)
    return True


def get_file_data(file_path, mode='r', encoding='utf-8'):
    """获取文件内容"""
    if not os.path.exists(file_path):
        log.error('IP:{local_ip}文件:{0}不存在'.format(file_path, local_ip=Local_Ip))
        raise Exception('IP:{local_ip}文件:{0}不存在'.format(file_path, local_ip=Local_Ip))
    with open(file_path, mode, encoding=encoding) as f:
        data = f.read()
        return data


def copy_file(source_file, dest_file):
    """拷贝文件"""
    if not os.path.exists(source_file):
        log.error('IP:{local_ip}文件:{0}不存在'.format(source_file, local_ip=Local_Ip))
        raise Exception('IP:{local_ip}文件:{0}不存在'.format(source_file, local_ip=Local_Ip))
    dest_path = os.path.dirname(dest_file)
    if not os.path.exists(dest_path):
        create_folder(dest_path)
    if shutil.copyfile(source_file, dest_file):
        return True
    raise Exception('IP:{local_ip}拷贝文件从{0}到{1}失败'.format(source_file, dest_file, local_ip=Local_Ip))


def rename_file(source_file, dest_file):
    """文件重命名"""
    if not os.path.exists(source_file):
        log.error("IP:{local_ip}文件：{0}不存在".format(source_file, local_ip=Local_Ip))
        return False
    source_folder = os.path.dirname(source_file)
    dest_file = os.path.join(source_folder, os.path.basename(dest_file))
    if os.path.exists(dest_file):
        os.remove(dest_file)
    os.rename(source_file, dest_file)
    return True


def __list_file__(path, is_deep=True):
    # name:
    import glob
    _list = []
    if is_deep:
        for root, dirs, files in os.walk(path):
            for fl in files:
                _list.append(os.path.join(root, fl))

    else:
        for fn in glob.glob(path + os.sep + '*'):
            if not os.path.isdir(fn):
                _list.append(os.path.join(path, fn[fn.rfind(os.sep) + 1:]))
    return _list


def list_file(remote_path, exclude=None, is_deep=True):
    """列举路径下所有文件
    
    :param remote_path: 远程路径
    :param exclude: list， 排除列表内的文件
    :param is_deep: 是否深度遍历
    :return:
    """
    _del_list = []
    # 本地
    _list = __list_file__(remote_path, is_deep)
    if not _list:
        return _list

    if exclude and type(exclude) == list:
        for extFile in exclude:
            for fp in _list:
                if extFile.lower() == os.path.basename(fp).lower():
                    _del_list.append(fp)
    if _del_list:
        for delfp in _del_list:
            _list.remove(delfp)
    return _list


def get_newest_file_list(remote_path, is_deep=True):
    """获取最近更改的文件列表"""
    file_dict = dict()
    _list = __list_file__(remote_path, is_deep)
    if not _list:
        log.error("遍历文件出现错误")
        return _list
    for file in _list:
        file_update_time = os.path.getmtime(file)
        if file_update_time not in file_dict.keys():
            file_dict[file_update_time] = list()
            file_dict[file_update_time].append(file)
        else:
            file_dict[file_update_time].append(file)

    newest_time = max(file_dict.keys())
    return file_dict[newest_time]


def delete_file(path):
    """删除文件"""
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
    if not os.path.exists(path):
        return True
    raise Exception('IP:{local_ip}删除文件：{0}失败'.format(path, local_ip=Local_Ip))


def copy_folder(source_folder, dest_folder):
    """拷贝文件夹"""
    shutil.copytree(source_folder, dest_folder)
    if os.path.isdir(dest_folder) and os.listdir(dest_folder):
        return True
    raise Exception("IP:{local_ip}拷贝文件夹从{0}到{1}失败".format(source_folder, dest_folder, local_ip=Local_Ip))


def delete_folder(path):
    """删除文件夹"""
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
    if os.path.exists(path):
        raise Exception("IP:{local_ip}删除文件夹{0}失败".format(path, local_ip=Local_Ip))
    return True


def md5_file(path, size=32768):
    """计算文件md5"""
    m = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            d = f.read(size)
            if not d:
                break
            m.update(d)
    return m.hexdigest()


def sha1_file(path, size=32768):
    """计算文件sha1"""
    m = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            d = f.read(size)
            if not d:
                break
            m.update(d)
    return m.hexdigest()


def unzip(source_path=None, dest_path=None, pwd=None):
    """用于解压ZIP文件
    
    :param pwd:         解压密码
    :param source_path: 源文件目录
    :param dest_path:  目标文件目录
    :return:
    """
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    if pwd and not isinstance(pwd, bytes):
        pwd = pwd.encode()

    with zipfile.ZipFile(source_path, 'r') as zipF:
        for file in zipF.namelist():
            zipF.extract(file, dest_path, pwd)
        return True


def download_file_by_url(url, file_path):
    """通过url下载文件"""
    import requests
    r = requests.get(url, stream=True)

    index = file_path.rfind(os.sep)
    if index > 0:
        if not exist_path(file_path[0:index]):
            create_folder(file_path[0:index])

    with open(file_path, "wb") as file:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
        r.close()
        return True


def read_contents_of_lipboard():
    """读取剪切板内容"""
    from tkinter import Tk
    r = Tk()
    clipboard_content = r.clipboard_get()
    return clipboard_content


def excel_read_file(file_path, row_index=None, col=None):
    import pandas as pd
    """读取Excel表中内容，默认返回整表 只支持（int，int）,(int,None),(None,list(str))(list[int],list[str])

    :param file_path: Excel文件路径
    :param row_index: 行信息（只支持int和list[int]）,下标从0开始，（不包含列名信息）
    :param col: 列信息 只支持int、list[str]  下标从0开始
    :return: str或list[str]
    """
    if not os.path.exists(file_path):
        log.error("不存在文件{0}".format(file_path))
        raise Exception("不存在文件{0}".format(file_path))
    df = pd.read_excel(file_path)
    if isinstance(row_index, int) and isinstance(col, int):
        ret = df.iat[row_index, col]
        result = str(ret)
    elif isinstance(row_index, int) and not col:
        result = []
        if row_index == 0:
            rst = df.columns
        else:
            rst = df.iloc[row_index]
        for i in rst:
            result.append(i)
    elif isinstance(col, list) and not row_index:
        result = []
        for col_obj in col:
            datas = df.get(col_obj)
            for dd in datas:
                result.append(dd)
    elif isinstance(col, list) and isinstance(row_index, list):
        tmp_list = []
        for col_obj in col:
            datas = df.get(col_obj)
            for index in row_index:
                tmp_list.append(datas[index])
        result = tmp_list
    else:
        data_list = list()
        for column in df.columns:
            tmp_list = []
            datas = df.get(column)
            for dd in datas:
                tmp_list.append(str(dd))
            data_list.append(tmp_list)
        result = data_list
    return result


class PandaExcel:
    def __init__(self, excel_file_path):
        import pandas as pd
        self._df = pd.read_excel(excel_file_path)

    def read_excel_by_sheet(self, excel_file, sheet_name: list):
        import pandas as pd
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        data = df.values()
        return data

    def get_columns(self):
        return self._df.columns

    def get_rows_num(self):
        return len(self._df.index.values)


if __name__ == "__main__":
    print(exist_path("C:\config.ini"))
    # file_path = "D:\\11.xlsx"
    # p_excel = PandaExcel(file_path)
    # print(p_excel.get_columns())
    # print(p_excel.get_rows_num())

    # delete_folder("C:\A1")
