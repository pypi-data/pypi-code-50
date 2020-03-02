import re, sys, getopt

try:
    import pyperclip
except Exception as e:
    print('-p 需要安装pyautogui: "pip install pyautogui"')

t = "\'" # 默认添加单引号


def replace(name):
    name1 = name.group("name1").strip()
    name2 = name.group("name2").strip()
    if t not in name1 and '\'' not in name1 and  '"' not in name1 and  '\"""' not in name1 and  "'''" not in name1:
        names = f"{t}{name1}{t}: {t}{name2}{t},"

    else:
        return None

    return names + '\n'


def main():
    """
    -c  把替换内容打印到控制台
    -v  把替换内容复制到剪辑版
    -h  帮助文档
    -p  复制到剪切板再粘贴到pycahrm（需要安装第三方库 pyautogui）
    -t  要用什么替换，默认用单引号替换  双引号需要转义如使用三引号替换：-t\"\"\"
    -r  填 -r"$SelectedText$" -r参数 请放在最后面

    例子1：-m replacess -c -r"$SelectedText$"
    例子2：-m replacess -v -r"$SelectedText$"
    例子3：-m replacess -v -c -r"$SelectedText$"
    例子4：-m replacess -p -r"$SelectedText$"
    例子5：-m replacess -p -t\" -r"$SelectedText$"  用双引号替换，并将替换的内容粘贴到pycahrm替换的位置

    作者QQ：2920007919
    """
    c,v,h,p,r = False,False,False,False,False
    global t
    try:
        opts, args = getopt.getopt(sys.argv[1:], "-c-v-h-p-t:-r:",
                                   ['console', 'version', 'help', 'paste', 'type=', 'chramText='])
        for o, a in opts:
            if o in ('-c', '--console'):c = True
            if o in ('-v', '--version'):v = True
            if o in ('-h', '--help'):h = True
            if o in ('-p', '--paste'):p = True
            if o in ('-t', '--type'):t = a
            if o in ('-r', '--chramText'):r = a

    except Exception as e:
        if "-r" in e.args[0]:
            print("你没有选中文本！或指定-r 参数！")
        else:
            print(e.args)
            print(main.__doc__)
    else:
        if r != "":
            text = re.sub(r'(?P<name1>.*?)[:|：](?P<name2>.*?)\n', replace, f'{r}\n').strip('\n')
        else:
            return 0

        if c and text:print(f'\n\n{text}')
        if v and text:
            try:
                import pyautogui
            except Exception as e:
                print('-p 需要安装pyautogui: "pip install pyautogui"')
                return 0
            else:
                pyperclip.copy(text)

        if h:print(main.__doc__, end=' ')

        if p and text:
            try:
                import pyautogui
            except Exception as e:
                print('-p 需要安装pyautogui: "pip install pyautogui"')
                return 0
            else:
                pyperclip.copy(text)
                pyautogui.hotkey('ctrl', 'v')


if __name__ == "__main__":
    sys.exit(main())
