"""
Copyright 2020 Carl Zeiss Microscopy GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import tempfile
from io import BytesIO
from typing import Sequence, Tuple, Union
from zipfile import ZipFile

import tensorflow as tf
from tensorflow.keras import Model

from czmodel.model_metadata import ModelMetadata
from .preprocessing import add_preprocessing_layers


def _zip_directory(directory: str, zip_file: ZipFile) -> None:
    """ Adds an entire directory to a ZipFile.
    Arguments:
        directory: The directory to be added to the zip file.
        zip_file: The zip file to add the directory to.
    """
    # Iterate all the files in directory
    for folder, _, filenames in os.walk(directory):
        for filename in filenames:
            # Determine full path
            full_path = os.path.join(folder, filename)
            # Determine path relative to directory
            rel_path = os.path.relpath(full_path, directory)
            # Add file to zip
            zip_file.write(full_path, arcname=rel_path)


def _create_model_zip(model: Union[str, bytes, memoryview], model_metadata: ModelMetadata, output_path: str) -> None:
    """ Creates a CZModel file from a given ModelMetadata.
    Args:
        model: The Keras model to be packed.
        model_metadata: The meta data describing the CZModel to be generated.
        output_path: The path of the CZModel file to be generated.
    """
    # Append correct extension if necessary
    if not output_path.lower().endswith('.czmodel'):
        output_path = output_path + '.czmodel'

    # Create ZIP file
    with ZipFile(output_path, mode='w') as zf:
        # Write model xml file
        buffer = BytesIO()
        model_metadata.to_xml().write(buffer, encoding='utf-8', xml_declaration=True)
        zf.writestr(str(model_metadata.model_id) + '.xml', buffer.getvalue())
        # Pack and rename proto-buffer file
        arcname = str(model_metadata.model_id) + '.model'
        if isinstance(model, str):
            zf.write(model, arcname=arcname)
        else:
            zf.writestr(arcname, model)
        # Pack license file
        if model_metadata.license_file is not None:
            zf.write(model_metadata.license_file, arcname=os.path.split(model_metadata.license_file)[1])
        # Write empty file with model id
        zf.writestr('modelid=' + str(model_metadata.model_id), '')


def convert(model: Model,
            model_metadata: ModelMetadata,
            output_path: str,
            spatial_dims: Tuple[int, int] = None,
            preprocessing: Union[tf.keras.layers.Layer, Sequence[tf.keras.layers.Layer]] = None) -> None:
    """ Converts a given Keras model to a TensorFlow .pb model optimized for inference.
    Args:
        model: Keras model to be converted. The model must have a separate InputLayer as input node.
        model_metadata: The metadata required to generate a CZModel.
        output_path: Destination path to the .czmodel file that will be generated.
        spatial_dims: Set new spatial dimensions for the input node. This parameter is expected to contain the
            new height and width in that order. Note: Setting this parameter is only possible for models
            that are invariant to the spatial dimensions of the input such as FCNs.
        preprocessing: A sequence of pre-processing layers to be prepended to the model.
            If None is passed no pre-processing is applied.
    """
    if preprocessing is not None or spatial_dims is not None:
        model = add_preprocessing_layers(model=model, layers=preprocessing, spatial_dims=spatial_dims)

    with tempfile.TemporaryDirectory() as tmpdir_name:
        # Export Keras model in SavedModel format
        model.save(tmpdir_name, include_optimizer=False, save_format='tf')
        # Zip saved model
        zip_buffer = BytesIO()
        with ZipFile(zip_buffer, mode='w') as zf:
            _zip_directory(tmpdir_name, zf)
        # Pack model into CZModel
        _create_model_zip(model=zip_buffer.getbuffer(), model_metadata=model_metadata, output_path=output_path)
