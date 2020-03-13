import re


def get_universal_page_info(html, current_page_pattern, count_page_pattern, url_template):
    """
    :param html: original html text
    :param current_page_pattern: somgthing like "var currentPage=(\d+?);"
    :param count_page_pattern: somgthing like "var currentPage=(\d+?);"
    :param url_template:  something like "/index_{}.shtml"
    :return:dict
    """
    try:
        current_page = int(re.findall(current_page_pattern, html).pop())
        count_page = int(re.findall(count_page_pattern, html).pop())
    except Exception as e:
        return {
            "current_page": None,
            "count_page": None,
            "next_page": None
        }

    if current_page < count_page - 1:
        next_page = current_page + 1
        res = {
            "current_page": current_page,
            "count_page": count_page,
            "next_page": url_template.format(next_page)
        }
        return res
    else:
        return {
            "current_page": current_page,
            "count_page": count_page,
            "next_page": None
        }


if __name__ == '__main__':
    import requests

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    })
    # csrc
    resp = session.get("http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwdd/")
    print(get_universal_page_info(resp.text,
                                  r"var currentPage = (\d+?);",
                                  r"var countPage = (\d+?)/",
                                  "/index_{}.html"))
    # ndrc
    resp = session.get("http://www.ndrc.gov.cn/zcfb/gfxwj/")
    print(get_universal_page_info(resp.text,
                                  r"createPageHTML\(\d+, (\d+), .*?\);",
                                  r"createPageHTML\((\d+), \d+, .*?\);",
                                  "/index_{}.html"))
    # mof
    resp = session.get("http://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/")
    print(get_universal_page_info(resp.text,
                                  r"var currentPage = (\d+?);",
                                  r"var countPage = (\d+?)/",
                                  "/index_{}.html"))

    # sac
    resp = session.get("https://www.sac.net.cn/hyfw/hydt/", verify=False)
    print(get_universal_page_info(resp.text,
                                  r"var currentPage = (\d+?);",
                                  r"var countPage = (\d+?);",
                                  "/index_{}.html"))

    # mee
    resp = session.get("http://www.mee.gov.cn/hdjl/yjzj/zjyj/")
    print(get_universal_page_info(resp.text,
                                  r"var currentPage=(\d+?);",
                                  r"var countPage=(\d+?)\n",
                                  "/index_{}.shtml"))
