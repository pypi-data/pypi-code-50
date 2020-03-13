import csv
import hashlib
import pathlib
import tempfile
import time
from typing import List, Optional, Union, Dict

import gridfs
import pydicom
import pymongo
import requests
import vtk
from PySide2.QtWidgets import QDialog, QSizePolicy, QVBoxLayout, QDialogButtonBox, QComboBox

import vmi

client = pymongo.MongoClient('mongodb://root:medraw123@192.168.11.122:27017/admin', 27017)
database = client.skyward
case_db = database.get_collection('case')
dicom_fs = gridfs.GridFS(database, collection='dicom')
vti_fs = gridfs.GridFS(database, collection='vti')
vtp_fs = gridfs.GridFS(database, collection='vtp')
stl_fs = gridfs.GridFS(database, collection='stl')
stp_fs = gridfs.GridFS(database, collection='stp')
customer_db = database.get_collection('customer')


def ask_customer_uid() -> Optional[dict]:
    sizep = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

    dialog = QDialog()
    dialog.setSizePolicy(sizep)
    dialog.setWindowTitle('选择顾客')
    dialog.setLayout(QVBoxLayout())
    dialog.setMinimumWidth(200)

    customer_combo = QComboBox()
    for i in customer_db.find():
        customer_combo.addItem('{} {} {}'.format(i['customer_uid'], i['name'], i['sales']), i['customer_uid'])
        dialog.layout().addWidget(customer_combo)

    ok_cancel = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
    ok_cancel.setSizePolicy(sizep)
    ok_cancel.accepted.connect(dialog.accept)
    ok_cancel.rejected.connect(dialog.reject)
    dialog.layout().addWidget(ok_cancel)

    if dialog.exec_() == QDialog.Accepted:
        return customer_combo.currentData()
    else:
        return None


def dicom_kw_value(f: str) -> dict:
    kw_value = {}
    with pydicom.dcmread(f) as ds:
        for e in ds.iterall():
            if e.value.__class__ in [None, bool, int, float, str]:
                kw_value[e.keyword] = e.value
            elif e.value.__class__ in [bytes]:
                kw_value[e.keyword] = '{} bytes'.format(len(e.value))
            else:
                kw_value[e.keyword] = str(e.value)
    return {kw: kw_value[kw] for kw in sorted(kw_value)}


def case(product_uid: str,
         patient_name: str, patient_sex: str, patient_age: str,
         dicom_files: dict, vti_files: dict, vtp_files: dict, stl_files: dict, stp_files: dict,
         **kwargs) -> Optional[dict]:
    """
    构造本地案例
    :param product_uid: 产品识别码
    :param patient_name: 患者姓名
    :param patient_sex: 患者性别
    :param patient_age: 患者年龄
    :param dicom_files: 原始DICOM文件，每个关键词索引一个文件列表
    :param vti_files: vtkXMLImageData格式文件，每个关键词索引一个文件
    :param vtp_files: vtkXMLPolyData格式文件，每个关键词索引一个文件
    :param stl_files: STL格式文件，每个关键词索引一个文件
    :param stp_files: STEP格式文件，每个关键词索引一个文件
    :param kwargs: 其它相关信息，每个关键词索引一个支持数据库直接录入的对象
    :return: 案例信息
    """
    case_data = {}

    # 上传原始DICOM文件
    for kw in dicom_files:
        sop_uids = []
        for f in dicom_files[kw]:
            sop_uid = pydicom.dcmread(f).SOPInstanceUID
            sop_uids.append(sop_uid)

            if not dicom_fs.exists({'SOPInstanceUID': sop_uid}):
                dicom_fs.put(open(f, 'rb').read(), **dicom_kw_value(f))
        case_data[kw] = sop_uids

    # 上传其它格式文件
    files = [vti_files, vtp_files, stl_files, stp_files]
    fs = [vti_fs, vtp_fs, stl_fs, stp_fs]
    for i in range(len(files)):
        for kw in files[i]:
            f_bytes = open(files[i][kw], 'rb').read()
            md5 = hashlib.md5(f_bytes).hexdigest()

            if fs[i].exists({'md5': md5}):
                case_data[kw] = fs[i].find_one({'md5': md5})._id
            else:
                case_data[kw] = fs[i].put(f_bytes)

    # 上传其它信息
    case_data['product_uid'] = product_uid
    case_data['patient_name'] = patient_name
    case_data['patient_sex'] = patient_sex
    case_data['patient_age'] = patient_age

    for kw in kwargs:
        case_data[kw] = kwargs[kw]
    return case_data


