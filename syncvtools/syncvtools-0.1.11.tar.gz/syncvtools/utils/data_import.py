'''
Imports images, detections, GTs into native classes.
Usually parse() is main entry point for each Class
'''

from typing import List, Dict, Any, Callable, Tuple, Union
import syncvtools.data.image as syncv_image
import syncvtools.utils.image as syncv_utils_image
from syncvtools.data.detections import DetectionEntity, DetectionsCollection, ImageLevelDetections
from syncvtools import config
import os, glob, json, re
import numpy as np
import logging

root = logging.getLogger()
root.setLevel(logging.INFO)
import syncvtools.utils.file_tools as ft
from syncvtools.utils._dependencies import dep, is_tf_one
from multiprocessing import Process, Queue, Manager
import syncvtools.config as synconfig
from queue import Queue as NormalQueue
import threading


class ProdDetections:
    '''
    Parser for our production inference (raw_inference)
    '''

    @staticmethod
    def to_detection_entity(input_dict: dict) -> DetectionEntity:
        '''
        Convert dict parsed from anywhere in our prod format (inference) to our DetectionEntity (one bbox)
        :param input_dict:
        :return:
        '''
        if 'bounding_box' in input_dict:
            bbox = input_dict['bounding_box']
            bbox = (
            int(round(bbox['xmin'])), int(round(bbox['ymin'])), int(round(bbox['xmax'])), int(round(bbox['ymax'])))
        else:
            bbox = None
        if 'point' in input_dict:
            point = input_dict['point']
            point = (int(round(point['xcenter'])), int(round(point['ycenter'])))
        else:
            point = None
        score = input_dict['score']['raw_score']
        label_txt = input_dict['class']
        det_obj = DetectionEntity(label_text=label_txt,
                                  bbox_abs=bbox,
                                  point_abs=point,
                                  score=score
                                  )
        return det_obj

    @staticmethod
    def from_file(file_src: str,
                  file_parser: Callable[[str], Any] = ft.json_read_to_object) -> Dict[str, List[DetectionEntity]]:
        '''
        Convert prod detection (inference) file to list of DetectionEntity. It can later be inserted into ImageLevelDetections
        :param file_src:
        :param file_parser:
        :return:
        '''
        raw_list = file_parser(file_src)
        all_detections = {}
        for json_view in raw_list:  # TODO ADD LIST TO EXPORTING PREDICTION FORMAT
            view = json_view['view'] if 'view' in json_view else 'default'
            if view not in all_detections:
                all_detections[view] = []
            for json_inference in json_view['inferences']:
                det_obj = ProdDetections.to_detection_entity(input_dict=json_inference)
                all_detections[view].append(det_obj)
        return all_detections

    @staticmethod
    def from_dir(dir_src: str) -> dict:
        '''
        Parse dir with JSON detections from our prod and return dict with img_name => List of DetectionEntity
        Name of file can be a key, or if it's 'raw_inference' than name picked up from corresponding image file in same dir
        :param dir_src: parent dir with detections (dump from ProdServer)
        :return: Dictionary of key: name without ext, value: list of DetectionEntity
        '''
        if not os.path.isdir(dir_src):
            raise ValueError("Provided argument dir_src should be an existing directory: {}".format(dir_src))
        det_files = ft.get_file_list_by_ext(dir=dir_src, ext=('json',), recursive=True)
        result_dict = {}
        for det_file in det_files:
            try:
                dets = ProdDetections.from_file(file_src=det_file)
            except:
                logging.debug("Failing to convert: {}".format(det_file))
                continue
            if os.path.basename(det_file) == config.PROD_RAW_DETECTIONS_NAME:
                det_keys = ft.get_file_list_by_ext(dir=os.path.dirname(det_file), ext=config.DEFAULT_IMG_TYPES,
                                                   recursive=False)
                if not det_keys:
                    raise ValueError(
                        "There should be corresponding images to this JSON file in the same dir. Nothing found")
                for det_key in det_keys:  # path to img
                    img_name = ft.cut_extension(os.path.basename(det_key))
                    vi = re.search(config.PROD_IMG_NAME_VIEW_MASK, img_name)
                    if not vi:
                        logging.warning("NWhere is view? Not recognized image: {}. ".format(det_key))
                        continue
                    vi = vi.group(1)  # i.e. 'top'
                    if vi not in dets:  # no such view in detections
                        logging.warning("No such view in detections: {}. File: {}".format(vi, det_key))
                        continue
                    result_dict[img_name] = dets[vi]
            else:
                det_key = ft.dataset_filename_to_key(det_file)
                dets_arr = []
                for vi in dets:
                    dets_arr.extend(dets[vi])
                result_dict[det_key] = dets_arr
        return result_dict

    @staticmethod
    def parse(predictions_dir: str, img_dir: str = None, return_preds=False, lazy=False) -> Union[
        DetectionsCollection, Dict]:
        '''
        Main entry point.
        :param img_dir: Dir with input images
        :param predictions_dir: Dir with JSON predictions which follow our production format.
        :return: Dictionary with set images and predictions.
        '''
        det_collection = DetectionsCollection()
        preds = ProdDetections.from_dir(predictions_dir)
        if return_preds:
            return preds
        # we create/update DetectionsCollection using our predictions
        det_collection.process_detections(preds, update_only=False)
        if img_dir:
            logging.info("Loading images...")
            imgs = syncv_utils_image.imgs_read_from_dir(img_dir=img_dir, lazy=lazy)
            logging.info("Loading images done.. processing")
            det_collection.process_images(imgs, update_only=True)
            logging.info("Processing images done")
        return det_collection


