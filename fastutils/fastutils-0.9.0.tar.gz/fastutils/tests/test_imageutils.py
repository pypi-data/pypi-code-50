# -*- coding: utf-8 -*-
import os
import uuid
import random
import unittest
from io import BytesIO
from PIL import ImageGrab
from fastutils.imageutils import get_image_bytes
from fastutils.imageutils import get_base64image
from fastutils.imageutils import parse_base64image
from fastutils.imageutils import resize


class TestImageUtils(unittest.TestCase):

    def test01(self):
        format = "png"
        image = ImageGrab.grab()
        data = get_image_bytes(image, format=format)
        b64image = get_base64image(data, format=format)
        format_new, data_new = parse_base64image(b64image)
        assert format_new == format
        assert data_new == data
