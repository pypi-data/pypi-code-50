from typing import Tuple, Any, Union, List
from syncvtools.data.image import ImgSize
import numpy as np


def normalize_bbox(bbox: Tuple[int, int, int, int], img_size: Tuple[int, int]) -> Tuple[float, float, float, float]:
    '''
    Takes x1,y1,x2,y2 in int and converts it into float32 0..1
    :param bbox: x1,y1,x2,y2 in int
    :param img_size: (w,h) in int
    :return: Normalized x1,y1,x2,y2 in float32 in range 0..1
    '''
    if bbox is None or len(bbox) < 4 or len(bbox) > 5:
        raise ValueError("Bbox is either None or not a tuple of size 4,5: (xmin, ymin, xmax, ymax)")

    img_size = ImgSize(width=img_size[0], height=img_size[1])
    norm_coords = (float(bbox[0] / img_size.width), float(bbox[1] / img_size.height), float(bbox[2] / img_size.width),
                   float(bbox[3] / img_size.height))
    for coord in norm_coords:
        if coord < 0 or coord > 1:
            raise ValueError("Norm coordinates should be [0;1]: {}".format(bbox[:4]))
    return norm_coords


def denormalize_bbox(bbox: Tuple[float, float, float, float], img_size: Tuple[int, int]) -> Tuple[int, int, int, int]:
    '''
    Takes x1,y1,x2,y2 in float32 0..1 and converts it into int
    :param bbox: x1,y1,x2,y2 in float32 0..1 rnage
    :param img_size: (w,h) in int
    :return: Normalized x1,y1,x2,y2 in int
    '''

    def cl(v, mn, mx):
        return max(min(v, mx), mn)

    # just to validate width/height
    img_size = ImgSize(width=img_size[0], height=img_size[1])
    bbox = validate_norm_coords(bbox=bbox)
    abs_coords = bbox[0] * img_size.width, bbox[1] * img_size.height, bbox[2] * img_size.width, bbox[
        3] * img_size.height
    abs_coords = list(map(int, map(round, abs_coords)))
    abs_coords = (cl(abs_coords[0], 0, img_size.width - 1),
                  cl(abs_coords[1], 0, img_size.height - 1),
                  cl(abs_coords[2], 0, img_size.width - 1),
                  cl(abs_coords[3], 0, img_size.height - 1))
    return abs_coords


def validate_norm_coords(bbox: Tuple[float, float, float, float]):
    '''
    Validates that normalized coordinates are in 0..1 range.
    Some small epsilon is allowed and fixed to sharp 0/1.
    :param bbox:
    :return:
    '''
    if bbox is None or len(bbox) != 4:
        raise ValueError("Bbox should take a tuple of float (x1,y1,x2,y2)")
    for coord in bbox[:4]:
        if coord < (0 - 1e-4) or coord > (1 + 1e-4):
            raise ValueError("Norm coordinates should be [0;1]: {}".format(bbox[:4]))
    return (max(0, bbox[0]), min(1, bbox[1]), max(0, bbox[2]), min(1, bbox[3]))


def abs_x1y1x2y2_to_abs_x1y1wh(box_coords) -> Union[list, tuple, np.ndarray]:
    '''
    converting from Synapse to MSCOCO box coordinates
    :param box_coords: x1,y1,x2,y2 abs list/tuple or np.array of shape (N,4)
    :return: abs x1,y1,w,h tuple or np.array of shape (N,4)
    '''
    if not isinstance(box_coords, np.ndarray):
        assert len(box_coords) == 4
        x1, y1, x2, y2 = box_coords[:4]
        w = x2 - x1
        h = y2 - y1
        if w <= 0 or h <= 0:
            raise ValueError("Bounding box is not correct: {}".format(box_coords))
        return (x1, y1, w, h)
    else:
        box_coords[:, 2] = box_coords[:, 2] - box_coords[:, 0]
        box_coords[:, 3] = box_coords[:, 3] - box_coords[:, 1]
        return box_coords


