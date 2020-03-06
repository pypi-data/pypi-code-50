'''
Part of Dec'2019 experiment to rotate images on random angle and infer only center of the bbox.
'''
from syncvtools.data.image import ImgSize
from typing import Tuple, Any, Union
import numpy as np
from math import cos, sin, radians


def validate_norm_coords(point: Tuple[float, float]):
    if point is None or len(point) != 2:
        raise ValueError("point should take a tuple of float (x1,y1)")
    for coord in point[:4]:
        if coord < (0 - 1e-4) or coord > (1 + 1e-4):
            raise ValueError("Norm coordinates should be [0;1]: {}".format(point[:4]))
    return (max(0, point[0]), min(1, point[1]))


def normalize_point(point: Tuple[int, int], img_size: Tuple[int, int]) -> Tuple[float, float]:
    if point is None or len(point) < 2 or len(point) > 3:
        raise ValueError("point is either None or not a tuple of size 4,5: (x, ymin, [conf])")
    img_size = ImgSize(width=img_size[0], height=img_size[1])
    norm_coords = (float(point[0] / img_size.width), float(point[1] / img_size.height))
    norm_coords = (min(1.0, max(0.0, norm_coords[0])), min(1.0, max(0.0, norm_coords[1])))
    # for coord in norm_coords:
    #     if coord < 0 or coord > 1:
    #         raise ValueError("Norm coordinates should be [0;1]: {}".format(point[:4]))
    return norm_coords


def denormalize_point(point: Tuple[float, float], img_size: Tuple[int, int]) -> Tuple[int, int]:
    def cl(v, mn, mx):
        return max(min(v, mx), mn)

    # just to validate width/height
    img_size = ImgSize(width=img_size[0], height=img_size[1])
    point = validate_norm_coords(point=point)
    abs_coords = point[0] * img_size.width, point[1] * img_size.height
    abs_coords = list(map(int, map(round, abs_coords)))
    abs_coords = (cl(abs_coords[0], 0, img_size.width - 1),
                  cl(abs_coords[1], 0, img_size.height - 1),
                  )
    return abs_coords


def backward_rotation_bbox_tf(bbox_norm: np.ndarray, angle, org_size, rot_size):
    angle = radians(-angle)
    point = np.empty((bbox_norm.shape[0], bbox_norm.shape[1], 2))
    # find center x,y
    point[:, :, 0] = (bbox_norm[:, :, 1] + bbox_norm[:, :, 3]) / 2
    point[:, :, 1] = (bbox_norm[:, :, 0] + bbox_norm[:, :, 2]) / 2
    # to abs
    point[:, :, 0] *= rot_size[0]
    point[:, :, 1] *= rot_size[1]
    # find original image origin point, and rotated image origin point
    org_center = (np.array(org_size) - 1) / 2.
    rot_center = (np.array(rot_size) - 1) / 2.
    # shift rotated point to rotated origin
    rot_point = point - rot_center
    orig_point = np.copy(rot_point)
    # find original_point (relativ to original image origin)
    orig_point[:, :, 0] = rot_point[:, :, 0] * np.cos(angle) + rot_point[:, :, 1] * np.sin(angle)
    orig_point[:, :, 1] = -rot_point[:, :, 0] * np.sin(angle) + rot_point[:, :, 1] * np.cos(angle)
    # shift back from origin (center) to 0,0 of image
    res = orig_point + org_center
    res = np.round(res).astype(np.int32)
    return res