def case_sync(case: dict, ukw: list) -> Optional[dict]:
    """
    同步案例
    :param case: 本地案例信息
    :param ukw: 特征键列表，用于判断相同案例
    :return: 同步后的案例信息
    """
    case['customer_confirmed'] = False

    ukw_value = {kw: case[kw] for kw in ukw}

    # 清理相同无效案例
    for c in case_db.find(ukw_value):
        if 'case_uid' not in c:
            case_db.delete_one({'_id': c['_id']})

    # 查找相同有效案例
    find = case_db.find_one(ukw_value)

    if find and 'case_uid' in find:
        if find['customer_confirmed']:
            vmi.askInfo('顾客已确认')
        r = vmi.askButtons(['下载存档', '上传存档'])
    else:
        r = vmi.askButtons(['创建存档'])

    if r == '创建存档':
        # 选择客户
        customer_uid = ask_customer_uid()
        if customer_uid:
            case['customer_uid'] = customer_uid

            _id = case_db.insert_one(case).inserted_id
            case_uid = vmi.convert_base(round(time.time() * 100))
            try:
                response = requests.post(url='http://med-3d.top:2334/sys/caseCreate',
                                         headers={'_id': str(_id), 'case_uid': case_uid})
                if response.text == 'true':
                    find = case_db.find_one({'_id': _id})
                    if 'case_uid' in find:
                        return case_db.find_one({'_id': _id})
                    else:
                        case_db.delete_one({'_id': _id})
                        vmi.askInfo('创建失败: 云端未分配编号')
                else:
                    case_db.delete_one({'_id': _id})
                    vmi.askInfo('创建失败: ' + response.text)
            except Exception as e:
                case_db.delete_one({'_id': _id})
                vmi.askInfo('网络错误: ' + str(e))
    elif r == '上传存档':
        case_uid = vmi.convert_base(round(time.time() * 100))
        try:
            response = requests.post(url='http://med-3d.top:2334/sys/caseUpdate',
                                     headers={'_id': str(find['_id']), 'case_uid': case_uid})
            if response.text == 'true':
                case_db.update_one({'_id': find['_id']}, {'$set': case})
                return case_db.find_one({'_id': find['_id']})
            else:
                vmi.askInfo('上传失败: ' + response.text)
        except Exception as e:
            case_db.delete_one({'_id': find['_id']})
            vmi.askInfo('网络错误: ' + str(e))
    elif r == '下载存档':
        return case_db.find_one({'_id': find['_id']})


def order(product_uid: str, case_uid: str,
          stl_files: dict, stp_files: dict,
          **kwargs) -> Optional[dict]:
    """
    构造生产单
    :param product_uid: 产品识别码
    :param stl_files: STL格式文件，每个关键词索引一个文件
    :param stp_files: STEP格式文件，每个关键词索引一个文件
    :param kwargs: 其它相关信息，每个关键词索引一个支持数据库直接录入的对象
    :return: 生产单信息
    """
    order_data = {'product_uid': product_uid, 'case_uid': case_uid,
                  'stl_files': {}, 'stp_files': {}}

    # 上传生产文件
    order_files = [order_data['stl_files'], order_data['stp_files']]
    files = [stl_files, stp_files]
    fs = [stl_fs, stp_fs]
    for i in range(len(files)):
        for kw in files[i]:
            f_bytes = open(files[i][kw], 'rb').read()
            md5 = hashlib.md5(f_bytes).hexdigest()

            if fs[i].exists({'md5': md5}):
                order_files[i][kw] = fs[i].find_one({'md5': md5})._id
            else:
                order_files[i][kw] = fs[i].put(f_bytes)

    for kw in kwargs:
        order_data[kw] = kwargs[kw]
    return order_data


def order_create(case: dict, ukw: list) -> Optional[dict]:
    """
    发布案例
    :param case: 本地案例信息
    :param ukw: 特征键列表，用于判断相同案例
    :return: 发布后的案例信息
    """
    # 查找相同案例
    ukw_value = {kw: case[kw] for kw in ukw}
    find = case_db.find_one(ukw_value)

    if find and 'case_uid' in find:
        if find['customer_confirmed']:
            vmi.askInfo('顾客已确认')
        r = vmi.askButtons(['下载存档', '上传存档'])
    else:
        r = vmi.askButtons(['创建存档'])


def costomer_update():
    f = vmi.askOpenFile('*.csv', '顾客信息表')
    if f is None:
        return

    customer_db = database.get_collection('customer')
    customer_db.delete_many({})

    with open(f, newline='') as f:
        for row in csv.reader(f):
            customer_db.insert_one(dict(zip(
                ['customer_uid', 'name', 'organization', 'email', 'mailing', 'sales', 'sales_contact'], row)))


if __name__ == '__main__':
    # 更新顾客信息表
    costomer_update()