def abs_x1y1wh_to_abs_x1y1x2y2(box_coords) -> Union[list, tuple, np.ndarray]:
    '''
    converting from MSCOCO to Synapse
    :param box_coords: x1,y1,x2,y2 abs list/tuple or np.array of shape (N,4)
    :return: abs x1,y1,w,h tuple or np.array of shape (N,4)
    '''
    if not isinstance(box_coords, np.ndarray):
        assert len(box_coords) == 4
        x1, y1, w, h = box_coords[:4]
        x2 = x1 + w
        y2 = y1 + h
        return (x1, y1, x2, y2)
    else:
        box_coords[:, 2] = box_coords[:, 2] + box_coords[:, 0]
        box_coords[:, 3] = box_coords[:, 3] + box_coords[:, 1]
        return box_coords


def nms(dets: np.ndarray, scores: np.ndarray, thresh: float, is_y1x1y2x2: bool = False) -> List:
    '''
    Non max suppression. For convenience it can take directly TF Obj Det Api order of coordinates
    :param dets: Shape: [num_of_det, 4]. Coords are x1,y1,x2,y2 or y1,x1,y2,x2 if is_y1x1y2x2 is set.
    :param scores: np list of preds confidences
    :param thresh: what IoU to use
    :param is_y1x1y2x2: True to set TF OBj Det API format for input
    :return:
    '''
    if is_y1x1y2x2:
        x1 = dets[:, 1]
        y1 = dets[:, 0]
        x2 = dets[:, 3]
        y2 = dets[:, 2]
    else:
        x1 = dets[:, 0]
        y1 = dets[:, 1]
        x2 = dets[:, 2]
        y2 = dets[:, 3]

    areas = (x2 - x1) * (y2 - y1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1)
        h = np.maximum(0.0, yy2 - yy1)
        inter = w * h
        try:
            ovr = inter / (areas[i] + areas[order[1:]] - inter)
        except:
            ovr = 0.0

        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]
    return keep


def bbox_vflip(bbox):
    """Flip a bounding box vertically around the x-axis. From albumentations.
    Args:
        #bbox (tuple): A bounding box `(x_min, y_min, x_max, y_max)`.
        rows (int): Image rows.
        cols (int): Image cols.
    Returns:
    """
    bbox_result = np.copy(bbox)
    bbox_result[:, :, 0] = 1 - bbox[:, :, 2]  # 1- y_max
    bbox_result[:, :, 2] = 1 - bbox[:, :, 0]  # 1- y_min

    # x_min, y_min, x_max, y_max = bbox[:4]
    return bbox_result


def bbox_hflip(bbox):
    """Flip a bounding box horizontally around the y-axis. From albumentations.
    Args:
        #bbox (tuple): A bounding boxes `(x_min, y_min, x_max, y_max)`.
        bbox: (batch,num, y1,x1,y2,x2)
    Returns:
        #tuple: A bounding box `(x_min, y_min, x_max, y_max)`.
    """
    bbox_result = np.copy(bbox)
    bbox_result[:, :, 1] = 1 - bbox[:, :, 3]  # 1- x_max
    bbox_result[:, :, 3] = 1 - bbox[:, :, 1]  # 1- x_min
    # x_min, y_min, x_max, y_max = bbox[:4]
    return bbox_result  # 1 - x_max, y_min, 1 - x_min, y_max


def bbox_abs_vflip(bbox, img_size):
    """Flip a bounding box vertically around the x-axis. From albumentations.
    Args:
        bbox (tuple): A bounding box `(x_min, y_min, x_max, y_max)`.
        rows (int): Image rows.
        cols (int): Image cols.
    Returns:
        tuple: A bounding box `(x_min, y_min, x_max, y_max)`.
    """
    w, h = img_size[:2]
    x_min, y_min, x_max, y_max = bbox[:4]
    return x_min, h - y_max, x_max, h - y_min


def bbox_abs_hflip(bbox, img_size):
    """Flip a bounding box horizontally around the y-axis. From albumentations.
    Args:
        bbox (tuple): A bounding box `(x_min, y_min, x_max, y_max)`.
    Returns:
        tuple: A bounding box `(x_min, y_min, x_max, y_max)`.
    """
    w, h = img_size[:2]
    x_min, y_min, x_max, y_max = bbox[:4]
    return w - x_max, y_min, w - x_min, y_max


