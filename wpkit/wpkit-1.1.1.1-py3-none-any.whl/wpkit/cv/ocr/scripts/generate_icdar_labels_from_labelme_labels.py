import os,shutil,glob
from wpkit.utils import json_load,TextFile,remake
import numpy
def convert_label(n):
    n=int(n)
    if n==0:
        n=19
    return "#"*n
def demo():
    src_dir=r'D:\work\data\vin码\0113_colabeler'
    out_dir=r'D:\work\data\vin码\0113_psenet_labels'
    resize_ratio=0.35
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    json_files=glob.glob(src_dir+'/*.json')
    for i,f in enumerate(json_files):
        obj=json_load(f)
        points=obj['shapes'][0]['points']
        points=[int(coord) for pt in points for coord in pt ]
        points=[int(x*resize_ratio) for x in points]
        label=obj['shapes'][0]['label']
        label=convert_label(label)
        label=[*points,label]
        label=[str(x) for x in label]
        label=','.join(label)
        p=obj['imagePath']
        f2=out_dir+'/'+p.replace('.jpg','.txt')
        TextFile(f2).write(label)
        print(i,f)




if __name__ == '__main__':
    demo()