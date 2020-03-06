'''
Inference class for SimpleDet (which is yet another framework for single NN: TridentNet)
It adds some custom layers to MXNet (apache), so to run this inference, you need to pip install provided
wheel package to docker container. Package can be found in github simpledet repo.
'''
import numpy as np, cv2, os

from syncvtools.data import detections as det_mod
from syncvtools.utils.draw_detections import DrawDetections
import syncvtools.utils.file_tools as ft
from mxnet import symbol as symbol
from mxnet import ndarray as nd
import mxnet as mx
from syncvtools.frameworks.simpledet_libs.operator_py.cython.cpu_nms import soft_nms
from syncvtools.frameworks.simpledet_libs.detection_module import DetModule
import logging


class SimpledetInference():
    @staticmethod
    def _cython_soft_nms_wrapper(thresh, sigma=0.5, score_thresh=0.001, method='linear'):
        methods = {'hard': 0, 'linear': 1, 'gaussian': 2}
        assert method in methods, 'Unknown soft_nms method: {}'.format(method)

        def _nms(dets):
            dets, _ = soft_nms(
                np.ascontiguousarray(dets, dtype=np.float32),
                np.float32(sigma),
                np.float32(thresh),
                np.float32(score_thresh),
                np.uint8(methods[method]))
            return dets

        return _nms

    def _do_nms(self,rec):
        bbox_xyxy = rec["bbox_xyxy"]
        cls_score = rec["cls_score"]
        final_dets = {}

        for cid in range(cls_score.shape[1]):
            score = cls_score[:, cid]
            if bbox_xyxy.shape[1] != 4:
                cls_box = bbox_xyxy[:, cid * 4:(cid + 1) * 4]
            else:
                cls_box = bbox_xyxy
            valid_inds = np.where(score > 0.001)[0]
            box = cls_box[valid_inds]
            score = score[valid_inds]
            det = np.concatenate((box, score.reshape(-1, 1)), axis=1).astype(np.float32)
            det = self.nms(det)
            final_dets[cid] = det
        rec["det_xyxys"] = final_dets
        del rec["bbox_xyxy"]
        del rec["cls_score"]
        return rec


    def __init__(self,
                 model_file: str,
                 params_file: str,
                 labels_file: str,
                 cfg_file: str):
        os.environ["MXNET_CUDNN_AUTOTUNE_DEFAULT"] = "0"
        os.environ["MXNET_CUDA_LIB_CHECKING"] = "0"

        params_file = ft.cache_file(params_file)
        model_file = ft.cache_file(model_file)
        cfg_file = ft.cache_file(cfg_file)
        labels_file = ft.cache_file(labels_file)
        cfg = ft.json_read_to_object(cfg_file)
        self.input_dimensions = cfg['input_dimensions']
        self.label_map = ft.pbmap_read_to_dict(input_file=labels_file)

        sym = symbol.load(model_file)
        save_dict = nd.load(params_file)
        arg_params = {}
        aux_params = {}
        if not save_dict:
            raise ValueError("Params file {} is empty".format(params_file))
        for k, v in save_dict.items():
            tp, name = k.split(":", 1)
            if tp == "arg":
                arg_params[name] = v
            if tp == "aux":
                aux_params[name] = v

        #sym, arg_params, aux_params = mx.model.load_checkpoint(model_prefix, epoch)

        self.data_names = ["data", "im_info", "im_id", "rec_id"]
        data_shape = [(1, 3, self.input_dimensions[1], self.input_dimensions[0]), (1, 3), (1,), (1,)]
        data_shape = [(name, shape) for name, shape in zip(self.data_names, data_shape)]
        ctx = mx.gpu(0)
        mod = DetModule(sym, data_names=self.data_names, context=ctx)
        mod.bind(data_shapes=data_shape, for_training=False)
        mod.set_params(arg_params, aux_params, allow_extra=False)
        self.mod = mod
        self.nms = SimpledetInference._cython_soft_nms_wrapper(0.5)


    def _transform(self, input_record, input_dimensions):
        #reading file from disk
        # image = cv2.imread(input_record["image_url"], cv2.IMREAD_COLOR)
        # if not os.path.exists(input_record["image_url"]):
        #     raise Exception("Path doesn't exist: {}".format(input_record["image_url"]))
        input_record["image"] = input_record["image"].astype("float32")
        #this one stores image size and scale
        if 'im_info' not in input_record:
            input_record["im_info"] = np.array([input_record["image"].shape[0], input_record["image"].shape[1], 1.0], dtype=np.float32)

        #resiging
        image = input_record["image"]
        logging.debug("Resize input: {}".format(image.shape))
        h, w = image.shape[:2]
        scale = min(input_dimensions[1] / h, input_dimensions[0] / w)
        input_record["image"] = cv2.resize(image, None, None, scale, scale,
                                           interpolation=cv2.INTER_LINEAR)
        input_record["im_info"] = np.array([round(h * scale), round(w * scale), scale], dtype=np.float32)
        logging.debug("Resize output: {}".format(input_record["image"].shape))

        #padding
        image = input_record["image"]
        logging.debug("Padding input: {}".format(image.shape))
        h, w = image.shape[:2]
        shape = (input_dimensions[1], input_dimensions[0], 3)
        padded_image = np.full(shape, 255, dtype=np.float32)
        padded_image[:h, :w] = image #TODO: center it
        logging.debug("Padding output: {}".format(padded_image.shape))
        input_record["image"] = padded_image
        input_record["im_info"] = np.array([input_dimensions[1], input_dimensions[0], input_record["im_info"][2]], dtype=np.float32)

        #channels first
        input_record["image"] = input_record["image"].transpose((2, 0, 1))

        #general procedure in Simpledet framework. Doesn't make a lot of sence here, but still.
        input_record["data"] = input_record["image"]
        del input_record["image"]
        return input_record

    def detect_image_raw(self, input_image, preprocess_func=None):
        rec = self._infer_img_file(img_rgb_np=input_image)
        dets = rec["det_xyxys"]
        boxes, scores, classes = [],[],[]
        for cid in dets:
            det = dets[cid]
            if det.shape[0] == 0:
                continue
            sc = det[:, -1]
            for i in range(sc.shape[0]):
                x1,y1,x2,y2 = list(map(int,map(round,det[i])))[:4]
                boxes.append([x1,y1,x2,y2])
                scores.append(sc[i])
                classes.append(cid)
        return {'boxes': boxes, 'scores': scores, 'classes': classes}


    def detect_image(self, input_image, preprocess_func = None):
        detections_raw = self.detect_image_raw(input_image=input_image, preprocess_func = preprocess_func)
        detections = []
        for box, score, label_id in zip(detections_raw['boxes'],detections_raw['scores'],detections_raw['classes']):
            label_id = int(label_id)
            label_text = self.label_map[label_id] if label_id in self.label_map else None
            detection_obj = det_mod.DetectionEntity(label_id=label_id,
                                                    label_text=label_text,
                                                    bbox_abs=box,
                                                    score=float(score),
                                                    img_size=(input_image.shape[1],input_image.shape[0]))
            detections.append(detection_obj)
        return detections

    def _infer_img_file(self, img_rgb_np):

        im_id = 1
        rec_id = 1
        input_record = {"image":img_rgb_np, "im_id":im_id, "rec_id":rec_id}
        self._transform(input_record, input_dimensions=self.input_dimensions)
        logging.debug("image tranform done")

        for name in self.data_names:
            input_record[name] = np.ascontiguousarray(np.stack([input_record[name]]))

        data = [mx.nd.from_numpy(input_record[name], zero_copy=True).astype('float32') for name in self.data_names]

        data_batch = mx.io.DataBatch(data=data)

        self.mod.forward(data_batch, is_train=False)
        out = [x.asnumpy() for x in self.mod.get_outputs()]

        rid, id, info, cls, box = out
        rid, id, info, cls, box = rid.squeeze(), id.squeeze(), info.squeeze(), cls.squeeze(), box.squeeze()
        # TODO: POTENTIAL BUG, id or rid overflows float32(int23, 16.7M)
        id = np.asscalar(id)
        rid = np.asscalar(rid)

        scale = info[2]  # h_raw, w_raw, scale
        box = box / scale  # scale to original image scale
        cls = cls[:, 1:]   # remove background
        # TODO: the output shape of class_agnostic box is [n, 4], while class_aware box is [n, 4 * (1 + class)]
        box = box[:, 4:] if box.shape[1] != 4 else box

        rec = dict(
            rec_id=rid,
            im_id=id,
            im_info=info,
            bbox_xyxy=box,  # ndarray (n, class * 4) or (n, 4)
            cls_score=cls   # ndarray (n, class)
        )
        rec = self._do_nms(rec)
        #print(rec)
        return rec



