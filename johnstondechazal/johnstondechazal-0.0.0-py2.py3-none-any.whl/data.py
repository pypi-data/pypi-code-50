#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

.. currentmodule:: 

"""
__author__ = 'Ben Johnston'

import json
import os
import tempfile
import urllib.request
from typing import Tuple
from zipfile import ZipFile

import pandas as pd

LANDMARK_REPO = 'https://github.com/doc-E-brown/facial-landmarks/archive/master.zip'

PKG_DIR = os.path.abspath(os.path.dirname(__file__))
LANDMARK_DIR = os.path.join(PKG_DIR, 'facial-landmarks-master')

def download_data(extract_path: str=PKG_DIR) -> None:
    """
    Download facial landmark data from github into
    the package directory

    :param extract_path: The extraction path for the landmark
        data, defaults to the package path.
    :type extract_path: str

    """
    with tempfile.NamedTemporaryFile(mode='w+b') as _zip:
        urllib.request.urlretrieve(LANDMARK_REPO, _zip.name)
        _zip.seek(0)

        with ZipFile(_zip.name) as _zip_contents:
            _zip_contents.extractall(extract_path)

def _json_to_landmarks(input_json: dict) -> Tuple[str, Tuple[int, int]]:
    """Convert json to landmarks for DataFrame"""

    _id = int(input_json["id"][1:])
    return (_id, (input_json['user_x'], input_json['user_y']))


def json_landmarks_to_dataframe(filepath: str) -> Tuple[str, pd.DataFrame]:
    """ Load landmarks from a json file as pandas Dataframe """

    with open(filepath, 'r') as f:
        data = json.load(f)

    # Check if this is a MTURK or expert result
    if 'WorkerId' in data.keys():
        worker = data['WorkerId']
        data = data['Answers'][1]['FreeText']
        data = json.loads(data)

    # expert result
    else:
        worker = os.path.splitext(os.path.basename(filepath))[0]
        data = data['results']

    data_frame = {'filename': [], 'workerid': []}

    for samp in data['samples']:
        data_frame['filename'].append(os.path.basename(samp['filename']))
        data_frame['workerid'].append(worker)
        for lmrk in samp['landmarks']:
            _id, *coords = _json_to_landmarks(lmrk)

            if _id in data_frame:
                data_frame[_id].append(coords[0])
            else:
                data_frame[_id] = coords

    return pd.DataFrame.from_dict(data_frame) 
