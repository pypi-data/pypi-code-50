# -*- coding: utf-8 -*-

import csv
import codecs

import os
import sys
import random
import math
import skimage.io

from picdetect.config import Config
from picdetect import model as modellib
from picdetect import visualize1

import warnings
warnings.filterwarnings("ignore")

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Run Object Detection


def CreateModel(model_path):
    # Root directory of the project
    ROOT_DIR = os.path.abspath("/home/data/Mask_RCNN/")

    # Directory to save logs and trained model
    MODEL_DIR = os.path.join(ROOT_DIR, "logs")

    class InferenceConfig(Config):
        # Set batch size to 1 since we'll be running inference on
        # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
        # Give the configuration a recognizable name
        NAME = "ship"

        # We use a GPU with 12GB memory, which can fit two images.
        # Adjust down if you use a smaller GPU.
        IMAGES_PER_GPU = 1

        # Number of classes (including background)
        NUM_CLASSES = 1 + 1  # Background + balloon

        # Number of training steps per epoch
        STEPS_PER_EPOCH = 100

        # Skip detections with < 90% confidence
        DETECTION_MIN_CONFIDENCE = 0.9

    config = InferenceConfig()
    # config.display()

    # Create Model and Load Trained Weights
    # Create model object in inference mode.
    PicModel = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
    # Load weights trained on MS-COCO
    PicModel.load_weights(model_path, by_name=True)
    # 模型预热
    image_temp = skimage.io.imread("/home/data/data/img/2.jpg")
    r = PicModel.detect([image_temp], verbose=1)

    return PicModel


def detect(Model, list, output_path_image, output_path_tuples):
    class_names = ['BG', 'ship']
    for img_path in list:
        imagename = img_path[img_path.rfind('/'):][1:]
        image = skimage.io.imread(img_path)
        file_name = imagename.split('.')[0]

        # Run detection
        results = Model.detect([image], verbose=1)

        # Visualize results
        r = results[0]
        visualize1.display_instances(file_name, image, r['rois'], r['masks'], r['class_ids'],
                                     class_names, output_path_image, r['scores'])

        filecsvName = output_path_tuples + "ex_" + file_name + ".csv"
        with codecs.open(filecsvName, 'w', 'utf-8-sig') as csvfile:

            # 指定 csv 文件的头部显示项
            filednames = ['head', 'relation', 'tail']
            writer = csv.DictWriter(csvfile, fieldnames=filednames)

            books = []
            if len(r['rois']) > 1:
                for i in range(0, len(r['rois']) - 1):
                    ycenter = (r['rois'][i][0] + r['rois'][i][2]) / 2
                    xcenter = (r['rois'][i][1] + r['rois'][i][3]) / 2
                    for j in range(i + 1, len(r['rois'])):
                        # print(r['rois'][i])
                        # print(r['rois'][j])
                        y1center = (r['rois'][j][0] + r['rois'][j][2]) / 2
                        x1center = (r['rois'][j][1] + r['rois'][j][3]) / 2
                        # print(str(ycenter) + ',' + str(xcenter))
                        # print(str(y1center) + ',' + str(x1center))
                        if ycenter <= y1center and xcenter <= x1center:
                            relat = '右后方'
                            # print("船只%d,右后方,船只%d" % (i, j))
                        else:
                            if ycenter <= y1center and xcenter > x1center:
                                relat = '左后方'
                                # print("船只%d,左后方,船只%d" % (i, j))
                            else:
                                if ycenter > y1center and xcenter <= x1center:
                                    relat = '右前方'
                                    # print("船只%d,右前方,船只%d" % (i, j))
                                else:
                                    relat = '左前方'
                                    # print("船只%d,左前方,船只%d" % (i, j))
                        book = {
                            'head': '船只' + str(i),
                            'relation': relat,
                            'tail': '船只' + str(j)
                        }
                        books.append(book)
            else:
                book = {
                    'head': '船只0',
                    'relation': '位置',
                    'tail': '(' + str(r['rois'][0][1]) + ',' + str(r['rois'][0][0]) + ',' + str(r['rois'][0][2] - r['rois'][0][0]) + ',' + str(r['rois'][0][3] - r['rois'][0][1]) + ')'
                }
                books.append(book)
            writer.writeheader()
            for book in books:
                writer.writerow({'head': book['head'], 'relation': book['relation'], 'tail': book['tail']})
