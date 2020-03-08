#!/usr/bin/env python
# coding: utf-8
#game site:
#http://wap.jue-huo.com/app/html/game/1to50/1to50.html

import sys,dlib,numpy
#pip install scikit-image
from skimage import io
import cv2
import os
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from os.path import dirname

import requests
import bz2

def _download_url_response(path,url):
    r = requests.get(url, stream = True)
    with open(path, 'wb') as f:
        i=0
        for ch in r:
            if i%1024==0:print('.',end='')
            f.write(ch);i+=1
    
def _bz2Decode(filepath):
    zipfile = bz2.BZ2File(filepath) # open the file
    data = zipfile.read() # get the decompressed data
    newfilepath = filepath[:-4] # assuming the filepath ends with .bz2
    open(newfilepath, 'wb').write(data) # write a uncompressed file
    
def dowloadFileInNeed(filename):
    if not os.path.isfile(filename):
        print("載入"+filename+"...可能需要一點時間") 
        url="http://dlib.net/files/"+filename+".bz2"
        _download_url_response(filename+".bz2",url)
        _bz2Decode(filename+".bz2")
        os.remove(filename+".bz2")
        print("ok")
dowloadFileInNeed("shape_predictor_68_face_landmarks.dat")  
dowloadFileInNeed("dlib_face_recognition_resnet_model_v1.dat")
    
#Package_Dir = dirname(__file__)
#載入字型
_FONT = ImageFont.truetype("kaiu.ttf",20,index=0)
# 載入人臉檢測器
_detector = dlib.get_frontal_face_detector()
# 載入人臉特徵點檢測器
_sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# 載入人臉辨識檢測器
_facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
#dlib_face_recognition_resnet_model_v1.dat  has to download by user
DB={}

def _createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' +  directory)
        
#一張圖片中，取rect區域當作人臉得到特徵向量   
def getFeatureVector(img,rect=None):
    if not rect:
        try:
            rect=_detector(img, 1)[0] #如果沒有傳入rect取第一個檢測到的臉區域
        except:return None
    shape = _sp(img,rect) #找出特徵點位置
    #由圖片中特徵點位置(shape)擷取出特徵向量(128維特徵向量)
    face_descriptor = _facerec.compute_face_descriptor(img, shape)
    # 轉換numpy array格式
    return numpy.array(face_descriptor)


def loadImg(fname):
    '''
    load image from file : return a opencv image object
    '''
    return io.imread(fname)

def loadDB(db=DB,folder='train'):
    '''
    db:dictionary of key feature vectors
    DB is a default dictionary object for db
    default folder should be "train"
    '''
    for f in os.listdir(folder):
        path = folder+"\\"+f
        if os.path.isfile(path):
            img = io.imread(path)
            DB[os.path.splitext(f)[0]]=getFeatureVector(img)
            print(f+" feature loaded")

def loadFeatureFromPic(imagePath):
    img = io.imread(imagePath)
    return getFeatureVector(img)

def loadPicRawFeature(fname):
    try:
        img = io.imread(fname)
        #img.tofile('test.txt',',')
        return img.flatten()/255.0
    except Exception:print(Exception.args)
    return None

def predictFromDB(VTest,db=DB):
    '''Get the correspondent class which is most similar with VTest'''
    minD = sys.float_info.max
    minK=''
    for k in DB:
        dist=numpy.linalg.norm(VTest-DB[k])
        if dist<minD:
            minK=k
            minD=dist
    return minK,minD


def dist(V1,V2):
    '''return distance between V1,V2'''
    return numpy.linalg.norm(V1-V2)

def addText2Img_cv2(img_cv2,text,font=_FONT,position=(20,20),fill=(255,0,0)):
    img_PIL = Image.fromarray(cv2.cvtColor(img_cv2,cv2.COLOR_BGR2RGB))#cv2.COLOR_BGR2RGB cv2.COLOR_RGB2BGR
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, text, font=font, fill=fill)
    img_cv2 = cv2.cvtColor(numpy.asarray(img_PIL),cv2.COLOR_RGB2BGR)# 转换回OpenCV格式
    img_PIL.close()
    return img_cv2

