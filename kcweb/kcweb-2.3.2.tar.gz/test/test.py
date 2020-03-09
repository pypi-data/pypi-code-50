#coding=utf8
 
from pydub import AudioSegment
import wave
import json
import numpy as np
def mp3_wav():
    MP3_File = AudioSegment.from_mp3(file="4.mp3")
    MP3_File.export("4.wav",format="wav")
mp3_wav()
# from matplotlib import pyplot as plt 
# import librosa.display
# import random
# x=range(0,10)
# y=[random.randint(20,35) for i in range(10)]
# plt.plot(x,y)
# plt.grid()
# plt.show()
# exit()


import librosa,time
import matplotlib.pyplot as plt
import librosa.display
audio_path = './4.wav'
t=time.time()
x , sr = librosa.load(audio_path)
print(len(x))
i=0
ii=[]
yy=[]
while i < len(x):
    yy.append(x[i])
    ii.append(i)
    i+=1
print("时间",time.time()-t)
plt.plot(ii,yy)
plt.grid()
plt.show()