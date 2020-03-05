import os,shutil,glob,cv2
from PIL import Image

def demo():
    imgs_dir='/home/ars/disk/chaoyuan/dataset/VIN码识别/0113'
    labels_dir='/home/ars/disk/chaoyuan/dataset/VIN码识别/0113_psenet_labels'
    out_dir='/home/ars/disk/chaoyuan/dataset/VIN码识别/ocr_dataset'
    resize_ratio=0.35
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for i,f in enumerate(glob.glob(labels_dir+'/*.txt')):
        imf=imgs_dir+'/'+os.path.basename(f).replace('.txt','.jpg')
        f2=out_dir+'/'+os.path.basename(f)
        imf2=out_dir+'/'+os.path.basename(imf)

        shutil.copy(f,f2)
        img=Image.open(imf)
        w,h=img.size
        w=int(w*resize_ratio)
        h=int(h*resize_ratio)
        img=img.resize((w,h))
        img.save(imf2)
        # shutil.copy(imf,imf2)
        print(i,f)

if __name__ == '__main__':
    demo()
