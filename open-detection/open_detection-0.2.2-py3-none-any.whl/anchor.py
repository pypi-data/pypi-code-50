import numpy as np
from math import sqrt


def generate_anchors(img_size, feature_map_size, aspect_ratio, scale, crop_out_of_range=True, keep_dim=False):
    """
    ```
    prior_boxes = od.anchor.generate_anchors(img_size=550,
                                             feature_map_size=[69, 35, 18, 9, 5],
                                             aspect_ratio=[1, 0.5, 2],
                                             scale=[24, 48, 96, 192, 384])

    print(prior_boxes.shape)
    ```
    :param img_size:
    :param feature_map_size:
    :param aspect_ratio:
    :param scale:
    :param crop_out_of_range:
    :param keep_dim:
    :return: (N, 4) => [x1, y1, x2, y2], if not keep_dim
             (N, fea_size, fea_size, ar_size, 4) => [x1, y1, x2, y2], if keep_dim
    """
    fea_sizes = feature_map_size
    aspect_ratios = aspect_ratio
    anchor_sizes = scale

    ar = np.array(aspect_ratios, dtype=np.float32)
    ar = np.sqrt(ar)

    prior_boxes = []
    for fea_size, anchor_size in zip(fea_sizes, anchor_sizes):
        x = np.arange(fea_size)
        y = np.arange(fea_size)
        gx, gy = np.meshgrid(x, y)

        s = float(img_size) / (fea_size + 1)

        gcx = (gx + 1) * s
        gcy = (gy + 1) * s
        gcx = np.reshape(gcx, [fea_size, fea_size, 1]).astype(np.float32)
        gcy = np.reshape(gcy, [fea_size, fea_size, 1]).astype(np.float32)

        ws = np.ones([fea_size, fea_size, len(aspect_ratios)], dtype=np.float32) * anchor_size
        hs = np.copy(ws)

        ar2 = np.repeat(ar, fea_size * fea_size)
        ar2 = np.reshape(ar2, [len(aspect_ratios), fea_size, fea_size])
        ar2 = np.transpose(ar2, [1, 2, 0])

        ws *= ar2
        hs /= ar2

        gx1 = gcx - ws / 2
        gy1 = gcy - hs / 2
        gx2 = gx1 + ws
        gy2 = gy1 + hs

        if crop_out_of_range:
            gx1 = np.maximum(gx1, 0)
            gy1 = np.maximum(gy1, 0)
            gx2 = np.minimum(gx2, img_size)
            gy2 = np.minimum(gy2, img_size)

        anchor = np.stack([gx1, gy1, gx2, gy2], axis=-1)
        prior_boxes.append(anchor)

    if not keep_dim:
        prior_boxes = [np.reshape(anchor, [-1, 4]) for anchor in prior_boxes]
        prior_boxes = np.concatenate(prior_boxes, axis=0)

    return prior_boxes


def calc_area(bboxes):
    """
    :param bboxes: (N, 4) => [x1, y1, x2, y2]
    :return: (N,)
    """
    assert bboxes.ndim == 2 and bboxes.shape[1] == 4

    x1, y1, x2, y2 = bboxes[:, 0], bboxes[:, 1], bboxes[:, 2], bboxes[:, 3]
    return (x2 - x1) * (y2 - y1)


def calc_iou(a, b):
    """
    :param a: (NA, 4) => [x1, y1, x2, y2]
    :param b: (NB, 4) => [x1, y1, x2, y2]
    :return: (NA,NB)
    """
    assert a.ndim == 2 and a.shape[1] == 4
    assert b.ndim == 2 and b.shape[1] == 4

    num_a, num_b = a.shape[0], b.shape[0]
    a = a.reshape([num_a, 1, 4]).repeat(num_b, axis=1)
    b = b.reshape([1, num_b, 4]).repeat(num_a, axis=0)

    a_x1, a_y1, a_x2, a_y2 = a[:, :, 0], a[:, :, 1], a[:, :, 2], a[:, :, 3]
    b_x1, b_y1, b_x2, b_y2 = b[:, :, 0], b[:, :, 1], b[:, :, 2], b[:, :, 3]
    a_area = (a_x2 - a_x1) * (a_y2 - a_y1)
    b_area = (b_x2 - b_x1) * (b_y2 - b_y1)

    max_x1 = np.maximum(a_x1, b_x1)
    min_x2 = np.minimum(a_x2, b_x2)
    max_y1 = np.maximum(a_y1, b_y1)
    min_y2 = np.minimum(a_y2, b_y2)

    inter_w = np.maximum(0, min_x2 - max_x1)
    inter_h = np.maximum(0, min_y2 - max_y1)
    inter = inter_w * inter_h

    return inter / (a_area + b_area - inter)


