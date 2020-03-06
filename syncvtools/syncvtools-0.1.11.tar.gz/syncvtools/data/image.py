from __future__ import annotations
import numpy as np
import syncvtools.utils.file_tools as ft
import os, logging
from typing import Tuple


# from scipy import ndimage
# import syncvtools.config as synconfig

class ImgSize:
    def __init__(self, width: int, height: int, channels: int = None):
        '''
        Property of Image class to store dimensions of image.
        Since image size sometimes (w,h,c) or (h,w,c) or (c,w,h) this is data class to eliminate confusion.
        :param width:
        :param height:
        :param channels:
        '''
        self.width = width
        self.height = height
        self.channels = channels

    def as_tuple(self):
        if self.channels is not None:
            return self.width, self.height, self.channels
        else:
            return self.width, self.height

    def __str__(self):
        return "{}".format((self.width, self.height, self.channels))


class Image:
    def __init__(self, img_np: np.ndarray = None, img_filename=None, img_src=None):
        '''
        Image class which supports lazy loading and parsing img dimensions without decoding/loading whole image. (fast)
        :param img_np: (h,w,c) in uint8 can be provided (optional)
        :param img_filename: just file name (not full path)
        :param img_src: path to the image  if lazy loading required
        '''
        # TODO need to be immutable
        self._img_np = img_np
        self.img_filename = img_filename
        self.img_src = img_src
        self._img_size = None
        if img_np is not None:
            self._img_size = ImgSize(width=self.img_np.shape[1], height=self.img_np.shape[0],
                                     channels=self.img_np.shape[2])

    def size(self) -> Tuple:
        return self.img_np.shape

    @property
    def img_size(self) -> ImgSize:
        if not self._img_size:
            width, height = ft.get_img_size(self.img_src)
            # ^ TODO A VERY WEAK ASSUMPTION HERE THAT WE HAVE 3 CHANNElS, BUT works so far for our use cases
            # But otherwise we need to use MUCH slower method
            self._img_size = ImgSize(width=width, height=height, channels=3)
        return self._img_size

    def free_img_np(self):
        '''
        Cleans out image array from memory. Although image size is still accessible.
        Be careful, if self.img_src doesn't exist and self.img_src is not set, it will fail if you try to access self.img_np, since there is no place
        to pick up image from.
        :return:
        '''
        self._img_np = None

    @property
    def img_np(self) -> np.ndarray:
        if self._img_np is None:
            '''
            For lazy loading we don't store images in memory even after they were loaded. 
            In future it's better to add LRU cache here
            '''
            img_np = ft.img_np_from_disk(self.img_src)
            self._img_size = ImgSize(width=img_np.shape[1],
                                     height=img_np.shape[0],
                                     channels=img_np.shape[2])
            return img_np
        return self._img_np

    @img_np.setter
    def img_np(self, img_np):
        assert img_np is not None
        self._img_np = img_np
        self._img_size = ImgSize(width=img_np.shape[1],
                                 height=img_np.shape[0],
                                 channels=img_np.shape[2])

    @staticmethod
    def from_src(file_src, lazy=False) -> Image:
        '''
        General static method to create object.
        :param file_src: path to image
        :param lazy: if True, object is created but image not loaded right away to save time/memory
        :return:
        '''
        if not os.path.exists((file_src)):
            raise ValueError("File doesn't exist: {}".format(file_src))
        file_size = os.path.getsize(file_src)
        if file_size == 0:
            raise ValueError("Empty file size: {}".format(file_src))
        if lazy:
            img_np = None
        else:
            img_np = ft.img_np_from_disk(file_src)
        return Image(img_np=img_np, img_filename=os.path.basename(file_src), img_src=file_src)

    @staticmethod
    def from_numpy(img_np: np.ndarray, file_name: str = None, file_src=None) -> Image:
        '''
        Instantinates class from numpy array
        :param img_np: numpy image in (w,h,channels) uint8 format
        :param file_name: just image name if available
        :param file_src: path on disk if avalaible
        :return:
        '''
        if img_np.dtype != np.uint8:
            raise ValueError("Image should be uint8! Given: {}".format(img_np.dtype))
        if img_np is None:
            raise ValueError("None value is provided instead of numpy array")
        if len(img_np.shape) != 3:
            raise ValueError("Image shape should be always 3. Given: {}".format(img_np.shape))
        img = Image(img_np=img_np, img_filename=file_name, img_src=file_src)
        return img
