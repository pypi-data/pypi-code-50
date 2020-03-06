'''
Exports data into from native classes into different formats
'''

from typing import List, Dict, Any, Callable
from syncvtools.data.image import Image
from syncvtools.data.detections import DetectionEntity, DetectionsCollection, ImageLevelDetections
import cv2, os, glob, json, hashlib
import numpy as np
import logging
from tqdm import tqdm
import syncvtools.utils.file_tools as ft
from syncvtools.utils._dependencies import dep, is_tf_one
from syncvtools.utils.segmenter import segment as segment_func
import datetime


class TFRecordsExport:
    @staticmethod
    def export(src: DetectionsCollection, out_path: str, segment=False, dump_keys_path=None):
        '''
        Dumps DetectionsCollection object into TensorFlow record format in Object Detection API format.
        :param src:
        :param out_path: path to save TF Record
        :return:
        '''
        if not src:
            raise ValueError("Empty input DetectionsCollection")
        test = next(iter(src.values()))

        tf = dep('tf')
        TFRecordWriter = tf.python_io.TFRecordWriter if is_tf_one(tf) else tf.io.TFRecordWriter
        logging.info("FIXED2 Segmentation is enabled for {}".format(out_path))
        final_keys = set()
        success_count = 0
        with  TFRecordWriter(out_path) as writer:
            for det_obj in tqdm(src):
                if det_obj in final_keys:
                    logging.warning("TF Record export collision: {}".format(det_obj))
                    continue
                try:
                    tf_det_obj = TFRecordsExport._convert_image(img_det=src[det_obj], img_key=det_obj, segment=segment)
                except Exception as e:
                    logging.warning("Convert to TF record failed: {}. Msg: {}".format(det_obj, str(e)))
                    continue
                final_keys.add(det_obj)
                writer.write(tf_det_obj.SerializeToString())
                success_count += 1
        if dump_keys_path:
            ft.list_to_file(path_dest=dump_keys_path, list_obj=sorted(list(final_keys)))
        logging.info("TF Record written: {}. Objects written: {}".format(out_path, success_count))

    @staticmethod
    def _convert_image(img_det: ImageLevelDetections, img_key: str, segment=False):
        '''
        Pieces from  Synapse CV repo and Object Detection API
        :param img_det:
        :return:
        '''

        def int64_feature(value):
            return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

        def int64_list_feature(value):
            return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

        def bytes_feature(value):
            return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

        def bytes_list_feature(value):
            return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))

        def float_list_feature(value):
            return tf.train.Feature(float_list=tf.train.FloatList(value=value))

        if not img_det.img:
            raise ValueError("Image is not set")
        tf = dep('tf')
        if segment:
            logging.debug("GT before segment {}: {}".format(img_key, img_det))
            img_det = segment_func(img_det)  # returns segmented copy of the original object raises ValueError
            logging.debug("GT after segment {}: {}".format(img_key, img_det))
        # to use OpenCV for encoding we need convert to BGR
        img_np = cv2.cvtColor(img_det.img.img_np, cv2.COLOR_RGB2BGR)
        img_conv_success, jpeg_numpy = cv2.imencode('.png', img_np)
        if not img_conv_success:
            raise ValueError("Cannot encode numpy image to jpg! Status: {}".format(img_conv_success))
        image_enc_bytes = jpeg_numpy.tostring()
        key = hashlib.sha256(image_enc_bytes).hexdigest()
        bbox_coords = ([], [], [], [])
        classes = []
        classes_text = []
        label_full_tag = []
        truncated = []
        poses = []
        difficult_obj = []
        if img_det.ground_truth is None:
            raise ValueError("Ground truth is not set for the input. TF format expects ground truth.")

        for gt in img_det.ground_truth:
            if gt.label_id is None:
                raise ValueError(
                    "You need to assign label_id to all boxes. Call .process_labelmap() on DetectionCollections object")
            classes.append(gt.label_id)
            if not gt.label_text:
                raise ValueError(
                    "You need to assign label_text to all boxes. Call .process_labelmap() on DetectionCollections object")
            classes_text.append(gt.label_text.encode('utf-8'))
            if gt.label_full_tag is not None:
                label_full_tag.append(gt.label_full_tag.encode('utf-8'))
            truncated.append(0)
            difficult_obj.append(0)
            poses.append("".encode('utf8'))
            for i in range(len(bbox_coords)):
                bbox_coords[i].append(gt.bbox.bbox_norm[i])

        return tf.train.Example(features=tf.train.Features(feature={
            'image/height': int64_feature(img_det.img.img_size.as_tuple()[1]),
            'image/width': int64_feature(img_det.img.img_size.as_tuple()[0]),
            'image/filename': bytes_feature(
                img_det.img.img_filename.encode('utf8')),
            'image/source_id': bytes_feature(
                img_det.img.img_filename.encode('utf8')),
            'image/key/sha256': bytes_feature(key.encode('utf8')),
            'image/encoded': bytes_feature(image_enc_bytes),
            'image/format': bytes_feature('png'.encode('utf8')),
            'image/object/bbox/xmin': float_list_feature(bbox_coords[0]),
            'image/object/bbox/xmax': float_list_feature(bbox_coords[2]),
            'image/object/bbox/ymin': float_list_feature(bbox_coords[1]),
            'image/object/bbox/ymax': float_list_feature(bbox_coords[3]),
            'image/object/class/text': bytes_list_feature(classes_text),
            'image/object/class/label': int64_list_feature(classes),
            'image/object/difficult': int64_list_feature(difficult_obj),
            'image/object/truncated': int64_list_feature(truncated),
            'image/object/view': bytes_list_feature(poses),
            'image/object/category': bytes_list_feature(label_full_tag),
        }))


