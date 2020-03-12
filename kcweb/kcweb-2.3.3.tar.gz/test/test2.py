import cv2
vc = cv2.VideoCapture('imageai/file/traffic-minis.mp4')  # 读取视频文件
c = 0
print("------------")
if vc.isOpened():  # 判断是否正常打开
    print("yes")
    rval, frame = vc.read()
else:
    rval = False
    print("false")

timeF = 1000000  # 视频帧计数间隔频率

while rval:  # 循环读取视频帧
    rval,frame = vc.read()
    # print(c,timeF,c%timeF)
    if (c % timeF == 0):# 每隔timeF帧进行存储操作
        print("write...",timeF)
        print(len(frame[400]))
        cv2.imwrite('aa/1' + str(c) +"--2"+ '.jpg', frame)  # 存储为图像
        print("success!")
    c = c + 100000
cv2.waitKey(1)
vc.release()
print("==================================")