def matching(anchors, gt_bboxes, gt_labels, threshold_pos=0.5, threshold_neg=0.4):
    """
    :param anchors (num_anchors, 4) => [x1, y1, x2, y2]
    :param gt_bboxes: (num_bboxes, 4) => [x1, y1, x2, y2]
    :param gt_labels: (num_bboxes,)
    :param threshold_pos: default value is 0.5
    :param threshold_neg: default value is 0.4
    :return: matched: (num_anchors,) in [-1, 0, 1], bboxes: (num_anchors, 4) => [x1, y1, x2, y2], labels: (num_anchors,)
    """
    # calculate iou => [num_anchors, num_bboxes]
    iou = calc_iou(anchors, gt_bboxes)

    # assign the max overlap gt index for each anchor
    max_iou_for_anchors = np.max(iou, axis=-1)
    max_id_for_anchors = np.argmax(iou, axis=-1)

    # pos=1, neg=-1, ignore=0
    matched = np.zeros_like(max_iou_for_anchors, dtype=int)
    matched[max_iou_for_anchors >= threshold_pos] = 1
    matched[max_iou_for_anchors <= threshold_neg] = -1

    # gather
    labels = gt_labels[max_id_for_anchors]
    bboxes = gt_bboxes[max_id_for_anchors]
    return matched, bboxes, labels, max_id_for_anchors


def bbox2offset(anchors, bboxes):
    """
    :param anchors: (N, 4) => [x1, y1, x2, y2]
    :param bboxes: (N, 4) => [x1, y1, x2, y2]
    :return: (N, 4) => r[cx, cy, w, h]
    """
    assert anchors.ndim == 2 and anchors.shape[1] == 4
    assert bboxes.ndim == 2 and bboxes.shape[1] == 4
    assert anchors.shape[0] == bboxes.shape[0]

    # convert to center form
    w = anchors[:, 2] - anchors[:, 0]
    h = anchors[:, 3] - anchors[:, 1]
    center_anchors = np.stack([anchors[:, 0] + (w / 2), anchors[:, 1] + (h / 2), w, h], axis=-1)

    w = bboxes[:, 2] - bboxes[:, 0]
    h = bboxes[:, 3] - bboxes[:, 1]
    center_gt = np.stack([bboxes[:, 0] + (w / 2), bboxes[:, 1] + (h / 2), w, h], axis=-1)

    # calculate offset
    g_hat_cx = (center_gt[:, 0] - center_anchors[:, 0]) / center_anchors[:, 2]
    g_hat_cy = (center_gt[:, 1] - center_anchors[:, 1]) / center_anchors[:, 3]
    g_hat_w = np.log(center_anchors[:, 2] / center_gt[:, 2])
    g_hat_h = np.log(center_anchors[:, 3] / center_gt[:, 3])
    offset = np.stack([g_hat_cx, g_hat_cy, g_hat_w, g_hat_h], axis=-1)
    return offset


def offset2bbox(anchors, offset):
    """
    :param anchors: anchors: (N, 4) => [x1, y1, x2, y2]
    :param offset: (N, 4) => r[cx, cy, w, h]
    :return: (N, 4) => [x1, y1, x2, y2]
    """
    # convert to center form
    w = anchors[:, 2] - anchors[:, 0]
    h = anchors[:, 3] - anchors[:, 1]
    center_anchors = np.stack([anchors[:, 0] + (w / 2), anchors[:, 1] + (h / 2), w, h], axis=-1)

    # convert from center form
    g_hat_cx, g_hat_cy, g_hat_w, g_hat_h = offset[:, 0], offset[:, 1], offset[:, 2], offset[:, 3]
    bboxes_cx = g_hat_cx * center_anchors[:, 2] + center_anchors[:, 0]
    bboxes_cy = g_hat_cy * center_anchors[:, 3] + center_anchors[:, 1]
    bboxes_w = center_anchors[:, 2] / np.exp(g_hat_w)
    bboxes_h = center_anchors[:, 3] / np.exp(g_hat_h)

    bboxes_x = bboxes_cx - bboxes_w / 2
    bboxes_y = bboxes_cy - bboxes_h / 2
    bboxes = np.stack([bboxes_x, bboxes_y, bboxes_x + bboxes_w, bboxes_y + bboxes_h], axis=-1)
    return bboxes