class TFObjDetAPIDetections:
    '''
    Format for  TF Object Detection API to store predictions after validation in JSON file.
    '''

    @staticmethod
    def to_detections_list(input_dict):
        det_list = []
        # if isinstance(input_dict, int):
        #     print(input_dict)
        for bbox, label_id, score in zip(input_dict['detection_boxes'], input_dict['detection_classes'],
                                         input_dict['detection_scores']):
            bbox = (bbox[1], bbox[0], bbox[3], bbox[2])
            det_obj = DetectionEntity(bbox_norm=tuple(np.asarray(bbox).clip(0.0, 1.0)),
                                      score=score,
                                      label_id=label_id)
            det_list.append(det_obj)

        gt_list = []
        for bbox, label_id, label_txt in zip(input_dict['groundtruth_boxes'],
                                             input_dict['groundtruth_classes'],
                                             input_dict['object_categories']):
            if label_txt.startswith('b\''):
                label_txt = label_txt[2:]
            if label_txt.endswith('\''):
                label_txt = label_txt[:-1]
            bbox = (bbox[1], bbox[0], bbox[3], bbox[2])
            gt_obj = DetectionEntity(bbox_norm=tuple(np.asarray(bbox).clip(0.0, 1.0)),
                                     label_id=label_id,
                                     label_text=label_txt)
            gt_list.append(gt_obj)
        return gt_list, det_list

    @staticmethod
    def parse(detection_file: str,
              file_parser: Callable[[str], Any] = ft.json_read_to_object) -> DetectionsCollection:
        '''
        Main entry point.
        :param detection_file: Path to JSON file (usually detections_and_losses.json).
        :param file_parser: Most of the cases leave default JSON parser.
        :return: Dictionary with groundtruth and predictions, but without image data.
        '''
        raw_dict = file_parser(detection_file)
        det_collection = DetectionsCollection()
        gt_list, det_list = {}, {}
        for det_key in raw_dict:
            if not isinstance(raw_dict[det_key],
                              dict):  ##adding 'num_images' to the level of detections = bad idea, we need to fix it
                continue
            gt_list_per_image, det_list_per_image = TFObjDetAPIDetections.to_detections_list(
                input_dict=raw_dict[det_key])
            det_key = ft.dataset_filename_to_key(det_key)
            gt_list[det_key] = gt_list_per_image
            det_list[det_key] = det_list_per_image

        # we create/update DetectionsCollection using our predictions. label_text not filled, coords are normalized
        det_collection.process_detections(det_list, update_only=False)

        # then we update it with ground truth
        det_collection.process_ground_truth(gt_list, update_only=True)

        return det_collection


