'''
TensorFlow Inference. Right now supports Object Detection API models only.
'''
from typing import Dict, List, Tuple, Any, Union
import numpy as np, cv2
from syncvtools.utils.image import img_rot90, img_flip, img_rotate
from syncvtools.utils._dependencies import dep
from syncvtools.data import detections as det_mod
from syncvtools.utils import file_tools as ft
from syncvtools.utils.draw_detections import DrawDetections, imshow
from syncvtools.utils.bbox import restore_boxes, denormalize_bbox, nms
from syncvtools.utils.center_point import backward_rotation_bbox_tf
from syncvtools.frameworks.tf_classifier import TFInferenceClassifier
from syncvtools import config
import logging
import operator

tf = dep('tf')


def encode_image(input_image: np.ndarray) -> np.ndarray:
    '''
    preprocessing script according to ObjectDetection API
    :param input_image: RGB image, preferably in uint8
    :return: np array which has binary of encoded PNG image
    '''
    # the input should be BGR
    input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)
    ret, img_buf = cv2.imencode('.png', input_image)
    if not ret:
        raise ValueError("Input image cannot be encoded")
    images_encoded = np.array([img_buf.tostring()])
    # images_encoded = img_buf.tostring()
    return images_encoded


class TensorflowInference:
    def __init__(self,
                 graph_src: str = None,
                 checkpoint_path: str = None,
                 label_map: str = None,
                 classifier_pb: str = None,
                 classifier_label_map: str = None,
                 classifier_threshold: float = None,
                 classifier_weight: float = None,
                 ):
        '''
        Main TF inference class
        :param graph_src: path to PB graph (Frozen_inference_graph). Supports local path or AWS S3
        :param checkpoint_path: path training checkpoint saved. Supports only local path since multiple files required
        :param label_map: path to label_map dict (TF format) for provided detection model. Supports local path or AWS S3
        :param classifier_pb: path to classifier PB. Local path or AWS s3. Should be PB with -1..1 float32 input
        :param classifier_label_map: path to label_map dict (TF format) for provided classifier model. Supports local path or AWS S3
        :param classifier_threshold: boxes with conf > threshold are send to classifier
        :param classifier_weight: while averaging detection and classifier predictions, this will be weight of classifier
        '''
        self.graph_data = {}

        # inference tensors and session
        self.input_tensor = None
        self.session = None
        self.output_tensors = None
        self.graph_loaded = False

        if graph_src:
            graph_src = ft.cache_file(graph_src)
            self._initialize_inference_graph(graph_src=graph_src)
            self.graph_loaded = True
        elif checkpoint_path:
            self._initialize_from_checkpoint(checkpoint_path=checkpoint_path)
            self.graph_loaded = True

        if label_map:
            label_map = ft.cache_file(label_map)
            self.label_map = ft.pbmap_read_to_dict(label_map)
            self.r_label_map = {}
            for label_id in self.label_map:
                if self.label_map[label_id] in self.r_label_map:
                    logging.warning("Not unique label: {}".format(self.label_map[label_id]))
                    continue
                self.r_label_map[self.label_map[label_id]] = label_id
            logging.info("Label map (for inference): {}".format(self.label_map))
            logging.info("Reverse label map (for inference): {}".format(self.r_label_map))
        # init-ing classifier
        self._init_classifier(classifier_pb, classifier_label_map, classifier_threshold, classifier_weight)

    def _init_classifier(self, classifier_pb, classifier_label_map, classifier_threshold, classifier_weight):
        '''
        Method to initialize classifier model to memory. Result stored in self.classifier as dict
        :param classifier_pb: path to label_map dict (TF format) for provided classifier model. Supports local path or AWS S3
        :param classifier_label_map: path to label_map dict (TF format) for provided classifier model. Supports local path or AWS S3
        :param classifier_threshold: boxes with conf > threshold are send to classifier
        :param classifier_weight: while averaging detection and classifier predictions, this will be weight of classifier
        :return:
        '''
        self.classifier = None
        if classifier_pb is not None:
            assert classifier_threshold is not None and classifier_weight is not None and \
                   classifier_label_map is not None
            assert classifier_threshold <= 1.0 and classifier_threshold >= 0.0  # epsilon?
            assert classifier_weight <= 1.0 and classifier_weight >= 0.0
            clsfr = TFInferenceClassifier(graph_src=classifier_pb,
                                          label_map=classifier_label_map)
            self.classifier = {'classifier': clsfr,
                               'classifier_weight': classifier_weight,
                               'classifier_threshold': classifier_threshold
                               }

    def _initialize_inference_graph(self, graph_src: str,
                                    read_func=lambda x: tf.gfile.GFile(x, 'rb').read(),
                                    input_tensor_name: str = 'encoded_image_string_tensor:0',
                                    output_tensor_names: tuple = ("detection_boxes",
                                                                  "detection_scores",
                                                                  "detection_classes",
                                                                  "num_detections")
                                    ):
        '''
        Inits detection graph to memory.
        :param graph_src: path to PB graph (Frozen_inference_graph). Supports local path
        :param read_func: default tf.gfile.GFile(x, 'rb')
        :param input_tensor_name: name of input tensors in detection graph
        :param output_tensor_names: tuple with names of output tensors
        :return:
        '''
        # get a pointer to default graph
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            # make a serializable graph
            od_graph_def = tf.GraphDef()
            # graph can be written to string by any function (read_func param). Default is gfile.GFile
            serialized_graph = read_func(graph_src)
            # load from string to serializabl graph
            try:
                od_graph_def.ParseFromString(serialized_graph)
            except Exception:
                print("Graph is not frozen/readble: {}".format(graph_src))
            # import this text-graph to real default one (which is currently detection_graph)
            tf.import_graph_def(od_graph_def, name='')
            # create TF session
            self.session = tf.Session(graph=detection_graph)
            # get a pointer to input image from the graph
            try:
                self.input_tensor = detection_graph.get_tensor_by_name(input_tensor_name)
            except:
                print([n.name for n in tf.get_default_graph().as_graph_def().node])
                raise

            self.output_tensors = [detection_graph.get_tensor_by_name("%s:0" % t) for t in output_tensor_names]

    def _initialize_from_checkpoint(self, checkpoint_path,
                                    input_tensor_name='encoded_image_string_tensor:0',
                                    output_tensor_names=("detection_boxes",
                                                         "detection_scores",
                                                         "detection_classes",
                                                         "num_detections")
                                    ):
        '''
        Inits graph from checkpoint to memory
        :param checkpoint_path:path to checkpoint without .meta extension
        :param input_tensor_name: name of input tensors in detection graph
        :param output_tensor_names: tuple with names of output tensors
        :return:
        '''
        # get a pointer to default graph
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            # make a serializable graph
            saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_path))
            self.session = tf.Session(graph=detection_graph)
            saver.restore(self.session, checkpoint_path)
            self.input_tensor = detection_graph.get_tensor_by_name(input_tensor_name)
            self.output_tensors = [detection_graph.get_tensor_by_name("%s:0" % t) for t in output_tensor_names]

    def fuse_weights(self, detector_scores: Dict[str, float], classifier_scores: Dict[str, float],
                     detector_class: str) -> Dict[str, Any]:
        '''
        Fusing weights of detector and classifier.
        :param detector_scores: dictionary with {label_name: 0.35} confidences. Should contain all supported classes + threatless
        :param classifier_scores: dictionary with {label_name: 0.35} confidences. Should contain 'threatless'
        :param detector_class: class that was initially selected by detector
        :return: dictionary with set of initial and fused detections.
        '''

        missing_cls_score = 0

        for label in list(classifier_scores.keys())[:]:
            if label not in detector_scores:
                missing_cls_score += classifier_scores[label]
                del classifier_scores[label]
        if missing_cls_score > 0:
            if 'threatless' not in classifier_scores:
                raise ValueError("There are some labels in classifier that are missing in detector. \
                Also threatless class is missing in classifier. So this score is nowhere to add: {}".format(
                    missing_cls_score))
            # adding all class scores that are not in detector towards 'threatless'
            classifier_scores['threatless'] += missing_cls_score

        out_scores = {}
        for label in classifier_scores:
            # det_score = 0.0 if label not in detector_scores else detector_scores[label]
            out_scores[label] = detector_scores[label] * (1.0 - self.classifier['classifier_weight']) + \
                                classifier_scores[label] * self.classifier['classifier_weight']
        label = max(out_scores, key=out_scores.get)
        score = out_scores[label]
        out = {'fused_finalClass_score': score,
               'fused_label': label,
               'fused_intialClass_score': out_scores[detector_class],
               # if fusion changed class, this is the fused score for original class
               'classifier_finalClass_score': classifier_scores[label],
               'classifier_intialClass_score': classifier_scores[detector_class],
               # if fusion changed class, this is the detector's score for original label
               'detector_initialClass_score': detector_scores[detector_class],  # the detectors score for original class
               'detector_finalClass_score': detector_scores[label]}  # the detectors score for final class
        return out

    def classifier_fusion(self, input_image: np.ndarray, boxes: np.ndarray, scores: np.ndarray, classes: np.ndarray) -> \
    Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        '''
        Modifies original detections if classifier is set.
        :param input_image:
        :param boxes: [[[y1,x1,y2,x2],[y1,x1,y2,x2]] ] float32, 0..1. Direct output from TF model. Since output supports batch of images, we always take first index [0]
        :param scores:[[0.35, 0.215, 0.266] ]   direct output from TF model. Since output supports batch of images, we always take first index [0]
        :param classes: [[1.0 2.0 1.0 3.0] ] class index. direct output from TF model. Since output supports batch of images, we always take first index [0]
        :return:
        '''
        clsfr_src_scores = np.full((classes[0].shape[0], 2), fill_value=np.nan)
        if self.classifier is not None:
            clsfr = self.classifier['classifier']
            for i, (box, score, label_id) in enumerate(zip(boxes[0], scores[0], classes[0])):
                label_id = int(label_id)
                label_text = self.label_map[label_id] if label_id in self.label_map else None
                if label_text not in clsfr.r_label_map:
                    # classifier doesn't know this type of threat
                    continue
                detector_scores = {label_text: score, 'threatless': 1.0 - score}
                for det_label in self.r_label_map:
                    if det_label not in detector_scores:
                        detector_scores[det_label] = 0.0  # temporary patch for missing full distribution for detector
                # print(detector_scores)
                if score < self.classifier['classifier_threshold']:
                    # threshold to low to go to classifier
                    continue
                box_abs = denormalize_bbox((box[1], box[0], box[3], box[2]),
                                           img_size=(input_image.shape[1], input_image.shape[0]))
                box_crop = input_image[box_abs[1]:box_abs[3], box_abs[0]:box_abs[2]]
                clsr_scores = clsfr.detect_image_raw(input_image=box_crop)['scores_dict']
                logging.debug("[{}] Detector scores: {}".format(i, detector_scores))
                logging.debug("[{}] Classifier scores: {}".format(i, clsr_scores))

                clsr_res = self.fuse_weights(detector_scores=detector_scores,
                                             classifier_scores=clsr_scores,
                                             detector_class=label_text)

                if clsr_res[
                    'fused_label'] not in self.r_label_map:  # it's threatless
                    scores[0][i] = clsr_res['fused_intialClass_score']
                    clsfr_src_scores[i] = [
                        clsr_res['detector_initialClass_score'], clsr_res['classifier_intialClass_score']]
                else:  # detector has this class, reassigning label and score
                    scores[0][i] = clsr_res['fused_finalClass_score']
                    classes[0][i] = self.r_label_map[clsr_res['fused_label']]
                    clsfr_src_scores[i] = [
                        clsr_res['detector_finalClass_score'], clsr_res['classifier_finalClass_score']]

        return boxes, scores, classes, clsfr_src_scores

    def nms(self, boxes, scores, classes, clsfr_src_scores) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        '''
        Non max suppression per class. IoU param is set in config file of the module.
        :param boxes: [[[y1,x1,y2,x2],[y1,x1,y2,x2]] ] float32, 0..1. Direct output from TF model. Since output supports batch of images, we always take first index [0]
        :param scores:[[0.35, 0.215, 0.266] ]   direct output from TF model. Since output supports batch of images, we always take first index [0]
        :param classes: [[1.0 2.0 1.0 3.0] ] class index. direct output from TF model. Since output supports batch of images, we always take first index [0]
        :param clsfr_src_scores: classifier results also need to be resorted, so they will be returned
        :return: same as input
        '''
        classes_unique = np.unique(classes[0])
        for label_ in classes_unique:
            orig_inds = np.nonzero(classes[0] == label_)
            boxes_c = boxes[0][orig_inds]
            scores_c = scores[0][orig_inds]
            # indexes in array which contains only specific label
            nms_inds = nms(boxes_c, scores_c, thresh=config.DETECTOR_NMS_THRESHOLD, is_y1x1y2x2=True)
            # filtered original indices
            filtered_inds = np.delete(orig_inds, nms_inds)
            scores[0][filtered_inds] = 0.0

        resort_inds = np.argsort(-scores[0])
        boxes[0] = boxes[0][resort_inds]
        classes[0] = classes[0][resort_inds]
        scores[0] = scores[0][resort_inds]
        clsfr_src_scores = clsfr_src_scores[resort_inds]
        return boxes, scores, classes, clsfr_src_scores

    def detect_image_raw(self,
                         input_image: np.ndarray,
                         preprocess_func=encode_image,
                         rot90: int = None,
                         flip: int = None,
                         rotate: int = 0,
                         padding: int = 0,
                         ):
        '''
        All detections happens here. Returns dictionary with numpy arrays of TF Obj Det format.
        :param input_image: RGB image (numpy array)
        :param preprocess_func: should output an encoded BGR PNG in bytes
        :param rot90: 1,2,3 to return 90 degrees CCW.
        :param flip: 1,2,3 to flip horizontally, vertically, or both
        :param rotate: random rotation, instead of box center point of box will be returned
        :param padding: for inference white padding will be added.
        :return: dict of values. BOXES ARE IN ymin, xmin, ymax, xmax format
        '''
        if not self.graph_loaded:
            raise Exception(
                "Graph is not loaded! Run either constructor with graph_src param or initialize_inference_graph()")
        orig_size = input_image.shape[:2][::-1]
        if rotate:
            input_image = img_rotate(img_np=input_image, degree=rotate)
            rotated_size = input_image.shape[:2][::-1]

        if flip:
            input_image = img_flip(img_np=input_image, d=flip)

        if rot90:
            input_image = img_rot90(img_np=input_image, factor=rot90)

        if padding:
            input_image = cv2.copyMakeBorder(input_image, padding, padding, padding, padding,
                                             cv2.BORDER_CONSTANT, value=(255, 255, 255))

        images_encoded = preprocess_func(input_image)
        boxes, scores, classes, num = self.session.run(self.output_tensors,
                                                       feed_dict={self.input_tensor: images_encoded})

        classes = classes.astype(int)

        boxes, scores, classes, clsfr_src_scores = self.classifier_fusion(input_image, boxes, scores, classes)
        boxes, scores, classes, clsfr_src_scores = self.nms(boxes, scores, classes, clsfr_src_scores)

        if rot90 or flip or padding:
            logging.debug("Restoring boxes..")
            boxes = restore_boxes(boxes=boxes,
                                  rot90=rot90,
                                  flip=flip,
                                  org_size=orig_size,
                                  modified_img_size=input_image.shape[:2][::-1],
                                  padding=padding)

        if rotate:
            logging.debug("Restoring original center points from rotated boxes..")
            points = backward_rotation_bbox_tf(bbox_norm=boxes, angle=rotate, org_size=orig_size, rot_size=rotated_size)
            return {'points': points, 'scores': scores, 'classes': classes, 'img_inf_size': input_image.shape,
                    'clsfr_src_scores': clsfr_src_scores}

            # boxes - (batch, num, min_y, min_x, max_y, max_x)
        return {'boxes': boxes, 'scores': scores, 'classes': classes, 'img_inf_size': input_image.shape,
                'clsfr_src_scores': clsfr_src_scores}

    def detect_image(self,
                     input_image: np.ndarray,
                     preprocess_func=encode_image,
                     rot90: int = None,
                     flip: int = None,
                     rotate: int = 0,
                     padding: int = 0,
                     ) -> List[det_mod.DetectionEntity]:
        '''
        High-level inference, which returns
        :param input_image: uint8 Numpy image
        :param preprocess_func: preprocess function for detector. Default works for Obj Det API
        :param rot90: 1,2,3 to return 90 degrees CCW.
        :param flip: 1,2,3 to flip horizontally, vertically, or both
        :param rotate: random rotation, instead of box center point of box will be returned
        :param padding: for inference white padding will be added.
        :return: List of DetectionEntity which can be added to ImageLevelDetections
        '''
        detections_raw = self.detect_image_raw(input_image=input_image, preprocess_func=preprocess_func,
                                               rot90=rot90, flip=flip, rotate=rotate, padding=padding)
        detections = []

        if rotate:
            raise Exception("This is not used anymore. To avoid bugs need to be revalidated")
            # rotation part is commented since it's probably never gonna be used again
            # for i, (point, score, label_id) in enumerate(zip(detections_raw['points'][0], detections_raw['scores'][0],
            #                                                  detections_raw['classes'][0])):
            #     label_id = int(label_id)
            #     if label_id not in self.label_map: #if model supports classes, that are not in label map - ignore this detection
            #         continue
            #     label_text = self.label_map[label_id]
            #
            #     detection_obj = det_mod.DetectionEntity(label_id=label_id,
            #                                             label_text=label_text,
            #                                             point_abs=tuple(map(int, point))[:2],
            #                                             score=float(score),
            #                                             detector_score=detections_raw['clsfr_src_scores'][i][0] if
            #                                             detections_raw[
            #                                                 'clsfr_src_scores'][i][0] == np.nan else None,
            #                                             classifier_score=detections_raw['clsfr_src_scores'][i][1] if
            #                                             detections_raw[
            #                                                 'clsfr_src_scores'][i][0] == np.nan else None,
            #                                             img_size=(input_image.shape[1], input_image.shape[0]))
            #     detections.append(detection_obj)
        else:
            for i, (box, score, label_id) in enumerate(zip(detections_raw['boxes'][0], detections_raw['scores'][0],
                                                           detections_raw['classes'][0])):
                label_id = int(label_id)
                if label_id not in self.label_map:  # if model supports classes, that are not in label map - ignore this detection
                    continue
                label_text = self.label_map[label_id]
                detection_obj = det_mod.DetectionEntity(label_id=self.r_label_map[label_text],
                                                        # label_id might be not unique
                                                        label_text=label_text,
                                                        bbox_norm=(box[1], box[0], box[3], box[2]),
                                                        score=float(score),
                                                        detector_score=detections_raw['clsfr_src_scores'][i][0] if
                                                        detections_raw[
                                                            'clsfr_src_scores'][i][0] != np.nan else None,
                                                        classifier_score=detections_raw['clsfr_src_scores'][i][1] if
                                                        detections_raw[
                                                            'clsfr_src_scores'][i][0] != np.nan else None,
                                                        img_size=(input_image.shape[1], input_image.shape[0]))
                detections.append(detection_obj)
        return detections