def bbox_flip(bbox, d):
    """Flip a bounding box either vertically, horizontally or both depending on the value of `d`. From albumentations.
    Args:
        #bbox (tuple): A bounding box `(x_min, y_min, x_max, y_max)`.
        bbox (batch,num, y1,x1,y2,x2)
        d (int):
        rows (int): Image rows.
        cols (int): Image cols.
    Returns:
        #tuple: A bounding box `(x_min, y_min, x_max, y_max)`.
    Raises:
        ValueError: if value of `d` is not 1,2,3
    """
    if d == 2:
        bbox = bbox_vflip(bbox)
    elif d == 1:
        bbox = bbox_hflip(bbox)
    elif d == 3:
        bbox = bbox_hflip(bbox)
        bbox = bbox_vflip(bbox)
    else:
        raise ValueError("Invalid d value {}. Valid values are 1,2,3".format(d))
    return bbox


def bbox_abs_flip(bbox, d, img_size):
    """Flip a bounding box either vertically, horizontally or both depending on the value of `d`. From albumentations.
    Args:
        bbox (tuple): A bounding box `(x_min, y_min, x_max, y_max)`.
        d (int):
        rows (int): Image rows.
        cols (int): Image cols.
    Returns:
        tuple: A bounding box `(x_min, y_min, x_max, y_max)`.
    Raises:
        ValueError: if value of `d` is not 1,2,3
    """
    if d == 2:
        bbox = bbox_abs_vflip(bbox, img_size)
    elif d == 1:
        bbox = bbox_abs_hflip(bbox, img_size)
    elif d == 3:
        bbox = bbox_abs_hflip(bbox, img_size)
        bbox = bbox_abs_vflip(bbox, img_size)
    else:
        raise ValueError("Invalid d value {}. Valid values are 1,2,3".format(d))
    return bbox


def bbox_abs_rot90(bbox, factor, img_size):
    """Rotates a bounding box by 90 degrees CCW (see np.rot90). From albumentations.
    Args:
        bbox (tuple): A bounding box (int) tuple (x_min, y_min, x_max, y_max).
        factor (int): Number of CCW rotations. Must be in set {0, 1, 2, 3} See np.rot90.
        img_size: w,h
    Returns:
        tuple: A bounding box tuple (x_min, y_min, x_max, y_max).
    """
    w, h = img_size[:2]
    if factor not in {0, 1, 2, 3}:
        raise ValueError("Parameter n must be in set {0, 1, 2, 3}")
    x_min, y_min, x_max, y_max = bbox[:4]
    if factor == 1:
        bbox = y_min, w - x_max, y_max, w - x_min
    elif factor == 2:
        bbox = w - x_max, h - y_max, w - x_min, h - y_min
    elif factor == 3:
        bbox = h - y_max, x_min, h - y_min, x_max
    return bbox


def bbox_rot90(boxes, factor):
    """Rotates a bounding box by 90 degrees CCW (see np.rot90). From albumentations.
    Args:
        boxes: (batch,num, y1,x1,y2,x2)
        factor (int): Number of CCW rotations. Must be in set {0, 1, 2, 3} See np.rot90.
        rows (int): Image rows.
        cols (int): Image cols.
    Returns:
        tuple: A bounding box tuple (x_min, y_min, x_max, y_max).
    """

    if factor not in {0, 1, 2, 3}:
        raise ValueError("Parameter n must be in set {0, 1, 2, 3}")

    boxes_res = np.copy(boxes)
    # x_min, y_min, x_max, y_max = boxes[:4]
    if factor == 1:  # [^]  ==> [<]
        # boxes = y_min, 1 - x_max, y_max, 1 - x_min
        boxes_res[:, :, 0] = 1 - boxes[:, :, 3]  # y_min
        boxes_res[:, :, 1] = boxes[:, :, 0]  # x_min
        boxes_res[:, :, 2] = 1 - boxes[:, :, 1]  # y_max
        boxes_res[:, :, 3] = boxes[:, :, 2]  # x_max
    elif factor == 2:  # [^] ==> [v]
        # boxes = 1 - x_max, 1 - y_max, 1 - x_min, 1 - y_min
        boxes_res[:, :, 0] = 1 - boxes[:, :, 2]  # y_min
        boxes_res[:, :, 1] = 1 - boxes[:, :, 3]  # x_min
        boxes_res[:, :, 2] = 1 - boxes[:, :, 0]  # y_max
        boxes_res[:, :, 3] = 1 - boxes[:, :, 1]  # x_max
    elif factor == 3:  # [^] ==> [>]
        # boxes = 1 - y_max, x_min, 1 - y_min, x_max
        boxes_res[:, :, 0] = boxes[:, :, 1]  # y_min
        boxes_res[:, :, 1] = 1 - boxes[:, :, 2]  # x_min
        boxes_res[:, :, 2] = boxes[:, :, 3]  # y_max
        boxes_res[:, :, 3] = 1 - boxes[:, :, 0]  # x_max
    return boxes_res


