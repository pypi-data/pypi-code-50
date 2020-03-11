#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:29:52 2020

@author: jlbraid
"""
import os
import cv2
from pvimage import process
import numpy as np

# Finds lens distortion correction parameters for a given image
def GetLensCorrectParams(imagepath,imgtype=''):
    """Automatically detects lens correction parameters for an image
        using linear fitting of the module edges.

    Args:
        imagepath (str): path to a raw image
        imgtype (str):  'UVF' UV Fluorescence Image
                        'gradient' for unequal intensity across the image
                        'lowcon' low contrast between cell and background
                            or PL images without background subtraction
    Returns:
        n,f (float): lens correction parameters
    """    
    img = cv2.imread(imagepath)
    mask = process.Mask(img,imgtype)
    return process.autoLensCorrect(mask)

def MMpipeline(imagepath,savepath,numCols,numRows, stitch=False, imgtype=''):
    """Performs minimodule image processing steps, including cell extraction,
        planar indexing, and re-combination of cell images into a module
        image, if desired.

    Args:
        imagepath (str): path to a raw image
        savepath (str): folder path for saving output
        numCols (int): number of cells across in module image
        numRows (int): number of cells down in module image
        stitch (bool): True if output image with cell-level images stitched
            together is desired. Default is False
        imgtype (str):  'UVF' UV Fluorescence Image
                        'gradient' for unequal intensity across the image
                        'lowcon' low contrast between cell and background
                            or PL images without background subtraction
    Returns:
        
    """    
    img = cv2.imread(imagepath)
    file_name,ext = os.path.splitext(os.path.split(imagepath)[1])
    rotated = process.RotateImage(img,imgtype)
    cellarrays = process.CellExtract(rotated,numCols,numRows,imgtype)
    pi = []
    if len(cellarrays)>1:
        for i in range(len(cellarrays)):
            planarindexed = process.PlanarIndex(cellarrays[i],imgtype)
            image_name = savepath+file_name+'-c'+ '{:02}'.format(i+1) + ext
            cv2.imwrite(image_name,planarindexed)
            pi.append(planarindexed)
        if stitch == True:
            dims = []
            for array in pi:
                y,x = array.shape[0:2]
                dims.append([y,x])
            dims = np.asarray(dims)
            newy = int(np.mean(dims[:,0]))
            newx = int(np.mean(dims[:,1]))
            resized = []
            for array in pi:
                resized.append(cv2.resize(array,(newy,newx)))
            top = np.concatenate((resized[0],resized[1]),axis=1)
            bot = np.concatenate((resized[2],resized[3]),axis=1)
        
            tot = np.concatenate((top,bot),axis=0)
            save_name = savepath+file_name + ext
            cv2.imwrite(save_name,tot)
    elif len(cellarrays)==1:
        out = process.PlanarIndex(cellarrays[0],imgtype)
        image_name = savepath+file_name + ext
        cv2.imwrite(image_name,out)
    return True

def FMpipeline(imagepath,savepath,n=None,f=None,numCols=None,numRows=None,savesmall=False,imgtype=''):
    """Performs full-size module image processing steps, including
        lens correction, planar indexing, and cell extraction, if desired.
        
        Lens correction is performed if n and f are provided.
        n and f can be found with the GetLensCorrectParams function.
        Cells are extracted if numCols and numRows are provided.

    Args:
        imagepath (str): path to a raw image
        savepath (str): folder path for saving output
        numCols (int): number of cells across in module image
        numRows (int): number of cells down in module image
        savesmall (bool): Save a smaller .jpg version of the planar indexed
            image with True. Default is False.
        imgtype (str):  'UVF' UV Fluorescence Image
                        'gradient' for unequal intensity across the image
                        'lowcon' low contrast between cell and background
                            or PL images without background subtraction
    Returns:
        
    """ 
    img = cv2.imread(imagepath)
    if (n is not None) and (f is not None):
        img = process.lensCorrect(img,n,f)
    planarindexed = process.PlanarIndex(img,imgtype)
    file_name = os.path.split(imagepath)[1]
    image_name = savepath+file_name
    cv2.imwrite(image_name,planarindexed)
    if savesmall == True:
        dims = planarindexed.shape
        y = int(dims[0]/3)
        x = int(dims[1]/3)
        jpg_name = os.path.splitext(image_name)[0]+'.jpg'
        cv2.imwrite(jpg_name,cv2.resize(planarindexed,(x,y)))
    if (numCols is not None) and (numRows is not None):
        cellarrays = process.CellExtract(planarindexed,numCols,numRows)
        for i in range(len(cellarrays)):
            out = cellarrays[i]
            file_name,ext = os.path.splitext(os.path.split(imagepath)[1])
            image_name = savepath+os.path.splitext(file_name)[0]+'-c'+ '{:02}'.format(i+1) + ext
            cv2.imwrite(image_name,out)
    return True

