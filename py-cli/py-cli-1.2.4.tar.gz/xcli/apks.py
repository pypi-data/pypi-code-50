# -*- coding: UTF-8 -*-

import os
import shutil
import subprocess
from os import path

from androguard.core.bytecodes.apk import APK

import xcli
from lang import files
from lang import ids
from lang.io import Properties

__PYCLI_PATH = path.abspath(path.join(path.dirname(os.getcwd()), '.'))
__LIBS_PATH = path.join(__PYCLI_PATH, 'libs')
__CHECK_SIGNATURE_V2_PATH = path.join(__LIBS_PATH, "CheckAndroidV2Signature.jar")

__WALLE_CLI_PATH = path.join(xcli.get_libs_path(), "walle-cli-all.jar")

__GENERAL_FLAVORS_NAME = 'apk'

__ASSEMBLE_RELEASE = 'assembleRelease'
__DEPLOY_RELEASE = 'release'
__NAMESPACE_XRJS = 'xrjs'


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


class JksConfig(object):
    """
    读取key_store配置文件

    key.store.path=/datum/workspace/x/profile/xrj_app.jks
    key.store.password=xxxxx
    key.alias=xiot
    key.password=xxxxx
    """
    props = {}

    store_path = ''
    store_password = ''
    key_alias = ''
    key_password = ''

    def __init__(self, abspath):
        self.props = Properties(abspath).dict()

        self.store_path = self.props.get('key.store.path')
        self.store_password = self.props.get('key.store.password')
        self.key_alias = self.props.get('key.alias')
        self.key_password = self.props.get('key.password')


def get_app_code(apk: APK):
    """
    获取apk中登记的app code

    :param apk:
    :return:
    """
    _manifest_xml = apk.get_android_manifest_xml()
    manifest_xml = apk.get_android_manifest_xml()

    ns_xrjs = manifest_xml.nsmap[__NAMESPACE_XRJS]
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


def get_build_apk_name(app_module, deploy_type=__DEPLOY_RELEASE):
    return "%s-%s.apk" % (app_module, deploy_type)


def get_build_output_path(module_abspath, flavors_name, deploy_type=__DEPLOY_RELEASE):
    return path.join(module_abspath, 'build/outputs', flavors_name, deploy_type)


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


def check_unsigned_apk_built(build_outputs_path, app_module, deploy_type=__DEPLOY_RELEASE):
    unsigned_apk_name = "%s-%s-unsigned.apk" % (app_module, deploy_type)

    return os.path.exists(os.path.join(build_outputs_path, deploy_type, unsigned_apk_name))


def gradle_build(project_path, app_module):
    """
    执行gradle脚本

    :param project_path:
    :param app_module:
    :return:
    """
    build_command = "./gradlew -q -p %s clean assembleRelease" % app_module
    print('[INFO]: %s: %s' % (build_command, project_path))
    subprocess.run(build_command, shell=True, cwd=project_path)


def get_jks_config(abspath):
    gradle_configs = Properties(abspath).dict()
    jks_abspath = gradle_configs.get('KEYSTORE_PROPERTIES_PATH')
    if jks_abspath:
        jks_config = JksConfig(jks_abspath)
    else:
        raise RuntimeError("\n[ERROR]: Apk签名配置文件加载失败：%s！" % jks_abspath)

    return jks_config


def zipalign(apk_abspath, out_path):
    """
    zipalign对齐

    :param apk_abspath:
    :param out_path:
    :return:
    """
    aligned_apk_path = path.join(out_path, "%s_aligned.apk" % ids.generate())
    zipalign_command = "zipalign -v 4 %s %s" % (apk_abspath, aligned_apk_path)
    print(zipalign_command)
    subprocess.run(zipalign_command, shell=True)

    return aligned_apk_path


def sign(apk_abspath, jks: JksConfig, out_path):
    """
    签名和校验V2
    :param apk_abspath:
    :param jks:
    :param out_path:
    :return:
    """
    signed_apk_path = path.join(out_path, "%s_signed.apk" % ids.generate())
    apk_signer_command = "apksigner sign --ks %s --ks-pass pass:%s --ks-key-alias %s --key-pass pass:%s --out %s %s" \
                         % (jks.store_path, jks.store_password, jks.key_alias, jks.key_password, signed_apk_path, apk_abspath)
    print('[INFO]: %s' % apk_signer_command)
    subprocess.run(apk_signer_command, shell=True)

    # 检查V2签名是否正确
    check_signature_v2_command = "java -jar %s %s" % (__CHECK_SIGNATURE_V2_PATH, signed_apk_path)
    print('[INFO]: %s' % check_signature_v2_command)
    subprocess.run(check_signature_v2_command, shell=True)

    return signed_apk_path


def channel(apk_abspath, channel_abspath, output_path):
    """
    写入渠道

    :param apk_abspath:
    :param channel_abspath:
    :param output_path:
    :return:
    """
    walle_cli_command = "java -jar %s batch -f %s %s %s" % (__WALLE_CLI_PATH, channel_abspath, apk_abspath, output_path)
    print(walle_cli_command)
    subprocess.run(walle_cli_command, shell=True)


def assemble(apk_abspath, jks: JksConfig, channel_abspath, output_path):
    walle_temp_path = files.get_cache_path()

    # 对齐
    aligned_apk_path = zipalign(apk_abspath, walle_temp_path)

    # 签名
    signed_apk_path = sign(aligned_apk_path, jks, walle_temp_path)

    # 写入渠道
    channel(signed_apk_path, channel_abspath, output_path)

    shutil.rmtree(walle_temp_path)
