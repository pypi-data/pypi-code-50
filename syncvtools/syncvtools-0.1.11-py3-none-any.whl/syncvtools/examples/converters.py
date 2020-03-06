from syncvtools.utils.draw_detections import DrawDetections
from syncvtools.utils.data_import import TFRecords, TFObjDetAPIDetections, PascalVOC
from syncvtools.utils.data_export import TFRecordsExport, PascalVOCExport
from syncvtools.data.detections import DetectionEntity
import itertools, cv2

def tfrecord_shrink(input_tfrecord: str, output_tfrecord: str, slice: slice = slice(0,3) ):
    '''
        Shrink a tfrecord using Python's standard slicing method
    :param input_tfrecord: path to input TF record
    :param output_tfrecord: path where to save output TF record
    :return:
    '''
    tf_gts = TFRecords.parse(tfrecord_src=input_tfrecord)
    tf_gts = tf_gts[slice]
    TFRecordsExport.export(src = tf_gts, out_path=output_tfrecord)


def pascalvoc_to_tfrecord(img_dir, pascal_voc_dir, output_tfrecord, label_map, slice: slice = None):
    '''
    :param img_dir: Directory with input images
    :param pascal_voc_dir: Directory with XML annotations (one file corresponds to one image)
    :param output_tfrecord: Path to output TF Record
    :param label_map: Path to label_map in TF format.
    :param slice: Slice in Python's format: slice(0,3)
    :return:
    '''
    pascal_gts = PascalVOC.parse(img_dir=img_dir, annotations_dir=pascal_voc_dir)
    if slice:
        pascal_gts = pascal_gts[slice]
    # to convert to TensorFlow we need to apply label_map, since label_id is required for TF-Record
    pascal_gts.process_labelmap(label_dict = label_map)
    TFRecordsExport.export(src=pascal_gts, out_path=output_tfrecord)


def pascalvoc_generate_threatless(input_img_dir, output_pascal_voc_dir):
    '''
    Making pascalvoc annotations for threatless data.
    Original: generate_xml_threatless.py
    :param input_img_dir:
    :param output_pascal_voc_dir:
    :return:
    '''
    pascal_imgs = PascalVOC.parse(img_dir=input_img_dir)
    #now set empty Ground truth to all items
    empty_detections = {}
    #and also set some meta fields required by PascalVOC (usually they parsed from XML, but we don't have it here)
    gt_metadata = {}
    for key in pascal_imgs:
        empty_detections[key] = []
        gt_metadata[key] = {'image_filename': pascal_imgs[key].img.img_filename,
                            'image_path':pascal_imgs[key].img.img_src or pascal_imgs[key].img.img_filename}

    pascal_imgs.process_detections(empty_detections)
    pascal_imgs.process_field('gt_metadata', gt_metadata)

    #now just dump it to some dir, ignoring images
    PascalVOCExport.export(src=pascal_imgs, out_xml_path=output_pascal_voc_dir)