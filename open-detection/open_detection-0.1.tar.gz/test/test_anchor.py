import open_detection as od
import numpy as np

anchors = od.anchor.generate_anchors(img_size=550,
                                     feature_map_size=[69, 35, 18, 9, 5],
                                     aspect_ratio=[1, 0.5, 2],
                                     scale=[24, 48, 96, 192, 384])

print(anchors.shape)

gt_bboxes = np.array([[10, 10, 100, 120],
                      [20, 30, 150, 170]], dtype=np.float32)
gt_labels = np.array([3, 7], dtype=np.int)

matched, bboxes, labels = od.anchor.matching(anchors, gt_bboxes, gt_labels)

offset = od.anchor.bbox2offset(anchors, bboxes)
bboxes2 = od.anchor.offset2bbox(anchors, offset)

print(np.abs(bboxes - bboxes2).max())
