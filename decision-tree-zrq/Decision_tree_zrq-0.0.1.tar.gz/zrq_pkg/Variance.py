from  src.Mean import mean
import math
# 方差计算
def variance(data):
    total = 0
    for value in data:
        total += (value - mean(data)) ** 2

    stddev = math.sqrt(total / len(data))
    return stddev

data = [3.53, 3.47, 3.51, 3.72, 3.43]
print("data的方差为：",variance(data))