def captureImageFromCam():
    ret = None
    cap = None
    for i in range(3):#assume there are less than 3 webcam attached to the platform
        cap = cv2.VideoCapture(i)
        if cap.isOpened(): break   
    if not cap:return None
    # 載入人臉檢測器
    while(True):
        if cap.isOpened():
            ret, frame = cap.read()
            ret = frame
            break
    cap.release()
    return ret

#由webcam擷取訓練影像 and save          
def capturePicFromCamAndSave(tag,folder="train"):
    ret = False
    cap = None
    for i in range(3):#assume there are less than 3 webcam attached to the platform
        cap = cv2.VideoCapture(i)
        if cap.isOpened(): break
        
    if not cap:return False
    cv2.startWindowThread()
    # 載入人臉檢測器
    text="press p to take picture"
    _createFolder(folder+"\\"+tag)

    while(True):
        if cap.isOpened():
            ret, frame = cap.read()
            # 顯示圖片
            if ret: 
                try:
                    rect=_detector(frame, 1)[0] #取第一個檢測到的臉區域# IndexError
                    if cv2.waitKey(1) & 0xFF == ord('p'):
                        im=cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                        io.imsave(folder+"\\"+tag+".jpg",im)
                        text=" pictures saved..."
                        ret = True
                        break
                    cv2.rectangle(frame,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(255,0,0),3)
                    cv2.putText(frame, text,(rect.left()-80, rect.top()-20), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2, cv2.LINE_AA)    
                    frame=addText2Img_cv2(frame,'tag='+tag,_FONT,(rect.left(), rect.top()-_FONT.size*2-5))   
                #except:pass 
                except IndexError:pass
                cv2.imshow('press esc to exit', frame)
            #若按下 esc 鍵則離開迴圈
            if cv2.waitKey(1) == 27: break
    cap.release()
    cv2.destroyAllWindows()
    return ret

def predictVedio(vedioPath,skipFranmes=10,db=DB):
    cv2.startWindowThread()
    cap = cv2.VideoCapture(vedioPath)
    success,image = cap.read()
    count = 0
    while success:
        success,frame = cap.read()
        count+=1
        if count%skipFranmes!=0 :continue
        try:
            rects=_detector(frame, 1)
            for rect in rects:
                V=getFeatureVector(frame,rect)
                Tag,dist=predictFromDB(V,DB) # predict the target Tag
                cv2.rectangle(frame,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(255,0,0),3)
                text=Tag+":"+str(dist)
                frame=addText2Img_cv2(frame,Tag+":"+str(round(dist,3)),_FONT,(rect.left(), rect.top()-_FONT.size-1))        
        except IndexError:pass    
        cv2.imshow('press esc to exit...', frame)
        if cv2.waitKey(10) == 27:                     # exit if Escape is hit
            break
    cap.release()
    cv2.destroyAllWindows()
    

def predictCam(camSerial=None,outputFileName=""):
    ''' perform predict on webcam the show the result to window'''
    #即時辨識
    cap = None
    if not camSerial:
        for i in range(5):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():break
    else: cap = cv2.VideoCapture(camSerial)
    cv2.startWindowThread()
    _detector = dlib.get_frontal_face_detector()
    while(True):    
        if not cap.isOpened():break
        ret, frame = cap.read()
        if ret: 
            try:
                rects=_detector(frame, 1)
                for rect in rects:
                    V=getFeatureVector(frame,rect)
                    Tag,dist=predictFromDB(V) # predict the target Tag
                    cv2.rectangle(frame,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(255,0,0),3)                    #cv2.putText(frame, Tag+":"+str(dist),, cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2, cv2.LINE_AA)
                    text=Tag+":"+str(dist)
                    frame=addText2Img_cv2(frame,Tag+":"+str(round(dist,3)),_FONT,(rect.left(), rect.top()-_FONT.size-1))        
                    if outputFileName!="":
                        with open(outputFileName,'w') as f:
                            f.write(Tag)
            except IndexError:pass    
            cv2.imshow('press esc to exit...', frame)
        if cv2.waitKey(10) == 27: break
    cap.release()
    cv2.destroyAllWindows()