class TensorflowInferenceRuleBased(TensorflowInference):
    '''
    Rules based inference (no fusion of weights). Based on confidence of detector an classifier box either rejected or accepted.
    '''

    def _init_classifier(self, classifier_pb, classifier_label_map, classifier_threshold, classifier_weight):
        self.classifier = None
        if classifier_pb is not None:
            clsfr = TFInferenceClassifier(graph_src=classifier_pb,
                                          label_map=classifier_label_map)
            self.classifier = {'classifier': clsfr,
                               'classifier_threshold': {'sharp': 0.2, 'handgun': 0.2},
                               'auto_accept_thresholds': {'sharp': 1.01, 'handgun': 0.5},
                               'ranges': {'sharp': [(0.0, 0.2, 0.999),
                                                    (0.2, 0.3, 0.995),
                                                    (0.3, 0.4, 0.99),
                                                    (0.4, 0.6, 0.95),
                                                    (0.6, 0.7, 0.9),
                                                    (0.7, 0.8, 0.8),
                                                    (0.8, 1.0, 0.7)
                                                    ],
                                          'handgun': [(0.0, 0.2, 0.999),
                                                      (0.2, 0.3, 0.999),
                                                      (0.3, 0.4, 0.99),
                                                      (0.4, 0.5, 0.9),
                                                      (0.5, 1.0, 0.0)],
                                          'ammo-round': [(0.0, 1.0, 0.9995)],
                                          'shotgun-shell': [(0.0, 1.0, 0.9995)],
                                          'ammo-pack': [(0.0, 1.0, 0.9995)],
                                          'cylinder': [(0.0, 1.0, 0.9995)],
                                          'receiver': [(0.0, 1.0, 0.9995)],
                                          'magazine': [(0.0, 1.0, 0.9995)],
                                          'slide': [(0.0, 1.0, 0.9995)],
                                          }
                               }

    def fuse_weights(self, detector_scores, classifier_scores, detector_class):

        out_score = None
        # what label classifier predicted
        label_to_consider = max(classifier_scores.items(), key=operator.itemgetter(1))[0]
        del detector_scores['threatless']  # not used there
        if label_to_consider == 'threatless':  # we don't take threatless as class, so we take then probability of detector_class from classifier
            label_to_consider = detector_class

        # what detector predicted for this label
        det_score = 0.0 if label_to_consider not in detector_scores else detector_scores[label_to_consider]

        is_range_found = False
        for min_, max_, cls_thresh in self.classifier['ranges'][label_to_consider]:
            if det_score >= min_ and det_score <= max_:  # to cover 0.0 and 1.0
                if classifier_scores[label_to_consider] >= cls_thresh:
                    out_score = 1.0  # immitation of "drawing this box"
                else:
                    out_score = 0.0  # immitation of not drawing this box
                is_range_found = True
                break
            else:
                continue
        if not is_range_found:
            raise ValueError("Range not found for {}".format(label_to_consider))

        # label = label_to_consider
        # score = out_score
        out = {'fused_finalClass_score': out_score,
               'fused_label': label_to_consider,  ##FIGURE OUT HERE TODO
               # 'fused_intialClass_score': detector_scores[detector_class], #we don't have fused scores for anything but main
               # if fusion changed class, this is the fused score for original class
               'classifier_finalClass_score': classifier_scores[label_to_consider],
               'classifier_intialClass_score': classifier_scores[detector_class],
               # if fusion changed class, this is the detector's score for original label
               'detector_initialClass_score': detector_scores[detector_class],  # the detectors score for original class
               'detector_finalClass_score': detector_scores[
                   label_to_consider] if label_to_consider in detector_scores else 0.0}  # the detectors score for final class
        return out

    def classifier_fusion(self, input_image, boxes, scores, classes):
        clsfr_src_scores = np.full((classes[0].shape[0], 2), fill_value=np.nan)
        if self.classifier is not None:

            clsfr = self.classifier['classifier']
            for i, (box, score, label_id) in enumerate(zip(boxes[0], scores[0], classes[0])):
                label_id = int(label_id)
                label_text = self.label_map[label_id] if label_id in self.label_map else None
                if label_text not in clsfr.r_label_map:
                    # classifier doesn't know this type of threat
                    continue
                detector_scores = {label_text: score, 'threatless': 1.0 - score}

                if score < self.classifier['classifier_threshold'][label_text]:
                    # threshold to go to classifier
                    continue
                if score > self.classifier['auto_accept_thresholds'][label_text]:
                    # in this case boxes are displayed as is, but we just leave confidence as is
                    continue

                box_abs = denormalize_bbox((box[1], box[0], box[3], box[2]),
                                           img_size=(input_image.shape[1], input_image.shape[0]))
                box_crop = input_image[box_abs[1]:box_abs[3], box_abs[0]:box_abs[2]]
                clsr_scores = clsfr.detect_image_raw(input_image=box_crop)['scores_dict']

                clsr_res = self.fuse_weights(detector_scores=detector_scores,
                                             classifier_scores=clsr_scores,
                                             detector_class=label_text)

                if clsr_res[
                    'fused_label'] not in self.r_label_map:  # it's threatless or class not in detector label_map
                    scores[0][i] = 0.0
                    clsfr_src_scores[i] = [
                        0.0, clsr_res['classifier_intialClass_score']]
                else:  # detector has this class, reassigning label and score
                    scores[0][i] = clsr_res['fused_finalClass_score']
                    classes[0][i] = self.r_label_map[clsr_res['fused_label']]
                    clsfr_src_scores[i] = [
                        clsr_res['detector_finalClass_score'], clsr_res['classifier_finalClass_score']]
        return boxes, scores, classes, clsfr_src_scores


if __name__ == '__main__':
    from syncvtools.utils.data_export import ProdDetectionsExport
    from syncvtools.utils.data_import import TFRecords
    from tqdm import tqdm
    import os


