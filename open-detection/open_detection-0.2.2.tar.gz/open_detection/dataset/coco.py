from pycocotools.coco import COCO
import numpy as np
import sys, os, cv2, time

from open_detection.dataset.parallel import ParallelGenerator
from open_detection.anchor import *


class COCODataSet:
    def __init__(self, data_root, kind="train2017", shuffle=False, shuffle_seed=None):
        self.data_root = data_root
        self.kind = kind
        self.shuffle = shuffle
        self.shuffle_seed = shuffle_seed

        self.images_dir = os.path.join(data_root, kind)
        if kind.startswith("test"):
            self.annotation_file = False
            self.image_files = [os.path.join(self.images_dir, filename) for filename in os.listdir(self.images_dir)]
        else:
            self.annotation_file = os.path.join(data_root, "annotations", f"instances_{kind}.json")
            self.annotation_coco = COCO(self.annotation_file)
            self.image_ids = list(self.annotation_coco.imgToAnns.keys())
            self.image_ids = self.image_ids[:10]

    def __len__(self):
        return len(self.image_ids) if self.annotation_file else len(self.image_files)

    def _load_data_item(self, img_id):
        img_info = self.annotation_coco.loadImgs([img_id])[0]
        img_file = os.path.join(self.images_dir, img_info.get("file_name"))
        image = cv2.imread(img_file)

        ann_ids = self.annotation_coco.getAnnIds([img_id])
        anns = self.annotation_coco.loadAnns(ann_ids)

        gt_labels, gt_bboxes, gt_masks, gt_is_crowd = [], [], [], []
        for ann in anns:
            x, y, w, h = ann.get("bbox")
            gt_labels.append(ann.get("category_id"))
            gt_bboxes.append([x, y, x + w, y + h])
            gt_masks.append(self.annotation_coco.annToMask(ann))
            gt_is_crowd.append(ann.get("iscrowd"))

        return {
            'image': image,
            'gt_labels': gt_labels,
            'gt_bboxes': gt_bboxes,
            'gt_masks': gt_masks,
            'gt_is_crowd': gt_is_crowd,
            'anns': anns
        }

    def __iter__(self):
        # 1.test
        if self.kind.startswith("test"):
            for file in self.image_files:
                yield cv2.imread(file)
            return

        # 2.shuffle
        if self.shuffle:
            if self.shuffle_seed is not None:
                np.random.seed(self.shuffle_seed)
            np.random.shuffle(self.image_ids)

        # 3.train or val
        for img_id in self.image_ids:
            yield self._load_data_item(img_id)


def enforce_size(img, bbox, masks, image_size=550, proto_output_size=138):
    """ Ensures that the image is the given size without distorting aspect ratio. """
    h, w, _ = img.shape
    new_h, new_w = image_size, image_size

    if h == new_h and w == new_w:
        return img, bbox, masks

    # Resize the image so that it fits within new_w, new_h
    w_prime = new_w
    h_prime = h * new_w / w

    if h_prime > new_h:
        w_prime *= new_h / h_prime
        h_prime = new_h

    w_prime = int(w_prime)
    h_prime = int(h_prime)

    # Do all the resizing
    img = cv2.resize(img, (w_prime, h_prime))

    # Act like each object is a color channel
    masks = [cv2.resize(mask, (w_prime, h_prime)) for mask in masks]

    # Scale bounding boxes (this will put them in the top left corner in the case of padding)
    dx, dy = w_prime / w, h_prime / h
    bbox = [(x * dx, y * dy, w * dx, h * dy) for (x, y, w, h) in bbox]

    # Finally, pad everything to be the new_w, new_h
    pad_dims = [(0, new_h - h_prime), (0, new_w - w_prime), (0, 0)]
    img = np.pad(img, pad_dims, 'constant', constant_values=0)

    pad_dims = [(0, new_h - h_prime), (0, new_w - w_prime)]
    masks = [np.pad(mask, pad_dims, 'constant', constant_values=0) for mask in masks]
    masks = [cv2.resize(mask, (proto_output_size, proto_output_size)) for mask in masks]

    return img, bbox, masks


