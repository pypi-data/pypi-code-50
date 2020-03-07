# Python program to read 
# image using PIL module 

# importing PIL 
from PIL import Image # pip install Pillow
import numpy as np
from m2controller import m2Const
import ctypes

def __readIcoImage(imagefilepath):
    errMsg = ''
    np_im = []
    # Read image 
    img = Image.open(imagefilepath) 

    # Output Images 
    #img.show()

    # prints format of image 
    #print(img.format)
    #if (img.format != 'ICO'):
    #    errMsg = errMsg + "expect the image file format to be ICO"
    #    return [errMsg,np_im]
    # prints mode of image 
    #print(img.mode) 
    #if (img.mode != 'RGBA'):
    #    errMsg = errMsg + "expect the image file mode to be RGBA"
    #    return [errMsg,np_im]

    np_im = np.array(img)
    if np_im.shape[0] != 16 or np_im.shape[1] != 16 or (np_im.shape[2] != 3 and np_im.shape[2] != 4):
        errMsg = errMsg + "Expect image dimension 16-by-16-by-(3(RGB) or 4(RGBA))"
        return [errMsg,np_im]
    
    return [errMsg,np_im]

def RGB2int(R,G,B):
    uint32Bytes = bytes([R,G,B,0])
    return np.frombuffer(uint32Bytes, dtype=np.uint32)

def int2RGB(np_uint32Val):
    byteVal = np.ndarray.tobytes(np.array([np_uint32Val],dtype='uint32')) # default little endian
    R = byteVal[0]
    G = byteVal[1]
    B = byteVal[2]
    return [R,G,B]
    
def __convertImg2arr(np_im):
    rgbrr = np.zeros(m2Const.ledmatrixSize*m2Const.ledmatrixSize, dtype=np.uint32)
    for ii in range(m2Const.ledmatrixSize):
        for jj in range(m2Const.ledmatrixSize):
            if ii%2 == 0:
                pixel = np_im[ii][jj]
            else:
                pixel = np_im[ii][m2Const.ledmatrixSize-1-jj]
            rgbrr[ii*m2Const.ledmatrixSize+jj] = RGB2int(pixel[0],pixel[1],pixel[2])
    return rgbrr

def np3Darr_to_IndexListsAndRGB(np_im): # 3D arr(row,col,rgb)
    indexSameRGB = []
    RGBvalues = []
    npArr = __convertImg2arr(np_im)
    uniqueRGB = np.unique(npArr)
    for colorii in range(uniqueRGB.__len__()):
        LEDindex_np64 = np.where(npArr == uniqueRGB[colorii])
        LEDindex = []
        for ledii in range(LEDindex_np64[0].__len__()):
            LEDindex.append(int(LEDindex_np64[0][ledii]))
        indexSameRGB.append(list(LEDindex))
        RGBvalues.append(int2RGB(uniqueRGB[colorii]))
    return [indexSameRGB,RGBvalues]

def icoImage2LEDmatrix2DindexAndRGB(imagefilepath):
    [errMsg,np_im] = __readIcoImage(imagefilepath)
    if errMsg.__len__() != 0:
        print(errMsg)
        print('bad image, abort LED matrix control')
        indexSameRGB = []
        RGBvalues = []
        return [errMsg,indexSameRGB,RGBvalues]
    [indexSameRGB,RGBvalues] = np3Darr_to_IndexListsAndRGB(np_im)
    return [errMsg,indexSameRGB,RGBvalues]

if __name__ == "__main__":
    icoImage2LEDmatrixCtrlData('./pacwoman2.ico')
    
    
    
    
    
    
