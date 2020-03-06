# -*- coding: UTF-8 -*-

import os
import subprocess

from androguard.core.bytecodes.apk import APK

__GENERAL_FLAVORS_NAME = 'apk'

__ASSEMBLE_RELEASE = 'assembleRelease'
__ASSEMBLE_DEBUG = 'assembleDebug'
__DEPLOY_RELEASE = 'release'
__DEPLOY_DEBUG = 'debug'
_NAMESPACE_XRJS = 'xrjs'


class Manifest(object):
    app_name = ''
    version_name = '1.0'
    version_code: int = 1
    change_log = '版本更新'

    deploy_abspath = ''

    def __init__(self, apk_object: APK):
        self.app_name = apk_object.get_app_name()
        self.version_name = apk_object.get_androidversion_name()
        self.version_code = apk_object.get_androidversion_code()
        self.change_log = '版本更新 %s' % self.version_name


def get_app_code(apk: APK):
    """
    获取apk中登记的app code

    :param apk:
    :return:
    """
    _manifest_xml = apk.get_android_manifest_xml()
    manifest_xml = apk.get_android_manifest_xml()

    ns_xrjs = manifest_xml.nsmap[_NAMESPACE_XRJS]
    application_element = manifest_xml.xpath('/manifest/application')[0]
    app_code = application_element.attrib["{%s}appCode" % ns_xrjs]

    return app_code


def get_deploy_name(apk: APK):
    """
    获取默认发布的apk名称

    :param apk:
    :return:
    """
    return '%s_%s_build_%s.apk' % (get_app_code(apk), apk.get_androidversion_name(), apk.get_androidversion_code())


def get_built_apk_name(app_module, deploy_type):
    return "%s-%s.apk" % (app_module, deploy_type)


def has_product_flavors(file_path):
    has_flavors = False

    with open(file_path) as file:
        line_text = file.readline()
        while line_text:
            if 'productFlavors' in line_text:
                has_flavors = True
                break

            line_text = file.readline()

    return has_flavors


def get_flavors_name(project_module_path):
    flavors_name = __GENERAL_FLAVORS_NAME

    build_gradle_path = os.path.join(project_module_path, 'build.gradle')

    has_flavors = has_product_flavors(build_gradle_path)
    if has_flavors:
        pass

    return flavors_name


def check_unsigned_apk_built(build_outputs_path, app_module, deploy_type):
    unsigned_apk_name = "%s-%s-unsigned.apk" % (app_module, deploy_type)

    return os.path.exists(os.path.join(build_outputs_path, deploy_type, unsigned_apk_name))


def gradle_build(project_path, app_module, flag):
    assemble_type = __ASSEMBLE_RELEASE if flag else __ASSEMBLE_DEBUG
    deploy_type = __DEPLOY_RELEASE if flag else __DEPLOY_DEBUG

    build_command = "./gradlew -q -p %s clean %s" % (app_module, assemble_type)

    # 执行gradle脚本
    _gradle_result = subprocess.call(build_command, shell=True, cwd=project_path)

    return deploy_type, _gradle_result