def restore_boxes(boxes, rot90, flip, org_size, modified_img_size, padding):
    '''
        Restore boxes after known deformations
    :param boxes: (num,y1,x1,y2,x2) TF ObjDet API format
    :param rot90: one of None,1,2,3
    :param flip: one of None,1,2,3
    :return:
    '''
    # applying operations in reversed order
    if padding:
        boxes[:, :, 0] = (boxes[:, :, 0] * modified_img_size[1] - padding) / org_size[1]
        boxes[:, :, 1] = (boxes[:, :, 1] * modified_img_size[0] - padding) / org_size[0]
        boxes[:, :, 2] = (boxes[:, :, 2] * modified_img_size[1] - padding) / org_size[1]
        boxes[:, :, 3] = (boxes[:, :, 3] * modified_img_size[0] - padding) / org_size[0]
        boxes = np.clip(boxes, 0.0, 1.0)
        # TODO some boxes might become zero sized (which were fully on the padding)

    if rot90:
        rot90 = -rot90 % 4
        boxes = bbox_rot90(boxes, factor=rot90)

    if flip:
        boxes = bbox_flip(boxes, d=flip)

    return boxes


def box_fusion(boxes_list_by_model, points_list_by_model=None):
    '''
    Merge sets of boxes from ensembles. Supports  merging of center points from random-angle-rotation inference
    :param boxes_list: (class, score, x1, y1,x2,y2)
    :return:
    '''

    def _set_avg(L_box, models_num):
        '''
        Calc average between already stacked in a right way boxes (L_box)
        :param L_box:
        :param models_num:
        :return:
        '''
        avg_np = np.empty(shape=(len(L_box), 4))
        score_np = np.empty(shape=(len(L_box)))
        for i in range(len(L_box)):
            L_box_np = np.asarray(L_box[i])  # [num,score,x1,y1,x2,y2]
            box_set_score = L_box_np[:, 0:1]
            box_set = L_box_np[:, 1:] * box_set_score
            box_set = np.sum(box_set, axis=0)
            conf_sum = np.sum(box_set_score)
            avg_np[i] = box_set / conf_sum
            score_np[i] = conf_sum / models_num

        return avg_np, score_np

    def _add_to_L(L, boxes_per_model, models_num):
        '''
        Add box to stack
        :param L:
        :param boxes_per_model:
        :param models_num:
        :return:
        '''
        if not boxes_per_model:
            return
        if not L:
            for box in boxes_per_model:
                L.append([list(box)])
            return
        F_np, F_score_np = _set_avg(L, models_num=models_num)
        f_inds = np.argsort(-F_score_np, kind='mergesort')

        boxes_per_model_np = np.asarray(boxes_per_model)

        boxes_np = boxes_per_model_np[:, 1:]
        scores_np = boxes_per_model_np[:, 0]
        b_inds = np.argsort(-scores_np, kind='mergesort')
        F_np_sorted = F_np[f_inds]
        boxes_np_sorted = boxes_np[b_inds]
        iou = iou_run_norm(F_np_sorted, boxes_np_sorted)
        for box_i in range(len(boxes_np_sorted)):
            f_found_index = -1
            for f_i in range(len(F_np_sorted)):
                if iou[f_i, box_i] > 0.55:
                    L[f_inds[f_i]].append([scores_np[b_inds[box_i]]] + list(boxes_np_sorted[box_i]))
                    f_found_index = f_i
                    break
            if f_found_index == -1:
                # not matched box to any prior boxes
                L.append([[scores_np[b_inds[box_i]]] + list(boxes_np_sorted[box_i])])
            else:
                iou[f_found_index, :] = 0  # don't match to this group any boxes from the same model

    def _x1y1x2y2_to_xyl(bb: np.ndarray):
        '''
        Converts x1,y1,x2,y2 norm format to (x-center, y-center, sqrt(w*h))
        bb: [len,x1,y1,x2,y2]
        :return:
        '''
        bb_out = np.empty((bb.shape[0], 3))
        # x1, y1, x2, y2 = np.split(bb, 4, axis=1)
        bb_out[:, 0] = (bb[:, 0] + bb[:, 2]) / 2
        bb_out[:, 1] = (bb[:, 1] + bb[:, 3]) / 2
        bb_out[:, 2] = np.sqrt((bb[:, 3] - bb[:, 1]) * (bb[:, 2] - bb[:, 0]))
        return bb_out

    def _points_dist(box_centers, points):
        x1, y1, l1 = np.split(box_centers, 3, axis=1)
        x2, y2 = np.split(points, 2, axis=1)
        pairwise_dist = np.sqrt((x1 - np.transpose(x2)) ** 2 + (y1 - np.transpose(y2)) ** 2) / l1
        # TODO may be we need to divide by size of the box here. Like dist relative to size of the box
        return pairwise_dist

    def _add_point_to_L(L, points_per_model, models_num):
        if not points_per_model or not L:
            return
        F_np, F_score_np = _set_avg(L, models_num=models_num)
        f_inds = np.argsort(-F_score_np, kind='mergesort')
        points_per_model_np = np.asarray(points_per_model)
        points_np = points_per_model_np[:, 1:]
        scores_np = points_per_model_np[:, 0]
        p_inds = np.argsort(-scores_np, kind='mergesort')
        F_np_sorted = F_np[f_inds]
        points_np_sorted = points_np[p_inds]
        pair_dist = _points_dist(_x1y1x2y2_to_xyl(F_np_sorted), points_np_sorted)

        for point_i in range(len(points_np_sorted)):
            f_found_index = -1
            for f_i in range(len(F_np_sorted)):
                if pair_dist[
                    f_i, point_i] < 0.3:  # dist between box center and point is < then this proportion of box geom avg length
                    # we adding average box to affect score only.
                    L[f_inds[f_i]].append([scores_np[p_inds[point_i]]] + list(F_np_sorted[f_i]))
                    f_found_index = f_i
                    break
            if f_found_index == -1:
                # L.append([[scores_np[p_inds[box_i]]] + list(boxes_np_sorted[box_i])])
                # we ignore points that are not matched to anything
                pass
            else:
                pair_dist[f_found_index, :] = np.inf  # don't match to this group any points from the same model

    if len(boxes_list_by_model) == 0:
        # we don't have box predictions
        return boxes_list_by_model[0]
    elif len(boxes_list_by_model) == 1 and (points_list_by_model is None or len(points_list_by_model) == 0):
        # we have only one set of box predictions and no points. Nothing to merge
        return boxes_list_by_model[0]

    num_prediction_sets = len(boxes_list_by_model) + len(points_list_by_model)
    #
    # boxes_list = [[]] * len(dt_bboxes)
    # for model_i in range(len(dt_bboxes)):
    #     for bbox_i, bbox in enumerate(dt_bboxes[model_i]):
    #         # model_i => [class, score, x1,y1,x2,y2]
    #         boxes_list[model_i].append([dt_classes[model_i][bbox_i], dt_scores[model_i][bbox_i]] + list(
    #             dt_bboxes[model_i][bbox_i]))

    ##MERGING SETS OF BOXES
    boxes_list_by_class = {}
    for model_id in boxes_list_by_model:
        for box in boxes_list_by_model[model_id]:
            if box[0] not in boxes_list_by_class:  # box[0] - label_id
                boxes_list_by_class[box[0]] = {}
            if model_id not in boxes_list_by_class[box[0]]:
                boxes_list_by_class[box[0]][model_id] = []
            boxes_list_by_class[box[0]][model_id].append(box[1:])  # [label_id] -> [model_id] -> box
    merged_boxes = []
    L_per_class = {}
    for label in boxes_list_by_class:  # by label
        L_per_class[label] = []
        for boxex_per_model in boxes_list_by_class[label]:  # by model
            _add_to_L(L=L_per_class[label], boxes_per_model=boxes_list_by_class[label][boxex_per_model],
                      models_num=num_prediction_sets)
        # F_np, F_score_np = _set_avg(L_per_class[label], models_num=len(boxes_list_by_model))
        # for i in range(len(F_np)):
        #     #label, class, x1,y1,x2,y2
        #     merged_boxes.append([label, F_score_np[i]] + list(F_np[i]))

    ###MERGING POINTS TO BOXES
    if len(points_list_by_model) > 0:
        points_list_by_class = {}
        for model_id in points_list_by_model:
            for point in points_list_by_model[model_id]:
                if point[0] not in points_list_by_class:  # box[0] - label_id
                    points_list_by_class[point[0]] = {}
                if model_id not in points_list_by_class[point[0]]:
                    points_list_by_class[point[0]][model_id] = []
                points_list_by_class[point[0]][model_id].append(point[1:])  # [label_id] -> [model_id] -> box
        #        merged_boxes = []
        for label in points_list_by_class:  # by label
            if label not in L_per_class:
                continue  # we don't have boxes for this class, skip
            for points_per_model in points_list_by_class[label]:  # by model
                _add_point_to_L(L=L_per_class[label], points_per_model=points_list_by_class[label][points_per_model],
                                models_num=num_prediction_sets)

    ###GETTING AVERAGED BOXES
    merged_boxes = []
    for label in L_per_class:
        F_np, F_score_np = _set_avg(L_per_class[label], models_num=num_prediction_sets)
        for i in range(len(F_np)):
            merged_boxes.append([label, F_score_np[i]] + list(F_np[i]))

    return merged_boxes


