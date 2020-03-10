# -*- coding: UTF-8 -*-

import os
from os import path

from androguard.core.bytecodes.apk import APK

import xcli
from xcli import ArgOpts
from xcli import OPT_DEPLOY
from xcli import oxs, apks, fir
from xcli.fir import FirToken


def get_apk_channel_abspath(module_abspath):
    return path.join(module_abspath, 'channel.ini')


def check_channel_config(channel_abspath):
    return path.exists(channel_abspath) and path.getsize(channel_abspath)


def check_project(args: ArgOpts):
    return path.exists(path.join(args.project_path, args.app_module, 'build.gradle'))


def deploy(args: ArgOpts):
    module_abspath = path.join(args.project_path, args.app_module)
    if path.exists(module_abspath):
        config = xcli.load_config()

        apks.gradle_build(args.project_path, args.app_module)
        print('\n[INFO]: 工程编译完成：%s' % args.project_path)

        flavors_name = apks.get_flavors_name(module_abspath)
        build_apk_name = apks.get_build_apk_name(args.app_module)

        build_outputs_abspath = apks.get_build_output_path(module_abspath, flavors_name)
        build_apk_abspath = path.join(build_outputs_abspath, build_apk_name)
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
                apk_deploy_abspath = path.join(build_outputs_abspath, apk_deploy_name)
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
        elif apks.check_unsigned_apk_built(build_outputs_abspath, args.app_module):
            raise RuntimeError("\n[ERROR]: apk文件未签名：%s！" % build_apk_abspath)

        else:
            raise RuntimeError("\n[ERROR]: 工程编译失败，未生成apk文件：%s！" % build_apk_abspath)
    else:
        raise RuntimeError('\n[ERROR]: 工程文件不存在：%s！' % module_abspath)


def main():
    args = ArgOpts()
    print(args)

    if args.operate == OPT_DEPLOY:
        if check_project(args):
            deploy(args)

        else:
            raise RuntimeError('\n[ERROR]: 当前目录非Android工程目录，请指定编译目录！！！')


if __name__ == "__main__":
    main()