class TFRecords:
    '''
    Parse Tensorflow TFRecord format.
    '''

    @staticmethod
    @DeprecationWarning
    def record_to_object(decoder, tf_one_record, is_decoded=False) -> Tuple[str, ImageLevelDetections]:
        '''
        Converts one raw TF record to our internal detection object.
        :param decoder:
        :param tf_one_record:
        :return:
        '''
        if not is_decoded:
            decoded = decoder.decode(tf_one_record)
        else:
            decoded = tf_one_record
        if not is_decoded:
            gt_bboxes = decoded['groundtruth_boxes'].numpy().tolist()
        else:
            gt_bboxes = decoded['groundtruth_boxes']

        for i, bbox in enumerate(gt_bboxes):
            # no idea why tf_example_decoder from Object Detection API makes (ymin,xmin,ymax,xmax) format
            gt_bboxes[i] = (bbox[1], bbox[0], bbox[3], bbox[2])
        if not is_decoded:
            image = decoded['image'].numpy()
        else:
            image = decoded['image']

        # it's BGR
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if not is_decoded:
            image_filename = decoded['filename'].numpy().decode("utf-8")
        else:
            image_filename = decoded['filename'].decode("utf-8")

        key = ft.dataset_filename_to_key(image_filename)

        if not is_decoded:
            image_size = tuple(decoded['image'].get_shape().as_list())
        else:
            image_size = image.shape
        # w,h, channels
        image_size = (image_size[1], image_size[0])

        if not is_decoded:
            gt_classes_num = decoded['groundtruth_classes'].numpy().tolist()
        else:
            gt_classes_num = decoded['groundtruth_classes'].tolist()

        if not is_decoded:
            # our specific tag for original full label tag
            gt_label_full_tag = [x.decode('utf-8') for x in decoded['object_categories'].numpy().tolist()]
        else:
            gt_label_full_tag = [x.decode('utf-8') for x in decoded['object_categories']]

        if not is_decoded:
            gt_classes_text = [x.decode('utf-8') for x in decoded['groundtruth_text'].numpy().tolist()]
        else:
            gt_classes_text = [x.decode('utf-8') for x in decoded['groundtruth_text']]

        gt_obj_list = []
        if len(gt_bboxes) > 0 and not (gt_classes_num or gt_classes_text):
            logging.warning("Neither label id or label_text is set inside TF Record")
        for i, gt_bbox in enumerate(gt_bboxes):
            gt_obj = DetectionEntity(bbox_norm=gt_bbox,
                                     label_id=gt_classes_num[i] if i < len(gt_classes_num) else None,
                                     # what if this one messed??
                                     label_text=gt_classes_text[i] if i < len(gt_classes_text) else None,
                                     label_full_tag=gt_label_full_tag[i] if i < len(gt_label_full_tag) else None,
                                     img_size=image_size)
            gt_obj_list.append(gt_obj)
        img_obj = syncv_image.Image.from_numpy(img_np=image, file_name=image_filename)
        imgdet_obj = ImageLevelDetections(img=img_obj,
                                          ground_truth=gt_obj_list)
        return key, imgdet_obj

    @staticmethod
    @DeprecationWarning
    def _record_to_object_multiprocess(tasks_q, out_q, decoder):
        for raw_record in iter(tasks_q.get, None):
            # while True:
            key, imgdet_obj = TFRecords.record_to_object(decoder=decoder, tf_one_record=raw_record)
            # logging.info("Read {}".format(key))
            out_q.put((key, imgdet_obj))
        out_q.put(None)

    @staticmethod
    @DeprecationWarning
    def _read_tf_record_multithread(tasks_q, tfrecord_src, threads_num):
        tf = dep('tf')
        raw_dataset = tf.data.TFRecordDataset([tfrecord_src])
        logging.debug("Start putting raw records in queue")
        for raw_record in raw_dataset:
            tasks_q.put(raw_record)
        logging.debug("Finished putting raw records in queue")
        for i in range(threads_num):
            tasks_q.put(None)

    @staticmethod
    @DeprecationWarning
    def to_det_col_multithread(tfrecord_src: str):
        '''
        DEPRECATED
        Parses TFRecord into separate imgs and ground truth dictionaries.
        :param tfrecord_src: path to input TF Record
        :return:
        '''
        tf = dep('tf')
        tf_obj_det_decoder = dep('tf_obj_det_decoder')
        raw_dataset = tf.data.TFRecordDataset([tfrecord_src])
        decoder = tf_obj_det_decoder()
        # imgs_dict = {} #images dict key(filename without extension)=>Image
        # gts_dict = {} #ground truth dict key=>DetectionEntity
        tasks_q = Queue()
        out_q = Queue()
        THREADS_NUM = 10
        logging.debug("Start filling queue..")
        # read_thread = Process(target=TFRecords._read_tf_record_multithread, args=(tasks_q, tfrecord_src,THREADS_NUM))
        read_thread = threading.Thread(target=TFRecords._read_tf_record_multithread,
                                       args=(tasks_q, tfrecord_src, THREADS_NUM))
        read_thread.start()
        # read_thread.join()
        # for raw_record in raw_dataset:
        #     tasks_q.put(raw_record)
        logging.debug("End filling queue..")
        thread_list = []

        logging.debug("Start threads..")
        for i in range(THREADS_NUM):
            # tasks_q.put(None)
            reader_p = Process(target=TFRecords._record_to_object_multiprocess, args=(tasks_q, out_q, decoder))
            reader_p.daemon = True
            reader_p.start()
            thread_list.append(reader_p)

        # logging.debug("Threads finished..")
        logging.debug("Arranging dict..")
        res = DetectionsCollection()
        finish_counter = 0
        while True:
            row = out_q.get()
            if not row:
                finish_counter += 1
                if finish_counter == THREADS_NUM:
                    break
                continue
            img_key, img_obj = row
            res[img_key] = img_obj
        read_thread.join()
        logging.debug("Read thread joined")
        for thread in thread_list:
            thread.join()
        logging.debug("Process threads joined")
        logging.debug("Done: Arranging dict..")
        return res

    @staticmethod
    @DeprecationWarning
    def to_dicts(tfrecord_src: str):
        '''
        Parses TFRecord into separate imgs and ground truth dictionaries.
        :param tfrecord_src: path to input TF Record
        :return:
        '''
        tf = dep('tf')
        tf_obj_det_decoder = dep('tf_obj_det_decoder')
        raw_dataset = tf.data.TFRecordDataset([tfrecord_src])
        decoder = tf_obj_det_decoder()
        imgs_dict = {}  # images dict key(filename without extension)=>Image
        gts_dict = {}  # ground truth dict key=>DetectionEntity
        logging.debug("Start tf record iteration..")
        for raw_record in raw_dataset:
            key, img_obj = TFRecords.record_to_object(decoder=decoder, tf_one_record=raw_record)
            gts_dict[key] = img_obj.ground_truth
            imgs_dict[key] = img_obj.img
        logging.debug("Finished tf record iteration..")

        return imgs_dict, gts_dict

    @staticmethod
    @DeprecationWarning
    def to_det_col(tfrecord_src: str):
        '''
        No threads. Writes data directly to DetectionCollection.
        :param tfrecord_src:
        :return:
        '''
        tf = dep('tf')
        tf_obj_det_decoder = dep('tf_obj_det_decoder')
        raw_dataset = tf.data.TFRecordDataset([tfrecord_src])
        decoder = tf_obj_det_decoder()
        logging.debug("Start tf record iteration..")
        res = DetectionsCollection()
        for raw_record in raw_dataset:
            key, img_obj = TFRecords.record_to_object(decoder=decoder, tf_one_record=raw_record)
            res[key] = img_obj
        logging.debug("Finished tf record iteration..")
        return res

    @staticmethod
    def to_det_col_iter(tfrecord_src, shuffle=False):
        '''
        For big TF records this one can be used as iterator:
        for img_key, img_obj in this_func():
            print(img_key)
        :param tfrecord_src:
        :return:
        '''

        def process_fn(value):
            """Sets up tf graph that decodes, transforms and pads input data."""
            processed_tensors = decoder.decode(value)
            return processed_tensors

        tf = dep('tf')
        # it might be accessed directly, public method
        tfrecord_src = ft.cache_file(tfrecord_src)
        # tf.disable_eager_execution()
        tf_obj_det_decoder = dep('tf_obj_det_decoder')
        decoder = tf_obj_det_decoder()
        raw_dataset = tf.data.TFRecordDataset([tfrecord_src])
        if shuffle:
            raw_dataset = raw_dataset.shuffle(buffer_size=100000)
        dataset = raw_dataset.map(process_fn, num_parallel_calls=12)
        if is_tf_one(tf):
            iter = dataset.make_initializable_iterator()
        else:
            iter = tf.compat.v1.data.make_initializable_iterator(
                dataset, shared_name=None
            )
        el = iter.get_next()
        if is_tf_one(tf):
            sess = tf.Session()
        else:
            sess = tf.compat.v1.Session()
        sess.run(iter.initializer)
        logging.debug("Start tf record iteration..")
        try:
            while True:
                decoded = sess.run(el)
                key, img_obj = TFRecords.record_to_object(decoder=None, tf_one_record=decoded, is_decoded=True)
                yield key, img_obj
        except tf.errors.OutOfRangeError as e:
            pass
        logging.debug("Finished tf record iteration..")

    @staticmethod
    def to_det_col_session(tfrecord_src: Union[str, List[str]]):
        '''
        Uses native means of TF to parse graph. Fastest method. No eager execution.
        :param tfrecord_src: path to record or records
        :return:
        '''
        logging.debug("STart tf record parsing..")
        res = DetectionsCollection()
        for key, img_obj in TFRecords.to_det_col_iter(tfrecord_src=tfrecord_src):
            res[key] = img_obj
        logging.debug("Finished tf record parsing..")
        return res

    @staticmethod
    @DeprecationWarning
    def parse2(tfrecord_src: str) -> DetectionsCollection:

        '''
        Main entry function.
        :param tfrecord_src: Input to TF Record
        :return: Returns DetectionCollection with parsed images and ground truth.
        '''
        imgs_dict, gts_dict = TFRecords.to_dicts(tfrecord_src=tfrecord_src)
        det_collection = DetectionsCollection()

        # then we update it with ground truth
        det_collection.process_images(imgs_dict, update_only=False)

        # we create/update DetectionsCollection using our predictions. label_text not filled, coords are normalized
        det_collection.process_ground_truth(gts_dict, update_only=True)
        return det_collection

    @staticmethod
    def parse(tfrecord_src: Union[str, List[str]]) -> DetectionsCollection:
        tfrecord_src = ft.cache_file(tfrecord_src)
        # if not os.path.exists(tfrecord_src):
        #     raise ValueError("TF Record doesnt exist: {}".format(tfrecord_src))
        '''
        Main entry function.
        :param tfrecord_src: Input to TF Record
        :return: Returns DetectionCollection with parsed images and ground truth.
        '''
        logging.info("Reading TF record(s): {}".format(tfrecord_src))
        det_collection = TFRecords.to_det_col_session(tfrecord_src=tfrecord_src)
        return det_collection


