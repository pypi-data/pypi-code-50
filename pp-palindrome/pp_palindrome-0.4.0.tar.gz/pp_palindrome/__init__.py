def number(data):
    if len(str(data)) < 2:
        print('请输入两个数字')
    else:
        positive_negative_list = []
        positive_num = str(data)
        lenth = len(str(positive_num))
        for num in range(0, lenth):
            positive_negative_list.append(positive_num[num])
        positive_negative_list.reverse()
        negative_num = ''
        for index in positive_negative_list:
            negative_num = negative_num + str(index)
        positive_negative_num = str(int(positive_num) + int(negative_num))
        import math
        count_num_positive = len(positive_negative_num) / 2
        count = math.floor(count_num_positive)
        count2 = len(str(positive_negative_num)) - 1
        data2 = positive_negative_num
        a = 0
        for count_num_negative in range(0,count):
            if int(positive_negative_num[count2]) == int(positive_negative_num[count_num_negative]):
                a += 1
            count2 -= 1
        if a == count:
            return int(positive_negative_num)
        else:
            while True:
                positive_negative_list = []
                positive_num = str(data2)
                lenth = len(str(positive_num))
                for num in range(0, lenth):
                    positive_negative_list.append(positive_num[num])
                positive_negative_list.reverse()
                negative_num = ''
                for index in positive_negative_list:
                    negative_num = negative_num + str(index)
                positive_negative_num = str(int(positive_num) + int(negative_num))
                import math
                count_num_positive = len(positive_negative_num) / 2
                count = math.floor(count_num_positive)
                count2 = len(str(positive_negative_num)) - 1
                data2 = positive_negative_num
                a = 0
                for count_num_negative in range(0, count):
                    if int(positive_negative_num[count2]) == int(positive_negative_num[count_num_negative]):
                        a += 1
                    count2 -= 1
                if a == count:
                    break

            return int(positive_negative_num)