class PascalVOCExport:
    @staticmethod
    def export(src: DetectionsCollection, out_img_path: str = None, out_xml_path: str = None) -> None:
        '''

        :param src: DetectionsCollection list of ImageLevelDetections
        :param out_img_path: path to save images
        :param out_xml_path: path to save strings
        :return:
        '''
        if not src:
            raise ValueError("None input DetectionsCollection: unable to export.")

        for det_key in src:
            if out_xml_path:
                xml_format = PascalVOCExport.convert_one(img_det=src[det_key])
                out_filename = os.path.join(out_xml_path, "{}.xml".format(det_key))
                ft.xml_write_to_file(input_obj=xml_format, output_file=out_filename)
                logging.info("XML written: {}".format(out_filename))

            if out_img_path:
                img_np = cv2.cvtColor(src[det_key].img.img_np, cv2.COLOR_RGB2BGR)
                out_filename = os.path.join(out_xml_path, src[det_key].img.img_filename)
                cv2.imwrite(out_filename, img_np)
                logging.info("IMAGE written: {}".format(out_filename))

    @staticmethod
    def convert_one(img_det: ImageLevelDetections) -> Dict:
        '''
        Encodes one image into dictionary that can be later dumped into XML file in PascalVOC format
        :param img_det:
        :return:
        '''
        xml_format = {'annotation': {'folder': 'fxx',
                                     'filename': img_det.img.img_filename,
                                     'path': img_det.gt_metadata['image_path'] if (
                                             'image_path' in img_det.gt_metadata) else img_det.img.img_filename,
                                     'source': {'database': 'Unknown'},
                                     'size': {'width': img_det.img.img_size.width,
                                              'height': img_det.img.img_size.height,
                                              'depth': img_det.img.img_size.channels},
                                     'segmented': 0,
                                     'object': []
                                     }
                      }
        if img_det.ground_truth:
            for gt in img_det.ground_truth:
                xmin, ymin, xmax, ymax = gt.bbox.bbox_abs
                xml_format['annotation']['object'].append({'name': gt.label_full_tag or gt.label_text,
                                                           'pose': 'Unspecified',
                                                           'difficult': 0,
                                                           'bndbox': {'xmin': xmin, 'ymin': ymin, 'xmax': xmax,
                                                                      'ymax': ymax}})
        return xml_format


