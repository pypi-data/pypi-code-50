
import os,shutil,glob,random,cv2,json
from PIL import Image
from wpkit.utils import json_load

def load_plain_annotation(path):
    # lines=[]
    with open(path,'r') as f:
        lines=f.read()
    lines