def iou_run(bboxes1: np.ndarray, bboxes2: np.ndarray):
    '''
    Caculates iou matrix between two arrays of boxes. Boxes in int values
    :param bboxes1:[n,4] x1,y1,x2,y2 in integers
    :param bboxes2: [m,4] x1,y1,x2,y2 in integers
    :return: [n,m] matrix of ious. To fetch iou: [bboxes1_index, bboxes2_index]
    '''
    x11, y11, x12, y12 = np.split(bboxes1.reshape(-1,4), 4, axis=1)
    x21, y21, x22, y22 = np.split(bboxes2.reshape(-1,4), 4, axis=1)
    xA = np.maximum(x11, np.transpose(x21))
    yA = np.maximum(y11, np.transpose(y21))
    xB = np.minimum(x12, np.transpose(x22))
    yB = np.minimum(y12, np.transpose(y22))
    interArea = np.maximum((xB - xA + 1), 0) * np.maximum((yB - yA + 1), 0)
    boxAArea = (x12 - x11 + 1) * (y12 - y11 + 1)
    boxBArea = (x22 - x21 + 1) * (y22 - y21 + 1)
    iou = interArea / (boxAArea + np.transpose(boxBArea) - interArea)
    return iou

def iou_run_norm(bboxes1, bboxes2):
    '''
    Calculates iou matrix between two arrays of boxes. FOR NOrmalized boxes: 0..1
    :param bboxes1: [n,4] x1,y1,x2,y2 in integers
    :param bboxes2: [m,4] x1,y1,x2,y2 in integers
    :return: [n,m] matrix of ious. To fetch iou: [bboxes1_index, bboxes2_index]
    '''
    x11, y11, x12, y12 = np.split(bboxes1, 4, axis=1)
    x21, y21, x22, y22 = np.split(bboxes2, 4, axis=1)
    xA = np.maximum(x11, np.transpose(x21))
    yA = np.maximum(y11, np.transpose(y21))
    xB = np.minimum(x12, np.transpose(x22))
    yB = np.minimum(y12, np.transpose(y22))
    interArea = np.maximum((xB - xA), 0) * np.maximum((yB - yA), 0)
    boxAArea = (x12 - x11) * (y12 - y11)
    boxBArea = (x22 - x21) * (y22 - y21)
    iou = interArea / (boxAArea + np.transpose(boxBArea) - interArea)
    return iou