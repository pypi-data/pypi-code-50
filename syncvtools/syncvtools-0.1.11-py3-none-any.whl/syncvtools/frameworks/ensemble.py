from ensemble_boxes import weighted_boxes_fusion
from syncvtools.data.detections import DetectionEntity
from syncvtools.data.bbox import denormalize_bbox
from syncvtools.utils import file_tools as ft
import numpy as np
from syncvtools.utils.bbox import box_fusion
from collections import defaultdict

from syncvtools.utils.draw_detections import DrawDetections, imshow


class InferenceEnsemble:
    def __init__(self, models_list, config=None, label_map=None):
        self.config = {'iou_thr': 0.1,
                       'skip_box_thr': 0.1,
                       'sigma': 0.1}
        if label_map:
            label_map = ft.cache_file(label_map)
            self.label_map = ft.pbmap_read_to_dict(label_map)

        if config:
            self.config = {**self.config, **config}
        # rewrite to threading
        self.models_list = models_list

    def detect_image(self, input_image):
        boxes_list = [[]] * len(self.models_list)
        # scores_list = [[]] * len(self.models_list)
        # labels_list = [[]] * len(self.models_list)
        if len(self.models_list) == 1:
            weights = None
        else:
            weights = [1] * len(self.models_list)
        for model_i, model in enumerate(self.models_list):
            dets = model.detect_image(input_image=input_image)
            for det in dets:
                boxes_list[model_i].append([det.label_id, det.score] + det.bbox.bbox_norm)
                # boxes_list[model_i].append(det.bbox.bbox_norm)
                # scores_list[model_i].append(det.score)
                # labels_list[model_i].append(det.label_id)
        # boxes, scores, labels = weighted_boxes_fusion(boxes_list,
        #                                               scores_list,
        #                                               labels_list,
        #                                               weights=weights,
        #                                               iou_thr=self.config['iou_thr'],
        #                                               skip_box_thr=self.config['skip_box_thr'])
        #boxes, scores, labels = box_fusion(boxes_list)
        merged_boxes_list = box_fusion(boxes_list)
        fused_dets = []
        for i in range(len(merged_boxes_list)):
            det = DetectionEntity(label_id=merged_boxes_list[i][0],
                                  label_text=self.label_map[merged_boxes_list[i][0]],
                                  score=merged_boxes_list[i][1],
                                  bbox_norm=merged_boxes_list[i][2:],
                                  img_size=(input_image.shape[1], input_image.shape[0])
                                  )
            fused_dets.append(det)

        return fused_dets





if __name__ == "__main__":

    dt_bboxes = [[(1, 0.6228677034378052, 0.8724392, 0.19467315, 0.9435892, 0.8424522),
                  (1, 0.18780216574668884,  0.21521226, 0.073410034, 0.56916577, 0.64480345),
                  (2, 0.31595955491065979, 0.34837043, 0.87477937, 0.42925015, 0.94358507),
                  (1, 0.09868103265762329, 0.68012455, 0.07648817, 0.85396917, 0.1383612)],
                 [(1, 0.4228677034378052, 0.8024392, 0.19167315, 0.9235892, 0.8024522),
                  (1, 0.3780216574668884, 0.21021226, 0.072410034, 0.56816577, 0.64180345),
                  (2, 0.11595955491065979, 0.34137043, 0.81477937, 0.42925015, 0.94358507)
                  ]]
    # dt_classes = [[1, 1, 2, 1],
    #               [1, 1, 2]]
    # dt_scores = [
    #     [0.6228677034378052, 0.18780216574668884,  0.31595955491065979, 0.09868103265762329],
    #     [0.4228677034378052, 0.3780216574668884,  0.11595955491065979]]


    boxes = box_fusion(dt_bboxes)


    draw = DrawDetections(threshold=0.0)
    img_np = np.zeros((500,500,3),dtype=np.uint8)
    for box in boxes:
        img_np = draw.draw_one(img_np=img_np,bbox=denormalize_bbox(box[2:],(img_np.shape[1],img_np.shape[0])),
                               label_txt = "Class #{}".format(box[0]), score=box[1])

    imshow(img_np, waittime=0)

