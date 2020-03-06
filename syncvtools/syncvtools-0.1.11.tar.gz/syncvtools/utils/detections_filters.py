'''
Filters used to filter DetectionCollections.
There are two types of functions here: filters and constructors.
Constructors return functions (filters) providing them some data.
'''

from syncvtools.data.detections import ImageLevelDetections
import syncvtools.utils.file_tools as ft
import os
import syncvtools.config as config
import logging


def _parse_key_list_input(keys_list_src):
    '''
    Supports:
    - tuples, lists, sets.
    - file with keys or list of files with keys
    - dir with files with keys or list of dirs with keys

    :param key_list_src:
    :return:
    '''
    if not keys_list_src:
        raise ValueError("Empty keys input passed")
    filter_keys_list = set()
    if isinstance(keys_list_src, str):  # may be it's a path
        if os.path.isfile(keys_list_src):  # path to list of keys?
            lst_ = ft.file_to_list(keys_list_src)
            logging.info("Using for filtering ({}): {}".format(len(lst_), keys_list_src))
            filter_keys_list.update(lst_)  # it's a file with list
        elif os.path.isdir(keys_list_src):  # or to dir with lists of keys?
            for exc_file in ft.get_file_list_by_ext(dir=keys_list_src, ext=('txt', 'log', 'keys'), recursive=True):
                lst_ = ft.file_to_list(exc_file)
                logging.info("Using for filtering ({}): {}".format(len(lst_), exc_file))
                filter_keys_list.update(lst_)
        else:  # guess it's just a value
            if '/' in keys_list_src:
                raise ValueError("It looks like non-existant path: {}".format(keys_list_src))
            filter_keys_list.add(keys_list_src)  # it's just a value
            logging.info("Adding to filter key: {}".format(keys_list_src))
    else:  # guess it's iterable
        for key_list_item in keys_list_src:
            filter_keys_list.update(_parse_key_list_input(key_list_item))
    return filter_keys_list


def image_level_remove_with_unknown_bboxes(img_det: ImageLevelDetections, img_key) -> bool:
    '''
    Removes images with boxes that parser wasn't able to parse from full-tag (annotation) and set to "unknown_tag'
    See DetectionEntity.__init__ for that.
    :param img_det:
    :return:
    '''
    # stat = {'dropped_unknown': 0, 'dropped_question': 0}
    if not img_det.ground_truth:
        return False
    is_drop = False
    for gt in img_det.ground_truth:
        if gt.label_text == config.NOT_PARSED_LABEL:
            is_drop = True
            break
    return is_drop


def image_level_remove_with_question_bboxes(img_det: ImageLevelDetections, img_key) -> bool:
    '''
    Removes images with uncertain annotations (labeld as ?)
    :param img_det:
    :return:
    '''
    # stat = {'dropped_unknown': 0, 'dropped_question': 0}
    if not img_det.ground_truth:
        return False
    is_drop = False
    for gt in img_det.ground_truth:
        if gt.label_text == 'uncertain':
            is_drop = True
            break
    return is_drop


def image_level_remove_boxes_with_suffix_constructor(suffix_list: tuple):
    def _image_level_remove_with_boxes_with_suffix(img_det: ImageLevelDetections, img_key) -> bool:
        '''
        Removes images with certain suffixes annotations. Suffix can be anywhere
        :param img_det:
        :return:
        '''
        if not img_det.ground_truth:
            return False
        is_drop = False
        for gt in img_det.ground_truth:
            for sf in suffix_list:
                if sf in gt.label_full_tag:
                    is_drop = True
                    break
            if is_drop:
                break
        return is_drop

    return _image_level_remove_with_boxes_with_suffix


def image_level_filterout_hard_gt_constructor(suffix_list=('-3C', '-4C')):
    return image_level_remove_boxes_with_suffix_constructor(suffix_list=suffix_list)


def image_level_filter_by_key_list_constructor(keys_list_src, trueRemove_falseKeep=True):
    '''
    Filtering by img keys
    :param keys_list_src:
    :param trueRemove_falseKeep:
    :return:
    '''
    filter_keys_list = _parse_key_list_input(keys_list_src)

    logging.info(
        "Key list is loaded to {} - {}".format("ignore" if trueRemove_falseKeep else "keep", len(filter_keys_list)))

    def _image_level_filter_by_key_list(img_det: ImageLevelDetections, img_key) -> bool:
        return not (trueRemove_falseKeep ^ (img_key in filter_keys_list))

    return _image_level_filter_by_key_list


def image_level_filter_by_label_list_constructor(keys_list_src, trueRemove_falseKeep=False):
    '''
    Filters specific labels.
    :param filter_list: list of classes to filter, one class or path to file with list of classes
    :param trueRemove_falseKeep:
    :return:
    '''
    filter_keys_list = _parse_key_list_input(keys_list_src)

    logging.info("Label list is loaded to ignore - {}".format(list(filter_keys_list)))

    def image_level_filter_by_label_list(img_det: ImageLevelDetections, img_key) -> bool:
        is_drop = False
        if not img_det.ground_truth:
            return False

        for gt in img_det.ground_truth:
            if not (trueRemove_falseKeep ^ (
                    gt.label_text in filter_keys_list)):  # ('ammo-round','shotgun-shell','ammo-pack','cylinder'):
                is_drop = True
                break
        return is_drop

    return image_level_filter_by_label_list


def image_level_filter_threatless_from_agp_constructor(
        filter_list=('ammo-round', 'shotgun-shell', 'ammo-pack', 'cylinder', 'magazine', 'slide', 'ammo-many')):
    '''
    From AGP dataset keep only images with AGP-save classes (no receiver)
    :param filter_list:
    :return:
    '''
    return image_level_filter_by_label_list_constructor(keys_list_src=filter_list, trueRemove_falseKeep=False)


def image_level_filter_threatless_constructor(trueRemove_falseKeep=False):
    def _image_level_filter_threatless(img_det: ImageLevelDetections, img_key) -> bool:
        if trueRemove_falseKeep ^ (bool(img_det.ground_truth) and len(img_det.ground_truth) > 0):
            return True

    return _image_level_filter_threatless


def image_level_set_empty_gt_for_missing_annotation(img_det: ImageLevelDetections, img_key) -> bool:
    '''
    Technically not filters everything, but sets empty GT for objects without it.
    :param img_det:
    :param img_key:
    :return:
    '''
    if img_det.ground_truth is None:
        img_det.ground_truth = []
    return False  # otherwise image will be deleted