class ProdDetectionsExport:
    @staticmethod
    def convert_one(img_det: ImageLevelDetections) -> List:
        '''
        Encodes detections into our JSON raw_inference format and returns suitable dict
        :param img_det:
        :return:
        '''
        json_format = [{'view': 'top', 'object_classes': [], 'model_ids': [], 'inferences': []}]
        if img_det.detections:
            for dt in img_det.detections:
                result = {'class': dt.label_text,

                          'score': {'raw_score': np.float64(dt.score),
                                    'normalized_score': None,
                                    'composite_score': None}}
                if dt.bbox:
                    xmin, ymin, xmax, ymax = dt.bbox.bbox_abs
                    result['bounding_box'] = {'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax}
                    result['type'] = 'box'
                elif dt.point:
                    xcenter, ycenter = dt.point.point_abs
                    result['type'] = 'point'
                    result['point'] = {'xcenter': xcenter, 'ycenter': ycenter}
                else:
                    raise ValueError("None of detection types is found")
                json_format[0]['inferences'].append(result)
        return json_format

    @staticmethod
    def convert_one_save(path_src: str,
                         img_det: ImageLevelDetections,

                         saver_func: Callable[[str, Any], None] = ft.json_object_to_file
                         ):
        '''
        Converts and saves one image into our ProdServer JSON format (raw_inferences)
        :param path_src: json path to save
        :param img_det:
        :param saver_func: default saves to JSON, provide different function
        to let's say the same structure in XML or YAML
        :return:
        '''
        data_obj = ProdDetectionsExport.convert_one(img_det=img_det)
        saver_func(path_src, data_obj)


class COCOExport:
    '''
    MS COCO Exporting class. Exports only annotations into one big JSON file.
    Label_id should be set for all predictions!
    '''

    @staticmethod
    def convert_one(img_det: ImageLevelDetections, counters: Dict[str, int]) -> Any:
        # IMAGE
        image = {}
        image['license'] = 3
        image['url'] = 'http://synapsetechnology.com'
        image['file_name'] = img_det.img.img_filename
        image['width'] = img_det.img.img_size.width
        image['height'] = img_det.img.img_size.height
        image['date_captured'] = '2019-09-03 15:26:19'
        counters['image_ids'] += 1
        image['id'] = counters['image_ids']
        categories = {}
        # BOXES / ANNOTATIONS
        annotations_list = []
        # for bbox, label_num, label_txt in zip(data_element.groundtruth_boxes,
        #                                       data_element.groundtruth_classes_num,
        #                                       data_element.groundtruth_classes_text):
        for gt in img_det.ground_truth:
            if gt.label_id is None:
                raise ValueError(
                    "label_id is not set for some ground truth. Apply label_map to your loaded dataset first.")
            counters['annotation_ids'] += 1
            bbox_coords = gt.bbox.bbox_abs_x1y1wh()
            bbox_area = bbox_coords[2] * bbox_coords[3]
            annotations_list.append({'bbox': bbox_coords,
                                     'area': bbox_area,
                                     'category_id': gt.label_id,
                                     'id': counters['annotation_ids'],
                                     'iscrowd': 0,
                                     'image_id': counters['image_ids'],
                                     'category_txt': gt.label_text  # hack, doesn't conform to COCO format
                                     })
            # categories[label_num] = label_txt
        return image, annotations_list

    @staticmethod
    def generate_coco_header():
        now = datetime.datetime.now()
        output = {"info":
                      {"description": "Synapse Technology dataset",
                       "url": "http://synapsetechnology.com",
                       "version": "1.0",
                       "year": now.year,
                       "contributor": "Synapse Technology",
                       "date_created": now.strftime("%Y-%m-%d, %H:%M:%S")},
                  "licenses": [{"url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",
                                "id": 1,
                                "name": "Attribution-NonCommercial-ShareAlike License"},
                               {"url": "http://creativecommons.org/licenses/by-nc/2.0/",
                                "id": 2,
                                "name": "Attribution-NonCommercial License"},
                               {"url": "http://creativecommons.org/licenses/by-nc-nd/2.0/",
                                "id": 3,
                                "name": "Attribution-NonCommercial-NoDerivs License"},
                               {"url": "http://creativecommons.org/licenses/by/2.0/",
                                "id": 4,
                                "name": "Attribution License"},
                               {"url": "http://creativecommons.org/licenses/by-sa/2.0/",
                                "id": 5,
                                "name": "Attribution-ShareAlike License"},
                               {"url": "http://creativecommons.org/licenses/by-nd/2.0/",
                                "id": 6,
                                "name": "Attribution-NoDerivs License"},
                               {"url": "http://flickr.com/commons/usage/",
                                "id": 7,
                                "name": "No known copyright restrictions"},
                               {"url": "http://www.usa.gov/copyright.shtml",
                                "id": 8,
                                "name": "United States Government Work"}]
                  }
        counters = {'image_ids': 0, 'annotation_ids': 0}
        return output, counters

    @staticmethod
    def export(src: DetectionsCollection, out_json_path: str = None):

        output, counters = COCOExport.generate_coco_header()

        coco_images = []
        coco_annotations = []
        for img_key in src:
            coco_image, coco_annotation = COCOExport.convert_one(img_det=src[img_key],
                                                                 counters=counters)
            coco_images.append(coco_image)
            coco_annotations += coco_annotation

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


class COCODetectionsExport:
    '''
    COCO detections format
    '''

    def __init__(self, coco_dataset):
        from pycocotools.coco import COCO
        coco = COCO(coco_dataset)
        imgIds = coco.getImgIds()
        self.img_data = coco.loadImgs(imgIds)

    def export(self, src: DetectionsCollection, out_json_path):
        if not self.img_data:
            raise ValueError("COCO Dataset is not init-ed for some reason. self.img_data should be set.")
        results = []
        logging.info("COCO Dataset: {}. Predictions: {}".format(len(self.img_data), len(src)))
        # looping through GT dataset in COCO format
        for img_coco in self.img_data:
            picture_name = os.path.splitext(img_coco['file_name'])[0]
            # if this picture from dataset in predictions
            if picture_name in src:
                for dt in src[picture_name].detections:
                    try:
                        inst = {
                            'image_id': img_coco['id'],  # assign Id from GT dataset
                            'category_id': dt.label_id,
                            'score': dt.score,
                            'bbox': dt.bbox.bbox_abs_x1y1wh()
                        }
                    except ValueError as e:
                        logging.error("Bad bounding in detections box: {}".format(e))
                        continue
                    results.append(inst)
        ft.json_object_to_file(path_src=out_json_path, data_obj=results)
        logging.info("{} instances written to file".format(len(results)))
