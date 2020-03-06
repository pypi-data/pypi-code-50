'''
TF  Classifier Inference class.
'''
import numpy as np, cv2
from typing import Tuple, List, Dict, Any
from syncvtools.utils._dependencies import dep
from syncvtools.utils import file_tools as ft
from syncvtools.utils.draw_detections import DrawDetections, imshow
import logging

tf = dep('tf')


def default_preprocess_func(img_np: np.ndarray, target_shape: Tuple) -> np.ndarray:
    '''
    Rotate to put it horizontally. Resize and pad to specific size (constant aspect ratio)
    :param img_np: Image in numpy uint8, RGB.
    :param target_shape: (h,w,channels). Channels is optional.
    :return: processed image in Numpy
    '''
    if img_np.shape[0] > img_np.shape[1]:  # should be w >= h
        img_np = np.rot90(m=img_np, k=1)
    h_ratio = target_shape[0] / img_np.shape[0]
    w_ratio = target_shape[1] / img_np.shape[1]
    scale = h_ratio if w_ratio > h_ratio else w_ratio
    img_np = cv2.resize(src=img_np, dsize=(0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    t_p = (target_shape[0] - img_np.shape[0]) // 2
    b_p = target_shape[0] - img_np.shape[0] - t_p
    l_p = (target_shape[1] - img_np.shape[1]) // 2
    r_p = target_shape[1] - img_np.shape[1] - l_p
    img_np = cv2.copyMakeBorder(src=img_np, top=t_p, bottom=b_p, left=l_p, right=r_p, borderType=cv2.BORDER_CONSTANT,
                                value=(127, 127, 127))
    img_np = (np.array([img_np]) / 127.5) - 1.0
    return img_np


class TFInferenceClassifier:
    def __init__(self,
                 graph_src,
                 label_map: str = None,
                 input_shape=(200, 500, 3)
                 ):
        '''
        TF Classifier inference
        :param graph_src: path to PB graph (Frozen_inference_graph). Supports local path or AWS S3
        :param label_map: path to label_map dict (TF format) for model. Supports local path or AWS S3
        :param input_shape: (h,w,channels) to resize inputs
        '''
        self.graph_data = {}

        # inference tensors and session
        self.input_shape = input_shape
        self.input_tensor = None
        self.session = None
        self.output_tensors = None

        graph_src = ft.cache_file(graph_src)
        self._initialize_inference_graph(graph_src=graph_src)

        if label_map:
            label_map = ft.cache_file(label_map)
            self.label_map = ft.pbmap_read_to_dict(label_map)
            self.r_label_map = {v: k for k, v in self.label_map.items()}
            logging.info("Classifier label_map: {}".format(self.label_map))
            logging.info("Classifier reverse label_map: {}".format(self.r_label_map))

    def _initialize_inference_graph(self, graph_src: str,
                                    read_func=lambda x: tf.gfile.GFile(x, 'rb').read(),
                                    input_tensor_name: str = 'import/input_1:0',
                                    output_tensor_name: str = 'import/dense_1/Softmax:0'
                                    ):
        '''
         Method to initialize classifier model to memory.
        :param graph_src:path to label_map dict (TF format) for provided classifier model. Supports local path
        :param read_func: default should be fine; GFile reader.
        :param input_tensor_name: name of input tensor
        :param output_tensor_name: name of output tensor
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
            tf.import_graph_def(od_graph_def)
            # create TF session
            self.session = tf.Session(graph=detection_graph)
            # get a pointer to input image from the graph
            self.input_tensor = detection_graph.get_tensor_by_name(input_tensor_name)
            self.output_tensor = detection_graph.get_tensor_by_name(output_tensor_name)

    def display_preprocessed(self, img_np: np.ndarray):
        '''
        Debug tool to show preprocessed image with numpy
        :param img_np:
        :return:
        '''
        img = ((img_np[0] + 1.0) * 127.5).astype(np.uint8)
        imshow(img)

    def detect_image_raw(self,
                         input_image: np.ndarray,
                         preprocess_func=default_preprocess_func,
                         ) -> Dict[str, Any]:
        '''
        Detects image and returns dictionary with raw scores
        :param input_image: Numpy RGB uint8 image.
        :param preprocess_func: default should be fine. Don't forget that current model expectes vertical images to be
        on the side CCW [^] -> [< ].
        :return: dict with raw_scores - just as is from model, scores_dict - dict which match label names to scores.
        '''

        images_encoded = preprocess_func(input_image, target_shape=self.input_shape)
        # self.display_preprocessed(img_np=images_encoded)
        raw_scores = self.session.run(self.output_tensor,
                                      feed_dict={self.input_tensor: images_encoded})
        raw_scores = raw_scores[0]
        scores_dict = {v: raw_scores[k] for (k, v) in self.label_map.items()}
        return {'raw_scores': raw_scores,
                'scores_dict': scores_dict}
