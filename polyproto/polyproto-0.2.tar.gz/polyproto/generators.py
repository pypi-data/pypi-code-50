# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:48:41 2020

@author: Kevin
"""


from polyproto.drawFunctions import drawRandomCircle,drawRandomLine,drawRandomEllipse,drawRandomRectangle,drawRandomPolygon
import numpy as np
import tensorflow as tf

if int(tf.__version__.split(".")[0])  >= 2:
    from keras.utils import to_categorical, Sequence
else:
    from keras.utils import to_categorical, Sequence
class GeometricGenerator(Sequence):      
    
    def __init__(self,
                 width=200,
                 height=200,
                 channels=3,
                 forms=3,
                 batch_mul=2,
                 epoch_length=100,
                 max_background_noise=128,
                 list_of_form_creators=[drawRandomCircle,
                                        drawRandomLine,
                                        drawRandomRectangle,
                                        drawRandomEllipse]):
        """
            @brief This is a simple generator for creating common geometric shapes 
            @param width image width
            @param height image height
            @param channels Image channels, note that only 3-Channels are supported at the moment
            @param forms Amount of different forms to be drawn, this is also the amount of classes produced
            @param batch_mul Multiplicator to create a batch. If you use 3 forms and a batch_mul of 2
            the resulting batch_size will have the size of 6 (batch_mul*forms)
            @param epoch_length Length of one epoch
            @param max_background_noise A random background will be used, this describes the maxmium
            @param list_of_form_creators here you can give in a list of functions that will be called
            to create a form
        """        
        
        self.image_size = (width,height)
        self.width = width
        self.height = height
        self.channels = channels
        self.epoch_length = epoch_length
        
        if forms > len(list_of_form_creators):
            raise ValueError("amount of forms cannot be larger than given functions")
        self.forms = forms
        self.list_of_form_creators = list_of_form_creators
        self.max_background_noise = max_background_noise
        self.batch_mul = batch_mul
    def __len__(self):
        # here we can just say whatever we find fitting for one epoch
        return self.epoch_length
        
        
    def __getitem__(self,idx):
        
        X = np.random.randint(0,self.max_background_noise,size=(self.batch_mul*self.forms,
                                          self.width,
                                          self.height,
                                          self.channels))
        Y = np.zeros(shape=(self.batch_mul*self.forms))
        
        cnt = 0
        for i in range(self.batch_mul):
            for j in range(self.forms):
                X[cnt] = self.list_of_form_creators[j](X[cnt])
                Y[cnt] = j
                cnt += 1
             
        idx = np.arange(0,len(X))
        np.random.shuffle(idx)
        
        X = X[idx]
        Y = Y[idx]
        
        return X/255,to_categorical(Y)


class GeometricNGenerator(Sequence):      
    
    def __init__(self,
                 width=200,
                 height=200,
                 channels=3,
                 forms=8,
                 batch_mul=2,
                 epoch_length=100,
                 maximum_vertices=20,
                 pts=None,
                 seed=3121991,
                 max_background_noise=128):
        """
            @brief This is a simple generator for creating polygons        
            @param width image width
            @param height image height
            @param channels Image channels, note that only 3-Channels are supported at the moment
            @param forms Amount of different forms to be drawn, this is also the amount of classes produced
            @param batch_mul Multiplicator to create a batch. If you use 3 forms and a batch_mul of 2
            the resulting batch_size will have the size of 6 (batch_mul*forms)
            @param epoch_length Length of one epoch
            @param maximum_vertices Maximum vertices for for a polygon, will be used if pts are None
            @param pts to create polygons from. Set to None if not used
            @param seed seed for numpy to make reproducible experiments
            @param max_background_noise A random background will be used, this describes the maxmium
        """        
        np.random.seed(seed)
        # will use random then
        if pts is None:
            self.random_pts = []
            for i in range(forms):
                
                # random length of vertices 
                amount_of_vertices = np.random.randint(2,maximum_vertices)
                x_cords = np.random.randint(0,width,size=amount_of_vertices)
                y_cords = np.random.randint(0,height,size=amount_of_vertices)

                pts = np.array([x_cords,y_cords]).T
                pts = pts.reshape((-1,1,2))

                self.random_pts.append(pts)
                
        else:
            self.random_pts = pts
            
        self.forms = forms
        self.image_size = (width,height)
        self.width = width
        self.height = height
        self.channels = channels
        self.epoch_length = epoch_length
        self.max_background_noise = max_background_noise
        self.batch_mul = batch_mul
    
    def __len__(self):
        # here we can just say whatever we find fitting for one epoch
        return self.epoch_length
        
        
    def __getitem__(self,idx):
        
        X = np.random.randint(0,self.max_background_noise ,size=(self.batch_mul*self.forms,
                                          self.width,
                                          self.height,
                                          self.channels))
        Y = np.zeros(shape=(self.batch_mul*self.forms))
        
        cnt = 0
        for i in range(self.batch_mul):
            for j in range(self.forms):
                
                X[cnt] = drawRandomPolygon(X[cnt],self.random_pts[j])
                Y[cnt] = j
                cnt += 1
             
        idx = np.arange(0,len(X))
        np.random.shuffle(idx)
        
        X = X[idx]
        Y = Y[idx]
        
        return X/255,to_categorical(Y)