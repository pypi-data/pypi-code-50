# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:55:17 2020

@author: Kevin
"""

import numpy as np
import cv2
import math as m

def getRandomRGB(minimum=1,maximum=255):
    """
        @brief Function for creating a rgb tuple to use
        @param minimum Minimum value in the random distribution
        @poaram maximum Maximum value in the random distirbution
        @return Will return a r,g,b tuple
    """
    r = np.random.randint(minimum,maximum)
    g = np.random.randint(minimum,maximum)
    b = np.random.randint(minimum,maximum) 
    
    return r,g,b

def getXYC(img,x_treshold=0,y_treshold=0):
    """
        @brief function for getting a random x and y location, as well as a 
        a center range
        @param img Image
        @param x_treshold will result in a lower x coordinate
        @param y_treshold will result in a lower y coordinate
        @return will return a x,y,c tuple
    """
    x = np.random.randint(0,img.shape[0]-x_treshold)
    y = np.random.randint(0,img.shape[1]-y_treshold)
    c = m.sqrt(img.shape[0]*img.shape[0] + img.shape[1]*img.shape[1]) - \
        m.sqrt(x*x + y*y)
        
    return x,y,c
            
def getThicknessAndLineType():
    thickness = np.random.randint(1,6)
    linetype = np.random.randint(0,3)
    return thickness,linetype
       
def geX1Y2(c):
    x1 = np.random.randint(0,c)
    y1 = np.random.randint(0,c)    
    return x1,y1

def drawRandomCircle(img):
    fail = True
    while fail:
        try:       
            
            x,y,c = getXYC(img)     
            radi = np.random.randint(1,c)
            r,g,b = getRandomRGB()           
            thickness,linetype = getThicknessAndLineType()
            img = cv2.circle(img.copy(),(y,x),int(radi),thickness=thickness,lineType=linetype,color=(r,g,b)) 
            fail = False
        except Exception as e:
            continue
    return np.array(img,dtype=np.uint8)

def drawRandomLine(img):
    fail = True
    while fail:
        try:
            x,y,c = getXYC(img)         
            x1,y1 = geX1Y2(c)
            r,g,b = getRandomRGB()
            thickness,linetype = getThicknessAndLineType()

            img = cv2.line(img.copy(),(y,x),(y1,x1),thickness=thickness,lineType=linetype,color=(r,g,b))    
            fail = False
        except Exception as e:
                continue
    
    return np.array(img,dtype=np.uint8)
    
def drawRandomRectangle(img):
    fail = True
    while fail:
        try:
            x,y,c = getXYC(img)            
            x1,y1 = geX1Y2(c)
            r,g,b = getRandomRGB()
            thickness,linetype = getThicknessAndLineType()

            img = cv2.rectangle(img.copy(),(y,x),(y1,x1),thickness=thickness,lineType=linetype,color=(r,g,b))    
            fail = False
        except Exception as e:
                continue
    
    return np.array(img,dtype=np.uint8)

def drawRandomEllipse(img):
    fail = True
    while fail:
        try:
            x,y,c = getXYC(img)   
            
            x1,y1 = geX1Y2(c)
            r,g,b = getRandomRGB()
            thickness,linetype = getThicknessAndLineType()
            
            range_ = np.random.randint(10,360)
            start = np.random.randint(0,360)
            end = np.random.randint(0,360)
            img= cv2.ellipse(img.copy(),(y,x),(y1,x1),start,end,range_,thickness=thickness,lineType=linetype,color=(r,g,b))
            fail = False
        except Exception as e:
                continue
    
    return np.array(img,dtype=np.uint8)

def drawRandomPolygon(img,pts):
    fail = True
    while fail:
        try:
             pts_c = pts.copy()
             x,y,c = getXYC(img,x_treshold=pts[:,:,0].max()-1,y_treshold=pts[:,:,1].max()-1)
             r,g,b = getRandomRGB()
             
             pts_c[:,:,0] = pts_c[:,:,0] + x
             pts_c[:,:,1] = pts_c[:,:,1] + y
             img = cv2.polylines(img.copy(),[pts_c],True,(r,g,b))
             fail = False
        except Exception as e:
                print(e)
                continue
    
    return np.array(img,dtype=np.uint8)       
        
        
        