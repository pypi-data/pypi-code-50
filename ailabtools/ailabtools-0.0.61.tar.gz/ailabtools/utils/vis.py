import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import math
from PIL import Image, ImageDraw
import os

def show_multi_image(imgs):
    nImgs = len(imgs)
    fig=plt.figure(figsize=(nImgs * 10,10))
    nCols = nImgs
    nRows = nImgs // nCols
    for i, v in enumerate(imgs):
        fig.add_subplot(1, nImgs, i + 1)
        plt.imshow(v)
    plt.show()

def show_overlap(img, mask, alpha=0.5):
    fig = Figure(figsize=(10,10))
    canvas = FigureCanvas(fig)
    ax = fig.gca()
    ax.imshow(img)
    ax.imshow(mask, alpha=alpha)
    ax.axis('off')
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    canvas.draw()
    width, height = (fig.get_size_inches() * fig.get_dpi()).astype(np.int16)
    image = np.fromstring(canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)
    return image

def build_sprite_img(imgs, size):
    total_img = len(imgs)
    per_row = int(math.sqrt(total_img))+1
    
    master_width = (size * per_row)
    master_height = (size * per_row)
    master = Image.new(
            mode='RGB',
            size=(master_width, master_height),
            color=(0,0,0))

    for idx, img in enumerate(imgs):
        y = idx//per_row
        x = idx%per_row
        x = x*size
        y = y*size
        pil_img = img.resize((size, size)).convert('RGB')
        master.paste(pil_img,(x,y))
        
    return master

def build_clustering(path, features, imgs=None, img_size=92):
    # path: save path
    # features: [n, feature_length]
    # img: [pil_img]
    import os
    import tensorflow as tf
    from tensorflow.contrib.tensorboard.plugins import projector

    if imgs != None:
        metadata = 'metadata.png'
        sprite_img = build_sprite_img(imgs, img_size)
        sprite_img.save(os.path.join(path, metadata))

    feature_vector = tf.Variable(features, name='feature_vector')
    with tf.Session() as sess:
        saver = tf.train.Saver([feature_vector])
        sess.run(feature_vector.initializer)
        saver.save(sess, os.path.join(path, 'feature_vector.ckpt'))
        config = projector.ProjectorConfig()
        # One can add multiple embeddings.
        embedding = config.embeddings.add()
        embedding.tensor_name = feature_vector.name
        # Link this tensor to its metadata file (e.g. labels).
        if imgs != None:
            embedding.sprite.image_path = metadata
            embedding.sprite.single_image_dim.extend([img_size, img_size])
        # Saves a config file that TensorBoard will read during startup.
        projector.visualize_embeddings(tf.summary.FileWriter(path), config)

    print("tensorboard --logdir={}".format(os.path.abspath(path)))