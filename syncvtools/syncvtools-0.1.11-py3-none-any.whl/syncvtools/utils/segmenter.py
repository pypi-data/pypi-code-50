'''
Based on this one: https://github.com/SyntechCorporation/Computer-Vision/blob/master/scripts/tfrecords/segment.py
Changes:
- Margin is set to 0
- Never crops the GT bounding boxes
'''

import cv2, logging
import numpy as np
from syncvtools.data.detections import ImageLevelDetections
import copy
from syncvtools.data.bbox import Bbox

WHITE_THRESHOLD = 25
MARGIN = 0

def crop_x_direction(binarized_image):

    width_flatten = binarized_image.min(axis=0)
    i_left, i_right = -1, -1
    # find i_left
    for i,intensity in enumerate(width_flatten):
        if intensity == 0:
            i_left = i
            break

    width_flatten = np.flip(width_flatten, axis=0)

    for i,intensity in enumerate(width_flatten):
        if intensity == 0:
            i_right = len(width_flatten) - i + 1
            break

    if i_left < 0 or i_right < 0:
        #print("something went wrong x")
        return None, None

    return i_left, i_right

def crop_y_direction(binarized_image):

    height_flatten = binarized_image.min(axis=1)
    i_top, i_bot = -1, -1

    #find i_t
    for i,intensity in enumerate(height_flatten):
        if intensity == 0:
            i_top = i
            break

    height_flatten = np.flip(height_flatten, axis=0)

    for i,intensity in enumerate(height_flatten):
        if intensity == 0:
            i_bot = len(height_flatten) - i + 1
            break

    if i_top < 0 or i_bot < 0:
        #print("something went wrong y")
        return None, None

    return i_top, i_bot


def get_new_label_root(img_det, crop_bbox):
    #with open(label_file, 'r') as fid:
    #    xml_str = fid.read()
    #xml = etree.fromstring(xml_str)
    # groundtruth = recursive_parse_xml_to_dict(xml_tree)['annotation']
    if img_det.ground_truth:
        w,h  = crop_bbox[2] - crop_bbox[0], crop_bbox[3] - crop_bbox[1]
        for gt in img_det.ground_truth[:]: #so we can delete from  this array in a loop
            bbox = min(w,max(0, gt.bbox.bbox_abs[0] - crop_bbox[0])),\
                   min(h,max(0, gt.bbox.bbox_abs[1] - crop_bbox[1])),\
                   min(w, gt.bbox.bbox_abs[2] - crop_bbox[0]),\
                   min(h, gt.bbox.bbox_abs[3] - crop_bbox[1])
            #if bbox is zero w/h - drop it
            if bbox[2]-bbox[0] < 1 or bbox[3]-bbox[1] < 1:
                img_det.ground_truth.remove(gt)
                logging.warning("GT Box ({}) out of the crop area ({}): ".format(list(gt.bbox.bbox_abs),list(crop_bbox)))
            gt.bbox = Bbox(bbox_abs=bbox,img_size=img_det.img.img_size)




def get_crop_bbox(img_det):
    ''' get [x_min, y_min, x_max, y_max] for image crop
    Args:
       image: numpy array
    '''
    img_np = img_det.img.img_np
    gray_image = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    binarized_image = cv2.threshold(gray_image, 255 - WHITE_THRESHOLD, 255, cv2.THRESH_BINARY)[1]
    binarized_image = cv2.medianBlur(binarized_image, 3)
    binarized_image = cv2.medianBlur(binarized_image, 3)
    i_top, i_bot = crop_y_direction(binarized_image)
    if i_top == None or i_bot == None:
        return None
    i_left, i_right = crop_x_direction(binarized_image)
    if i_left == None or i_right == None:
        return None

    #ADDING MARGIN
    i_top = max(0, i_top - MARGIN)
    i_bot = min(img_np.shape[0], i_bot + MARGIN)
    i_left = max(0, i_left - MARGIN)
    i_right = min(img_np.shape[1], i_right + MARGIN)


    if img_det.ground_truth:
        #building a convex box over all GT boxes so we wan't cut GT accidently
        min_x, min_y, max_x, max_y = img_np.shape[1], img_np.shape[0], 0, 0
        for gt in img_det.ground_truth: #so we can delete from  this array in a loop
            #print("GT:", gt.bbox.bbox_abs)
            min_x = min(min_x, gt.bbox.bbox_abs[0])
            min_y = min(min_y, gt.bbox.bbox_abs[1])
            max_x = max(max_x, gt.bbox.bbox_abs[2])
            max_y = max(max_y, gt.bbox.bbox_abs[3])
        i_left = min(min_x, i_left)
        i_top =  min(min_y, i_top)
        i_right = max(i_right, max_x)
        i_bot = max(i_bot, max_y)
        #print("IMG size:", img_np.shape)
        #print(min_x,min_y,max_x,max_y)
        #print(i_left, i_top,  i_right, i_bot)

    return i_left, i_top,  i_right, i_bot

def crop_image(imgdet, crop_bbox):
    cropped_image = imgdet.img.img_np[crop_bbox[1]:crop_bbox[3], crop_bbox[0]:crop_bbox[2], :]
    imgdet.img.img_np = cropped_image

def segment(imgdet: ImageLevelDetections) -> ImageLevelDetections:
    '''
    Returns segmentd copy of the object
    :param imgdet: image with detections
    :return: copy with cropped image (deepcopies the object)
    '''
    imgdet_copy = copy.deepcopy(imgdet)
    try:
        crop_bbox = get_crop_bbox(imgdet_copy)
    except Exception as e:
        #logging.warning("Failed to segment: {}".format(imgdet_copy.img.img_src))
        raise ValueError("Failed to get crop box for segmentation: {}. Error: {}".format(imgdet_copy.img.img_src,str(e)))
    if crop_bbox is None:
        raise ValueError("Empty cropbox after segmentation: {}.".format(imgdet_copy.img.img_src))
    try:
        crop_image(imgdet_copy, crop_bbox)
        get_new_label_root(imgdet_copy, crop_bbox)
        if imgdet_copy.img.img_size.width < 50 or imgdet_copy.img.img_size.height < 50:
            raise ValueError("Segmentation error. Resulting image too small: {}.".format(imgdet_copy.img.img_src))
        else:
            return imgdet_copy
    except Exception as e:
        raise ValueError("Segmentation error. Failed to apply crop: {}.. Error: {} ".format(imgdet_copy.img.img_src,str(e)))

