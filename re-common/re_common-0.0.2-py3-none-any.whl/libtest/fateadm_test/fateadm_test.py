def test_fateadm_file():
    """
    第二种简便用法
    命令行下　在当前目录使用该命令测试
    pytest fateadm_test.py::test_fateadm_file -s
    :return:
    """
    from re_common.baselibrary import UseFateadm

    f = UseFateadm()
    print("直接返回结果************************************")
    print(f.PredictFromFileExtend("1.jpg", f.pred_type))
    print("返回一个对象************************************")
    rsp = f.PredictFromFile("1.jpg", f.pred_type)
    print("resp:", rsp)
    print("ret_code:" + str(rsp.ret_code))
    print("cust_val:" + str(rsp.cust_val))
    print("err_msg:" + str(rsp.err_msg))
    print("rsp.pred_rsp.value:" + str(rsp.pred_rsp.value))
    print("************************************")
    # 　使用默认类型
    print("直接返回结果,使用默认类型************************************")
    print(f.PredictFromFileExtend("1.jpg"))
    print("返回一个对象************************************")
    rsp = f.PredictFromFile("1.jpg")
    print("resp:", rsp)
    print("ret_code:" + str(rsp.ret_code))
    print("cust_val:" + str(rsp.cust_val))
    print("err_msg:" + str(rsp.err_msg))
    print("rsp.pred_rsp.value:" + str(rsp.pred_rsp.value))
    print("************************************")


def test_fateadm_data():
    """
    第二种简便用法
    命令行下　在当前目录使用该命令测试
    pytest iniconfig_test.py::test_Iniconfig_config -s
    :return:
    """
    from re_common.baselibrary import UseFateadm
    from re_common.baselibrary import BaseFile
    file = "2.jpg"
    data = BaseFile.read_file_rb(file)
    f = UseFateadm()
    print("直接返回结果************************************")
    print(f.PredictExtend(data, f.pred_type))
    print("返回一个对象************************************")
    rsp = f.Predict(data, f.pred_type)
    print("resp:", rsp)
    print("ret_code:" + str(rsp.ret_code))
    print("cust_val:" + str(rsp.cust_val))
    print("err_msg:" + str(rsp.err_msg))
    print("rsp.pred_rsp.value:" + str(rsp.pred_rsp.value))
    print("************************************")
    # 使用默认类型
    print("直接返回结果************************************")
    print(f.PredictExtend(data))
    print("返回一个对象************************************")
    rsp = f.Predict(data)
    print("resp:", rsp)
    print("ret_code:" + str(rsp.ret_code))
    print("cust_val:" + str(rsp.cust_val))
    print("err_msg:" + str(rsp.err_msg))
    print("rsp.pred_rsp.value:" + str(rsp.pred_rsp.value))
    print("************************************")
