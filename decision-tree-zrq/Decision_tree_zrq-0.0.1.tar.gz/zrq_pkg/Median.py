# 中位数计算
def median(data):
    # data=float(data)
    data.sort()
    mid = int(len(data) / 2)
    if len(data) % 2 == 0:
        median = (data[mid - 1] + data[mid]) / 2.0
    else:
        median = data[mid]

    return median


data = [3.53, 3.47, 3.51, 3.72, 3.43]
print("data的中位数为：",median(data))