def train(data_root,
          anchors,
          kind="2017",
          image_size=550,
          proto_output_size=138,
          threshold_pos=0.5,
          threshold_neg=0.4,
          batch_size=32,
          shuffle=True,
          shuffle_seed=None,
          total_iter=0,
          num_workers=7,
          max_queue=32,
          use_multiprocess_reader=True):
    def transform(data):
        image = data["image"]
        gt_labels_origin = data["gt_labels"]
        gt_bboxes_origin = data["gt_bboxes"]
        gt_masks_origin = data["gt_masks"]

        image, gt_bboxes, gt_masks = enforce_size(image, gt_bboxes_origin, gt_masks_origin, image_size=image_size,
                                                  proto_output_size=proto_output_size)

        gt_labels = np.array(gt_labels_origin, dtype=np.int)
        gt_bboxes = np.array(gt_bboxes, dtype=np.float32)

        matched, gt_bboxes, gt_labels, id_for_anchors = matching(anchors, gt_bboxes, gt_labels,
                                                                 threshold_pos=threshold_pos,
                                                                 threshold_neg=threshold_neg)
        gt_bboxes = bbox2offset(anchors, gt_bboxes)

        return {
            "image": image,
            "gt_labels_origin": gt_labels_origin,
            "gt_bboxes_origin": gt_bboxes_origin,
            "gt_masks_origin": gt_masks_origin,
            "gt_labels": gt_labels,
            "gt_bboxes": gt_bboxes,
            "gt_masks": gt_masks,
            "matched": matched,
            "id_for_anchors": id_for_anchors
        }

    def batch_reader():
        generator = COCODataSet(data_root, kind="train" + kind, shuffle=shuffle, shuffle_seed=shuffle_seed)

        batch = []
        while True:
            for data in generator:
                data = transform(data)
                batch.append(data)
                if len(batch) == batch_size:
                    yield {
                        "image": np.stack([item.get("image") for item in batch]),
                        "gt_labels_origin": [item.get("gt_labels_origin") for item in batch],
                        "gt_bboxes_origin": [item.get("gt_bboxes_origin") for item in batch],
                        "gt_masks_origin": [item.get("gt_masks_origin") for item in batch],
                        "gt_labels": np.stack([item.get("gt_labels") for item in batch]),
                        "gt_bboxes": np.stack([item.get("gt_bboxes") for item in batch]),
                        "gt_masks": [item.get("gt_masks") for item in batch],
                        "matched": np.stack([item.get("matched") for item in batch]),
                        "id_for_anchors": [item.get("id_for_anchors") for item in batch]
                    }
                    batch = []

    if not use_multiprocess_reader:
        def _reader():
            cnt = 0
            for data in batch_reader():
                cnt += 1
                yield data
                if cnt >= total_iter:
                    break

        return _reader
    else:
        if sys.platform == "win32":
            print("multiprocess is not fully compatible with Windows, "
                  "you can set --use_multiprocess_reader=False if you "
                  "are training on Windows and there are errors incured "
                  "by multiprocess.")
        print("multiprocess reader starting up, it takes a while...")

    def parallel_batch_reader():
        generator = ParallelGenerator(batch_reader(), use_multiprocessing=use_multiprocess_reader)
        cnt = 0
        try:
            generator.start(max_queue_size=max_queue, workers=num_workers)
            generator_out = None
            while True:
                while generator.is_running():
                    if not generator.queue.empty():
                        generator_out = generator.queue.get()
                        break
                    else:
                        time.sleep(0.02)
                yield generator_out
                cnt += 1
                if cnt >= total_iter:
                    generator.stop()
                    return
                generator_out = None
        except Exception as e:
            print("Exception occured in reader: {}".format(str(e)))
        finally:
            generator.stop()

    return parallel_batch_reader
