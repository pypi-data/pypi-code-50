import os
settime = 90
package_name_list = ["os", "shutil"]
keywords = "import"


def check_package(res, file_name):
    ff = open(file_name, "r", encoding="u8")
    ad = ff.readlines()
    for package_name in package_name_list:
        unsafename = package_name
        for line in ad:
            if keywords in line and " "+unsafename in line:
                res.update(code=555, msg="安全检查未通过",
                           err="代码中引入了" + unsafename + "库，违反了机器人第三定律，终止运行，请检查代码后重新运行")
                os.remove(file_name)
                return res
    return res


def check_mode(code):
    advance = ["###offline_running=True###"]
    for ss in advance:
        if ss in code:
            return True
    return False
