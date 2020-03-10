Ans="""
from PIL import Image
import numpy as np
a=Image.open('D:\sy16\linear alg\image1')
b=Image.open('D:\sy16\linear alg\image2')
l1=np.array(a)
l2=np.array(b)
def imresize(im,sz):
        PIL_im=Image.fromarray(np.unit8(im))
        return np.array(PIL_im.resize(sz))
r1=imresize(l1,(200,200))
r2=imresize(l2,(200,200))
a1=Image.fromarray(r1)
b1=Image.fromarray(r2)
a1.show()
b1.show()


"""
