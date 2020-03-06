'''
Direct conversion scripts which are too complicated to do through our classes.
Most of conversions are done through data_import and data_export
'''

from typing import List, Dict, Any, Callable
import logging, os
from tqdm import tqdm
import syncvtools.utils.file_tools as ft
from syncvtools.utils.data_export import COCOExport
from syncvtools.utils.data_import import TFRecords
from syncvtools.utils._dependencies import dep


def tfrecord_to_coco(tfrecord_src, out_json_path, out_img_path, label_map=None):
    '''
    Takes TF Record and converts it to MSCOCO format for BBOX detection without loading TF record to memory.
    :param tfrecord_file: input tf record
    :param annotation_file: output JSON file for MSCOCO annotations
    :param out_img_path: output directory to store images extracted from TF record
    :return:
    '''

    label_map_direct = ft.pbmap_read_to_dict(label_map)
    label_map_inverse = {v: k for k, v in label_map_direct.items()}

    # LOADING ITERATIVELY TF RECORD. We can't just read the whole thing to memory using data_import.
    # tf = dep('tf')
    # tf_obj_det_decoder = dep('tf_obj_det_decoder')
    # raw_dataset = tf.data.TFRecordDataset([tfrecord_src])
    # decoder = tf_obj_det_decoder()

    output, counters = COCOExport.generate_coco_header()
    coco_images = []
    coco_annotations = []
    counter_written = 0
    for img_key, imgdet_obj in tqdm(TFRecords.to_det_col_iter(tfrecord_src=tfrecord_src)):
        # img_key, imgdet_obj = TFRecords.record_to_object(decoder=decoder, tf_one_record=raw_record)
        imgdet_obj.process_labelmap(label_map=label_map_direct,
                                    inverse_label_map=label_map_inverse)

        coco_image, coco_annotation = COCOExport.convert_one(img_det=imgdet_obj, counters=counters)
        coco_images.append(coco_image)
        coco_annotations += coco_annotation
        assert imgdet_obj.img.img_filename
        ft.img_np_to_disk(img_np=imgdet_obj.img.img_np,
                          save_path=os.path.join(out_img_path, imgdet_obj.img.img_filename))
        counter_written += 1

    categories_list = []
    categories_set = set()
    for coco_annotation in coco_annotations:
        if coco_annotation['category_id'] in categories_set:
            continue
        categories_set.add(coco_annotation['category_id'])
        categories_list.append({'supercategory': "threat",
                                'id': coco_annotation['category_id'],
                                'name': coco_annotation['category_txt']}
                               )
    output['categories'] = categories_list
    output['annotations'] = coco_annotations
    output['images'] = coco_images
    logging.info("Dumping annotations to file {}".format(out_json_path))
    ft.json_object_to_file(path_src=out_json_path, data_obj=output)
    logging.info("Done. {} written".format(counter_written))
