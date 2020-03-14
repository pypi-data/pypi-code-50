import pygrading.general_test as gg

testcases = gg.create_testcase(100)

for i in range(1, 5):
    input_src = i
    output_src = pow(2, i)

    # 使用append()方法向testcases追加评测用例
    testcases.append("TestCase{}".format(i), 25, input_src, output_src)

print(str(testcases))