if __name__ == '__main__':
    from syncvtools.utils.draw_detections import DrawDetections, imshow
    from syncvtools.utils.image import img_rotate
    from syncvtools.utils.bbox import denormalize_bbox, normalize_bbox


    def forward_rotation(bbox_abs: np.ndarray, angle, org_size, rot_size):
        point = np.asarray(bbox_abs)
        angle = radians(angle)
        org_center = (np.array(org_size) - 1) / 2.
        rot_center = (np.array(rot_size) - 1) / 2.
        org = point - org_center
        new = np.array([org[0] * np.cos(angle) + org[1] * np.sin(angle),
                        -org[0] * np.sin(angle) + org[1] * np.cos(angle)])
        res = new + rot_center
        return res


    def backward_rotation(bbox_abs: np.ndarray, angle, org_size, rot_size):
        point = np.asarray(bbox_abs)
        angle = radians(-angle)
        org_center = (np.array(org_size) - 1) / 2.
        rot_center = (np.array(rot_size) - 1) / 2.
        rot_point = point - rot_center
        orig_point = np.array([rot_point[0] * np.cos(angle) + rot_point[1] * np.sin(angle),
                               -rot_point[0] * np.sin(angle) + rot_point[1] * np.cos(angle)])
        res = orig_point + org_center
        return res


    # def backward_rotation_bbox_tf(bbox_norm: np.ndarray, angle, org_size, rot_size):
    #     angle = radians(-angle)
    #     point = np.empty((bbox_norm.shape[0], bbox_norm.shape[1], 2))
    #     #find center x,y
    #     point[:, :, 0] = (bbox_norm[:, :, 0] + bbox_norm[:, :, 2]) / 2
    #     point[:, :, 1] = (bbox_norm[:, :, 1] + bbox_norm[:, :, 3]) / 2
    #     #to abs
    #     point[:, :, 0] *= rot_size[0]
    #     point[:, :, 1] *= rot_size[1]
    #     #find original image origin point, and rotated image origin point
    #     org_center = (np.array(org_size) - 1) / 2.
    #     rot_center = (np.array(rot_size) - 1) / 2.
    #     #shift rotated point to rotated origin
    #     rot_point = point - rot_center
    #     orig_point = np.copy(rot_point)
    #     #find original_point (relativ to original image origin)
    #     orig_point[:,:,0]  =   rot_point[:,:,0] * np.cos(angle) + rot_point[:,:,1] * np.sin(angle)
    #     orig_point[:, :, 1] = -rot_point[:,:,0] * np.sin(angle) + rot_point[:,:,1] * np.cos(angle)
    #     #shift back from origin (center) to 0,0 of image
    #     res = orig_point + org_center
    #     return res

    import syncvtools.utils.file_tools as ft

    test_bbox = DrawDetections(bbox_line_height=2)
    img_np = ft.img_np_from_disk('/Users/apatsekin/Downloads/1576174609133332342.png')
    orig_img = img_np.astype(np.uint8)
    rotated_image = img_rotate(orig_img, degree=170)
    point = (150, 500)
    rotated_box = (point[0] - 5, point[1] - 5, point[0] + 5,
                   point[1] + 5)  # denormalize_bbox(bbox=orig_box, img_size=(or_img.shape[1],or_img.shape[0]))
    rotated_box_norm = normalize_bbox(bbox=rotated_box, img_size=(rotated_image.shape[1], rotated_image.shape[0]))
    # changing to tf format
    rotated_box_norm = (rotated_box_norm[1], rotated_box_norm[0], rotated_box_norm[3], rotated_box_norm[2])
    rot_box_norm = np.asarray(rotated_box_norm).reshape(1, 1, -1)
    point_restore = backward_rotation_bbox_tf(rot_box_norm, 170, (orig_img.shape[1], orig_img.shape[0]),
                                              (rotated_image.shape[1], rotated_image.shape[0]))
    # point_restore_abs = denormalize_point(point_restore, img_size=(orig_img.shape[1],orig_img.shape[0]))
    point_restore = point_restore[0][0]
    img_bbox_before = test_bbox.draw_one(img_np=rotated_image,
                                         bbox=rotated_box,
                                         label_txt="Demo detection", score=0.435, prefix="[prefix] sdfs dfs dfsd fsdf ",
                                         suffix="[suffix]",
                                         color_id=0, tag_orientation=0)
    img_bbox = test_bbox.draw_one(img_np=orig_img,
                                  bbox=(int(point_restore[0]) - 5,
                                        int(point_restore[1] - 5),
                                        int(point_restore[0] + 5),
                                        int(point_restore[1] + 5)),
                                  label_txt="Demo detection", score=0.435, prefix="[prefix] sdfs dfs dfsd fsdf ",
                                  suffix="[suffix]",
                                  color_id=0, tag_orientation=0)

    imshow(img_bbox_before)
    imshow(img_bbox)
