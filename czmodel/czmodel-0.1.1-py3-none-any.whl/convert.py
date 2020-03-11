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

This module provides conversion functions to generate a CZModel from exported TensorFlow models.
"""
import os

from tensorflow.keras import Model
from tensorflow.keras.models import load_model

from .model_metadata import ModelSpec
from .util import keras_to_czmodel
from .util.argument_parsing import dir_file

from typing import Tuple, Union, Sequence


def convert_from_model_spec(model_spec: ModelSpec,
                            output_path: str,
                            output_name: str = 'DNNModel',
                            spatial_dims: Tuple[int, int] = None,
                            preprocessing: Union['tensorflow.keras.layers.Layer', Sequence[
                                'tensorflow.keras.layers.Layer']] = None) -> None:
    """ Converts a TensorFlow .pb or TensorFlow Keras model specified in a ModelMetadata instance to a CZModel that is
    usable in ZEN Intellesis.
    Args:
        model_spec: A ModelSepc object describing the specification of the CZModel to be generated.
        output_path: A folder to store the generated CZModel file.
        output_name: The name of the generated .czmodel file.
        spatial_dims: Set new spatial dimensions for the input node. This parameter is expected to contain the
            new height and width in that order. Note: Setting this parameter is only possible for models
            that are invariant to the spatial dimensions of the input such as FCNs.
        preprocessing: A sequence of pre-processing layers to be prepended to the model.
            If None is passed no pre-processing is applied.
    """
    # Create output directory
    os.makedirs(output_path, exist_ok=True)

    # Load model if necessary
    model = model_spec.model if isinstance(model_spec.model, Model) else load_model(model_spec.model)

    # Convert model
    keras_to_czmodel.convert(model=model,
                             model_metadata=model_spec.model_metadata,
                             output_path=os.path.join(output_path, output_name),
                             spatial_dims=spatial_dims,
                             preprocessing=preprocessing)


def convert_from_json_spec(model_spec_path: str,
                           output_path: str,
                           output_name: str = 'DNNModel',
                           spatial_dims: Tuple[int, int] = None,
                           preprocessing: Union['tensorflow.keras.layers.Layer', Sequence[
                               'tensorflow.keras.layers.Layer']] = None) -> None:
    """ Converts a TensorFlow .pb model specified in a JSON metadata file to a CZModel that is usable in ZEN Intellesis.
    Args:
        model_spec_path: The path to the JSON specification file.
        output_path: A folder to store the generated CZModel file.
        output_name: The name of the generated .czmodel file.
        spatial_dims: Set new spatial dimensions for the input node. This parameter is expected to contain the
            new height and width in that order. Note: Setting this parameter is only possible for models
            that are invariant to the spatial dimensions of the input such as FCNs.
        preprocessing: A sequence of pre-processing layers to be prepended to the model.
            If None is passed no pre-processing is applied.
    """

    # Parse the specification JSON file
    parsed_spec = ModelSpec.from_json(model_spec_path)

    # Write CZModel to disk
    convert_from_model_spec(parsed_spec,
                            output_path,
                            output_name,
                            spatial_dims=spatial_dims,
                            preprocessing=preprocessing)


def main():
    """
    Console script to convert a TensorFlow proto-buffer to a CZModel.
    """
    # Import argument parser
    import argparse

    # Define expected arguments
    parser = argparse.ArgumentParser(
        description='Convert a TensorFlow proto-buffer to a CZModel that can be executed inside ZEN.')
    parser.add_argument('model_spec', type=dir_file, help='A JSON file containing the model specification.')
    parser.add_argument('output_path', type=str, help='The path where the generated CZModel will be created.')
    parser.add_argument('output_name', type=str, help='The name of the generated CZModel.')

    # Parse arguments
    args = parser.parse_args()

    # Run conversion
    convert_from_json_spec(args.model_spec, args.output_path, args.output_name)


if __name__ == '__main__':
    main()