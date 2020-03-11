from ddcmaker.public.lsc_client import LSC_Client

lsc = LSC_Client()


class showlib(object):
    def hiphop(self):
        print("机器人给大家表演街舞！")
        lsc.RunActionGroup(16, 1)
        lsc.WaitForFinish(60000)

    def jiangnanstyle(self):
        print("机器人给大家表演江南style！")
        lsc.RunActionGroup(17, 1)
        lsc.WaitForFinish(600000)

    def smallapple(self):
        print("机器人给大家表演小苹果！")
        lsc.RunActionGroup(18, 1)
        lsc.WaitForFinish(60000)

    def lasong(self):
        print("机器人给大家表演LASONG！")
        lsc.RunActionGroup(19, 1)
        lsc.WaitForFinish(60000)

    def feelgood(self):
        print("机器人给大家表演倍儿爽！")
        lsc.RunActionGroup(20, 1)
        lsc.WaitForFinish(60000)

    def fantastic_baby(self):
        print("机器人给大家表演fantastic baby！")
        lsc.RunActionGroup(21, 1)
        lsc.WaitForFinish(60000)

    def super_champion(self):
        print("机器人给大家表演super champion！")
        lsc.RunActionGroup(22, 1)
        lsc.WaitForFinish(60000)

    def youth_cultivation(self):
        print("机器人给大家表演青春修炼手册！")
        lsc.RunActionGroup(23, 1)
        lsc.WaitForFinish(60000)

    def Love_starts(self):
        print("机器人给大家表演爱出发！")
        lsc.RunActionGroup(24, 1)
        lsc.WaitForFinish(60000)
