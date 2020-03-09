
import numpy as np
import cv2,time
video = cv2.VideoCapture("imageai/file/traffic-minis.mp4")
fps = video.get(cv2.CAP_PROP_FPS) #视频帧率
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT) #视频总帧数
width=int(video.get(cv2.CAP_PROP_FRAME_WIDTH)) #视频宽度
height=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)) #视频高度

# videoWriter = cv2.VideoWriter('imageai/file/traffic-minis1.mp4', cv2.VideoWriter_fourcc(*'MP4V'), fps, (width,height)) 

success, frame = video.read() #逐帧读取视频 第一个返回值的是读取视频成功与否，第二个返回值是视频当前帧，读完后视频会迭代到下一帧，下载再调read方法的时候，就可以把下一帧读出。因此，用while循环，即可把视频逐帧读出：
index = 1
while success :
	cv2.putText(frame, 'fps: ' + str(fps), (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
	cv2.putText(frame, 'count: ' + str(frameCount), (0, 300), cv2.FONT_HERSHEY_SIMPLEX,2, (255,0,255), 5)
	cv2.putText(frame, 'frame: ' + str(index), (0, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
	cv2.putText(frame, 'time: ' + str(round(index / 24.0, 2)) + "s", (0,500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
	cv2.imshow("frame", cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY))
    # cv2.waitKey(1)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
	# cv2.waitKey(1000 / int(fps))
	# videoWriter.write(frame)
	success, frame = video.read()
    # print(success)
	index += 1
video.release()