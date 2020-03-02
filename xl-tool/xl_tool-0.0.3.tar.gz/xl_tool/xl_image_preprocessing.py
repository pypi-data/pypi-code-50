"""图片预处理"""
import os
from PIL import Image
import numpy as np
from xl_tool.xl_io import file_scanning, time_analysis_wrapper
from tqdm import tqdm
import shutil


def grey_world(img_array):
    """白平衡处理函数
    Args:
        img_array:输入三通道图像数组
    """
    R = img_array[:,:,0].mean()
    G = img_array[:,:,1].mean()
    B = img_array[:,:,2].mean()
    avg = (B + G + R) / 3  
    img_array[:,:,0] = np.minimum(img_array[:,:,0] * (avg / R), 255)  
    img_array[:,:,1] = np.minimum(img_array[:,:,1] * (avg / G), 255)  
    img_array[:,:,2] = np.minimum(img_array[:,:,2] * (avg / B), 255)  
    return  img_array.astype(np.uint8)

def read_image(file, target_size=(224,224)):
    """以指定的尺寸读取数据，并返回图像数组"""
    img = Image.open(file)
    img = img.resize(target_size)
    if img.mode in ["P","L"]:
        img = img.convert("RGB")
    return np.array(img)
    