class PascalVOC:
    '''
    Format used by LabelImg. One XML file = one image detections.
    '''

    @staticmethod
    def to_detection_entity(input_dict: dict, img_size: Tuple[int, int, int] = None) -> DetectionEntity:
        '''
        Convert dict parsed in PascalVOC format (usually ground truth) to our DetectionEntity (one bbox)
        :param input_dict:
        :return:
        '''
        bbox = input_dict['bndbox']
        bbox = (int(round(float(bbox['xmin']))), int(round(float(bbox['ymin']))),
                int(round(float(bbox['xmax']))), int(round(float(bbox['ymax']))))
        score = None
        label_txt = input_dict['name']
        det_obj = DetectionEntity(label_full_tag=label_txt,
                                  bbox_abs=tuple(bbox),
                                  score=score,
                                  img_size=img_size
                                  )
        return det_obj

    @staticmethod
    def from_file(file_src: str,
                  file_parser: Callable[[str], Any] = ft.parse_xml_pascalvoc) -> Dict:
        '''
        Convert PascalVOC format file to list of DetectionEntity. It can later be inserted into ImageLevelDetections
        :param file_src:
        :param file_parser:
        :return:
        '''
        raw_list = file_parser(file_src)['annotation']
        gt_metadata = {'image_filename': raw_list['filename'],
                       'image_path': raw_list['path'] if 'path' in raw_list else raw_list['filename']}
        img_size = (int(raw_list['size']['width']), int(raw_list['size']['height']), int(raw_list['size']['depth']))
        all_detections = []
        if 'object' in raw_list:
            for detection_xml_element in raw_list['object']:
                det_obj = PascalVOC.to_detection_entity(input_dict=detection_xml_element, img_size=img_size)
                all_detections.append(det_obj)
        return {'ground_truth': all_detections, 'gt_metadata': gt_metadata}

    @staticmethod
    def parse_annotation_dir(filename):
        if filename is None:
            raise ValueError("Filename for annotation can't be none")
        dir_name = os.path.dirname(filename)
        for tag in PascalVOC.annotation_tag_priority:
            if dir_name.endswith(tag):
                return filename, tag
        return filename, None

    annotation_tag_priority = ["_tags_AB_accepted_DR",
                               "_tags_AB_accepted",
                               "_tags_A_DR",
                               "_tags_B_DR",
                               "_tags_accepted",
                               "_tags_A_accepted",
                               "_tags_B_accepted",
                               "_tags_A",
                               "_tags_B",
                               "_tags"]

    @staticmethod
    def from_dir(dir_src: Any) -> dict:
        '''
        Parse dir with JSON detections from our prod and return dict with img_name => List of DetectionEntity
        :param dir_src:
        :return: Dictionary of key: name without ext, value: list of DetectionEntity
        '''

        det_files = []
        inp_dirs = []
        if isinstance(dir_src, str):
            inp_dirs.append(dir_src)
        elif isinstance(dir_src, list) or isinstance(dir_src, tuple):
            inp_dirs += list(dir_src)

        for i, inp_dir in enumerate(inp_dirs):
            if not inp_dirs[i]:
                raise ValueError("Empty dir in dirs: {}".format(inp_dirs))
            if not os.path.isdir(inp_dirs[i]):
                storage_path = os.path.join(synconfig.ANNOTATION_DIR, inp_dirs[i])
                if os.path.isdir(storage_path):
                    inp_dirs[i] = storage_path
                else:
                    raise ValueError("Inp dir doesn't exist: {} or {}".format(inp_dirs[i], storage_path))
            det_files += ft.get_file_list_by_ext(dir=inp_dirs[i], ext=('xml',), recursive=True)
        result_dict = {'ground_truth': {}, 'gt_metadata': {}}

        dir_names = {}

        for det_file in det_files:
            try:
                action = 1  # should we keep this annotation?

                det_key = ft.dataset_filename_to_key(det_file)
                new_annot_file, new_tag = PascalVOC.parse_annotation_dir(det_file)

                if det_key in dir_names:
                    old_annot_file, old_tag = dir_names[det_key]
                    # if we already seen annotation with same key (file name without extension)
                    if new_tag is None and old_tag is None:  # if both annotation names don't have tags
                        logging.warning(
                            "BAD Collision. Dir names without tags: {}, {}".format(old_annot_file, new_annot_file))
                        action = 0  # no, we don't know if it's better then previous one
                    elif new_tag and old_tag:  # if both annotations do have tags, check priority
                        ind_new_tag = PascalVOC.annotation_tag_priority.index(new_tag)
                        ind_old_tag = PascalVOC.annotation_tag_priority.index(old_tag)
                        if ind_new_tag == ind_old_tag:
                            action = 0  # same tag, collision, keep old one
                            logging.debug(
                                "BAD tags collision. Same tag names: {}, {}".format(old_annot_file, new_annot_file))
                        elif ind_new_tag < ind_old_tag:
                            action = 1  # replace with new tag
                            logging.debug(
                                "Replacing old with new (tap update): {}, {}".format(old_annot_file, new_annot_file))
                        else:
                            action = 0  # do nothing if worse tag
                            logging.debug(
                                "Keeping old one tag (superior old tag): {}, {}".format(old_annot_file, new_annot_file))
                    elif new_tag is None and old_tag:  # if old one has tag, keep it
                        action = 0  # old one has tag, new dir has not
                        logging.debug("Collision (no new tag): {}, {}".format(old_annot_file, new_annot_file))
                    elif old_tag is None and new_tag:  # if new one has tag, update old one
                        action = 1  # new dir has tag, old one didn't have it
                        logging.debug("Collision (no old tag): {}, {}".format(old_annot_file, new_annot_file))

                if action:
                    dir_names[det_key] = (new_annot_file, new_tag)  # updating/creating key
                    logging.debug("Reading annotation from file (tag: {}): {}".format(new_tag, new_annot_file))
                    annot_dict = PascalVOC.from_file(file_src=det_file)
                    result_dict['ground_truth'][det_key] = annot_dict['ground_truth']
                    result_dict['gt_metadata'][det_key] = annot_dict['gt_metadata']

            except Exception as e:
                logging.warning("Annotation can't be read: {}. Msg: {}".format(det_file, str(e)))
        return result_dict

    @staticmethod
    def parse(img_dir: Any = None, annotations_dir: Any = None, lazy=False,
              allow_missing_annotation=True) -> DetectionsCollection:
        '''
        Main entry point.
        :param img_dir: Directory with images
        :param annotations_dir: Directory or list of dirs with corresponding XML files with annotations
        :return: An object with filled imgs and ground truth
        '''
        det_collection = DetectionsCollection()
        if annotations_dir:
            annotations_parsed = PascalVOC.from_dir(annotations_dir)
            logging.info("PascalVOC: {} annotations found".format(len(annotations_parsed['ground_truth'])))
            # we create/update DetectionsCollection using our predictions
            det_collection.process_ground_truth(annotations_parsed['ground_truth'],
                                                update_only=False)
            det_collection.process_field('gt_metadata', annotations_parsed['gt_metadata'], update_only=True)
        else:
            logging.warning("No ground truth is provided for PascalVoc import")

        if img_dir:
            imgs = syncv_utils_image.imgs_read_from_dir(img_dir=img_dir, lazy=lazy)
            logging.info("PascalVOC: {} images found.. Processing".format(len(imgs)))
            det_collection.process_images(imgs, update_only=not allow_missing_annotation)
            logging.info("PascalVOC: processing images done".format(len(imgs)))
        else:
            logging.warning("Images are not provided for PascalVOC import")

        return det_collection


class MSCOCO:
    pass


if __name__ == '__main__':
    from syncvtools.utils.data_export import TFRecordsExport

    tfrec_obj = TFRecords.parse(
        tfrecord_src='/Users/apatsekin/projects/datasets/synapse/20190717_sdmv_ammo_gunparts_kix/val.record')
    tfrec_new = DetectionsCollection()
    c = 0
    for img_key in tfrec_obj:
        if not tfrec_obj[img_key].ground_truth:
            continue
        tfrec_new[img_key] = tfrec_obj[img_key]
        c += 1
        if c == 100:
            break

    TFRecordsExport.export(src=tfrec_new,
                           out_path='/Users/apatsekin/projects/datasets/synapse/20190717_sdmv_ammo_gunparts_kix/val100.record')
