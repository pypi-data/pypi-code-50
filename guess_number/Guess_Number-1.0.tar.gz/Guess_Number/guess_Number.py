'''
让用户输入一个数，判断是否正确
# 随机数需要引入random包
'''

def guess_number( ):
    import random
    guessNum = random.randint(0, 100)

    # 提示用户输入整数
    while True:
        iptNum = int(input("请输入一个整数："))
        if guessNum == iptNum:
            print("恭喜你猜对了！")
            break
        elif guessNum > iptNum:
            print("您猜小了，请重新输入！")
        else:
            print("您猜大了，请重新输入！")

guess_number()