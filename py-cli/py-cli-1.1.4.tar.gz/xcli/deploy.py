# -*- coding: UTF-8 -*-

import getopt
import os
import sys
from os import path

from androguard.core.bytecodes.apk import APK

import xcli
from xcli import oxs, apks, __version__, fir
from xcli.fir import FirToken


def __print_usage():
    print('Usage: python -m <app_module>')


def __find_args_from_command():
    project_path = app_module = ''
    release_flag = True

    opts, args = getopt.getopt(sys.argv[1:],
                               'hm:dvp:',
                               ['help', 'project=' 'module=', 'debug', 'version'])
    if opts:
        for opt, arg in opts:
            if opt in ("-p", "--project"):
                if arg:
                    project_path = arg

            elif opt in ("-m", "--module"):
                if arg:
                    app_module = arg
                else:
                    raise RuntimeError('[ERROR]: Usage: pycli -m <your project path> | --project="your project path"')

            elif opt in ("-d", "--debug"):
                release_flag = False

            elif opt in ("-v", "--version"):
                print(__version__)
                sys.exit(0)

            elif opt in ("-h", "--help"):
                __print_usage()
                sys.exit(0)

    if not project_path:
        cwd_path = os.getcwd()
        if path.exists(path.join(cwd_path, app_module, 'build.gradle')):
            project_path = cwd_path

        else:
            raise RuntimeError('\n[ERROR]: 当前目录非Android工程目录，请指定编译目录！！！')
    if not app_module:
        app_module = 'app'

    return project_path, app_module, release_flag


def invoke():
    project_abspath, app_module, release_flag = __find_args_from_command()
    module_abspath = path.join(project_abspath, app_module)
    if path.exists(module_abspath):
        config = xcli.load_config()

        deploy_type, gradle_result = apks.gradle_build(project_abspath, app_module, release_flag)
        if gradle_result == 0:
            print('\n[INFO]: 工程编译完成：%s' % project_abspath)

            flavors_name = apks.get_flavors_name(module_abspath)
            build_apk_name = apks.get_built_apk_name(app_module, deploy_type)

            build_outputs_abspath = path.join(module_abspath, 'build/outputs', flavors_name)
            build_apk_abspath = path.join(build_outputs_abspath, deploy_type, build_apk_name)
            if path.exists(build_apk_abspath):
                apk_object = APK(build_apk_abspath)
                apk_deploy_name = apks.get_deploy_name(apk_object)
                app_code = apks.get_app_code(apk_object)
                app_version_name = apk_object.get_androidversion_name()

                oss_key = path.join(app_code, flavors_name, app_version_name, apk_deploy_name)
                verify_result = oxs.publish(oss_key, build_apk_abspath)
                if verify_result:
                    print('[INFO]: apk文件上传OSS成功！')

                    # outputs apk文件修改成正式发布的名称
                    apk_deploy_abspath = path.join(build_outputs_abspath, deploy_type, apk_deploy_name)
                    os.rename(build_apk_abspath, apk_deploy_abspath)

                    manifest = apks.Manifest(apk_object)
                    manifest.deploy_abspath = apk_deploy_abspath

                    # 上传到Fir.im上
                    fir_cert = fir.validate(FirToken(config.fir_token, apk_object.get_package()))
                    is_completed = fir.publish(fir_cert, manifest)
                    if is_completed:
                        print('[INFO]: apk文件上传FIR.IM成功！')

                else:
                    raise RuntimeError("\n[ERROR]: oss上文件和本地apk文件校验失败！")
            elif apks.check_unsigned_apk_built(build_outputs_abspath, app_module, deploy_type):
                raise RuntimeError("\n[ERROR]: apk文件未签名：%s！" % build_apk_abspath)

            else:
                raise RuntimeError("\n[ERROR]: 工程编译失败，未生成apk文件：%s！" % build_apk_abspath)
        else:
            raise RuntimeError("\n[ERROR]: 工程编译失败，详见编译信息！")
    else:
        raise RuntimeError('\n[ERROR]: 工程文件不存在：%s！' % module_abspath)


if __name__ == "__main__":
    invoke()
