# 均值计算
def mean(data):

    average = float(sum(data))/len(data)
    return average


data = [3.53, 3.47, 3.51, 3.72, 3.43]

print("data的均值为：",mean(data))