if __name__ == '__main__':
    from syncvtools.utils.data_export import ProdDetectionsExport
    from syncvtools.utils.data_import import TFRecords
    from tqdm import tqdm
    import os
    if os.path.exists('/Users/apatsekin/projects'):
        path_to_projects = '/Users/apatsekin/projects'
    elif os.path.exists('/home/apatsekin/projects'):
        path_to_projects = '/home/apatsekin/projects'
    else:
        raise Exception("Path to projects not found")
    print("Project dir: {}".format(path_to_projects))
    #file_src = '/Users/apatsekin/Downloads/ammo_scans/SP-200H-231_20190920_00000547_top.png'
    inf = SimpledetInference(model_file='s3://perception-models/tridentnet/2019-11-17_unknown_hs/checkpoint_infer-symbol.json',
                             params_file='s3://perception-models/tridentnet/2019-11-17_unknown_hs/checkpoint_infer-0015.params',
                             labels_file='s3://perception-models/tridentnet/2019-11-17_unknown_hs/sharp_handgun_label_map.pbtxt',
                             cfg_file='s3://perception-models/tridentnet/2019-11-17_unknown_hs/config.json'
                             )
    drawer = DrawDetections(bbox_line_height=2, threshold=0.1)
    print("parsing tf record")
    tfrec_obj = TFRecords.parse(tfrecord_src=os.path.join(path_to_projects,'datasets/synapse/20190717_sdmv_ammo_gunparts_kix/val100.record'))
    print("inference started")
    for img_key in tqdm(tfrec_obj):
        img_obj = tfrec_obj[img_key]
        dets = inf.detect_image(input_image=img_obj.img.img_np)
        img_obj.detections = dets
        pred_json = os.path.join(path_to_projects,"datasets/synapse/20190717_sdmv_ammo_gunparts_kix/val100_detections/{}.json".format(img_key))

        ProdDetectionsExport.convert_one_save(path_src=pred_json, img_det=img_obj)
        # img_bbox = drawer.draw_imageleveldetections(img_dets=img_obj)
        # cv2.imshow('test', img_bbox)
        # cv2.waitKey(0)


