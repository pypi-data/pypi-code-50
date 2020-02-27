import numpy as np
import yaml
import os
import warnings

from . import (Sparse, Dense, BackendType, ConvolutionMode, PoolingType,
               LearningType, InputData, InputConvolutional, InputBCSpike,
               FullyConnected, Convolutional, SeparableConvolutional)
from .core import ModelBase, Layer, LayerType
from .parameters_serializer import (deserialize_parameters,
                                    serialize_learning_type)
from .layer_statistics import LayerStatistics
from .observer import Observer

class Model(ModelBase):
    """An Akida neural ``Model``, represented as a hierarchy of layers.

    The ``Model`` class is the main interface to Akida.

    It provides methods to instantiate, train, test and save models.

    """

    def __init__(self, filename = None, backend = BackendType.Software):
        """
        Creates an empty ``Model``, a ``Model`` template from a YAML file,
        or a full ``Model`` from a serialized file.

        Args:
            filename (str, optional): path of the YAML file containing the model
                architecture, or a serialized Model.
                If None, an empty sequential model will be created.
            backend (:obj:`BackendType`, optional): backend to run the model on.

        """
        try:
            if filename is not None:
                # get file extension
                extension = os.path.splitext(filename)[1].lower()
                if extension == ".yml" or extension == ".yaml":
                    ModelBase.__init__(self, backend)
                    self._build_model(filename)
                else:
                    ModelBase.__init__(self, filename, backend)
            else:
                ModelBase.__init__(self, backend)
        except:
            self = None
            raise

    def __repr__(self):
        data = "<akida.Model, layer_count=" + str(self.get_layer_count())
        data += ", output_dims=" + str(self.output_dims)
        data += ", backend_type=" + str(self.get_backend_type()) + ">"
        return data

    def get_statistics(self):
        """Get statistics by layer for this network.

        Returns:
            a dictionary of obj:`LayerStatistics` indexed by layer_name.

        """
        self._layers_stats = {}
        for i in range(self.get_layer_count()):
            layer = self.get_layer(i)
            self._layers_stats[layer.name] = self.get_layer_statistics(layer)
        return self._layers_stats

    def _check_hardware_compatibility(self, layer_index):
        """Checks a layer compatibility with hardware.

        This method performs parameters value checking for hardware
        compatibility and returns incompatibility messages when needed.
        Hardware compatibility can be seen by calling the summary() method.

        Args:
            layer_index (int): the layer index.

        """
        def full_message(layer_name, msg_list):

            if len(msg_list):
                return str("Layer " + layer_name + " is not compatible with "
                           "hardware: \n" + "\n".join(msg_list))
            else:
                return str()

        layer = self.get_layer(layer_index)
        hw_msg = []
        # inputData layer
        if layer.parameters.layer_type == LayerType.InputData:
            return str()

        if layer.parameters.activations_params.threshold_fire_bits not in [1, 2, 4]:
            hw_msg.append("- unsupported threshold_fire_bits, supported "
                          "values are [1, 2, 4], currently at " +
                          str(layer.parameters.activations_params.threshold_fire_bits))

        if layer.parameters.activations_params.threshold_fire not in range(-2**19, 2**19):
            hw_msg.append(
                "- unsupported threshold_fire, it must fit in 20 bits")

        # fullyConnected layer
        if layer.parameters.layer_type == LayerType.FullyConnected:
            if layer.parameters.weights_bits not in [1, 2, 3, 4]:
                hw_msg.append("- weights_bits must be in [1, 2, 3, 4], "
                              "currently at " +
                              str(layer.parameters.weights_bits))
            if layer_index > 0:
                previous_params = self.get_layer(layer_index - 1).parameters
                if "threshold_fire_bits" in dir(previous_params):
                    if previous_params.threshold_fire_bits not in [1, 2]:
                        hw_msg.append("- unsupported input dimensions. "
                                      "threshold_fire_bits in previous layer "
                                      "must be in [1, 2], currently at " +
                                      str(previous_params.threshold_fire_bits))
            return full_message(layer.name, hw_msg)

        # define aliases for readbility
        kw = layer.parameters.kernel_width
        kh = layer.parameters.kernel_height
        pw = layer.parameters.pooling_width
        ph = layer.parameters.pooling_height
        psx = layer.parameters.pooling_stride_x
        psy = layer.parameters.pooling_stride_y

        # inputConvolutional layer
        if layer.parameters.layer_type == LayerType.InputConvolutional:
            sx = layer.parameters.stride_x
            sy = layer.parameters.stride_y

            if kw != kh:
                hw_msg.append("- kernel_width and kernel_height must be "
                              "equal, currently at " + str(kw) + " and "
                              + str(kh))
            if kw not in [3, 5, 7]:
                hw_msg.append("- kernel_width must be in [3, 5, 7], "
                              "currently at " + str(kw))
            if sx != sy:
                hw_msg.append("- stride_x and stride_y must be equal, "
                                "currently at " + str(sx) + " and " +
                                str(sy))
            if sx not in [1, 2, 3]:
                hw_msg.append("- stride_x must be in [1, 2, 3], "
                                "currently at " + str(sx))
            if (layer.parameters.convolution_mode not in
                    [ConvolutionMode.Same, ConvolutionMode.Valid]):
                hw_msg.append("- convolution_mode must be "
                              "ConvolutionMode.Same or "
                              "ConvolutionMode.Valid")
            if layer.parameters.pooling_type == PoolingType.Max:
                if pw not in [1, 2]:
                    hw_msg.append("- pooling_height must be in [1, 2], "
                                    "currently at " + str(pw))
                if ph not in [1, 2]:
                    hw_msg.append("- pooling_width must be in [2, 3], "
                                    "currently at " + str(pw))
                if psx != psy:
                    hw_msg.append("- pooling_stride_x and pooling_stride_y "
                                  "must be equal, currently at " + str(psx) +
                                  " and " + str(psy))
                if psx != 2 :
                    hw_msg.append("- pooling_stride_x must be 2, currently at "
                                  + str(sx))
            elif layer.parameters.pooling_type == PoolingType.Average:
                hw_msg.append("- average pooling_type not supported")
        # convolutional layers
        elif (layer.parameters.layer_type in
                [LayerType.Convolutional, LayerType.SeparableConvolutional]):
            wb = layer.parameters.weights_bits

            if kw != kh:
                hw_msg.append("- kernel_width and kernel_height must be "
                                "equal, currently at " + str(kw) + " and "
                                 + str(kh))
            if layer.parameters.convolution_mode != ConvolutionMode.Same:
                hw_msg.append("convolution_mode must be ConvolutionMode.Same")
            if layer.parameters.pooling_type == PoolingType.Max:
                # Max pooling forbidden if it is not followed by an other CNP
                if (layer_index == self.get_layer_count() - 1
                or self.get_layer(layer_index + 1).parameters.layer_type
                  not in [LayerType.Convolutional, LayerType.SeparableConvolutional]):
                    hw_msg.append("- max pooling on convolutional or separable"
                    " convolutional layer must be followed by another"
                    " convolutional or separable convolutional layer")
                if pw != ph:
                    hw_msg.append("- pooling_width and pooling_height must "
                                  "be equal, currently at " + str(pw) +
                                  " and " + str(ph))
                if pw not in [2, 3]:
                    hw_msg.append("- pooling_width must be in [2, 3], "
                                  "currently at " + str(pw))
                if psx != psy:
                     hw_msg.append("- pooling_stride_x and pooling_stride_y"
                                   " must be equal, currently at "
                                   + str(psx) + " and " + str(psy))
                if pw == 2 and psx not in [1, 2]:
                    hw_msg.append("- pooling_stride_x must be in [1, 2] "
                                  "for 2x2 pooling, currently at "
                                  + str(psx))
                if pw == 3 and psx not in [1, 2, 3]:
                    hw_msg.append("- pooling_stride_x must be in [1, 2, 3] "
                                  "for 3x3 pooling, currently at "
                                  + str(psx))
            elif layer.parameters.pooling_type == PoolingType.Average:
                if pw != -1 and ph != -1:
                     hw_msg.append("- only global average pooling is supported:"
                                   " pooling_width and pooling height must be "
                                   "set to -1 (default)")
            if layer.parameters.layer_type == LayerType.SeparableConvolutional:
                if kw not in [3, 5, 7]:
                    hw_msg.append("- kernel_width must be in [3, 5, 7], "
                                  "currently at " + str(kw))
                if wb not in [2, 4]:
                    hw_msg.append("- weights_bits must be in [2, 4], "
                                  "currently at "
                                  + str(wb))
            elif layer.parameters.layer_type == LayerType.Convolutional:
                if kw not in [1, 3, 5, 7]:
                    hw_msg.append("- kernel_width must be in [1, 3, 5, 7], "
                                  "currently at " + str(kw))
                if wb not in [1, 2]:
                    hw_msg.append("- weights_bits must be in [1, 2], "
                                  "currently at " + str(wb))
        return full_message(layer.name, hw_msg)

    def _build_model(self, filename):
        """Builds a model from a YAML description file of the layers.

        Args:
            filename (str): path of the YAML file containing the model
                architecture, or a serialized Model.

        """
        # test whether the yml file can be found
        if not os.path.isfile(filename):
            raise ValueError("The ymlfile ({}) could not be found, "
                             "instance not initialised".format(filename))
        # load the file
        yaml_content = yaml.load(open(filename), Loader=yaml.FullLoader)

        if "Layers" not in yaml_content:
            raise ValueError(
                "Invalid model configuration: missing 'Layers' section.")

        layers = yaml_content["Layers"]
        if len(layers) == 0:
            raise ValueError("Empty model configuration.")

        # build and add layers to the model
        for layer_description in layers:
            name = layer_description["Name"]

            # deserialize YAML into a kwargs dict for the layer
            if "Parameters" not in layer_description:
               raise ValueError("Invalid model configuration: "
                                "missing 'Parameters' section in layer " + name)
            type, params_dict = deserialize_parameters(
                layer_description["Parameters"])

            # create a layer object from the dict
            layer = None
            if type == "inputData":
                layer = InputData(name, **params_dict)
            elif type == "inputConvolutional":
                layer = InputConvolutional(name, **params_dict)
            elif type == "inputBCSpike":
                layer = InputBCSpike(name, **params_dict)
            elif type == "fullyConnected":
                layer = FullyConnected(name, **params_dict)
            elif type == "convolutional":
                layer = Convolutional(name, **params_dict)
            elif type == "separableConvolutional":
                layer = SeparableConvolutional(name, **params_dict)
            elif type == "depthwiseConvolutional":
                warnings.warn("depthwiseConvolutional layer name is deprecated,"
                              " please use separableConvolutional instead.")
                layer = SeparableConvolutional(name, **params_dict)
            elif type == str():
                raise ValueError("Invalid model configuration: missing"
                                 " 'layerType' parameter in layer " + name)
            else:
                raise ValueError("Invalid model configuration, unknown"
                                 " layerType " + type + " in layer " + name)

            # add the layer
            self.add(layer)

    def predict(self, input, num_classes=None):
        """Returns the model class predictions.

        Forwards input data (images or events) through the model and compute
        predictions based on the neuron id.
        If the number of output neurons is greater than the number of classes,
        the neurons are automatically assigned to a class by dividing their id
        by the number of classes.

        Note that the predictions are based on the spike values of the last
        layer: for most use cases, you may want to disable activations for that
        layer (ie setting ``activations_enabled=False``) to get a better
        accuracy.

        Args:
            input (:obj:`Sparse`,`numpy.ndarray`): a Sparse object of
                shape (w, h, f) containing the events, or a numpy.ndarray of
                shape (n, h, w, c) containing the n images.
                (grayscale (c=1) or RGB (c=3))
            num_classes (int, optional): optional parameter (defaults to the
                number of neurons in the last layer).

        Returns:
            :obj:`numpy.ndarray`: an array of shape (n).

        """
        if num_classes is None:
            w, h, f = self.output_dims
            num_classes = f

        if isinstance(input, np.ndarray):
            if input.flags['C_CONTIGUOUS']:
                dense = Dense(input)
            else:
                dense = Dense(np.ascontiguousarray(input))
            labels = super(Model, self).predict(dense, num_classes)
        elif isinstance(input, Sparse):
            labels = super(Model, self).predict(input, num_classes)
        else:
            raise TypeError("predict expects Sparse or numpy array as input")
        return labels

    def fit(self, input, input_labels=None):
        """Trains a set of images or events through the model.

        Trains input data (images or events) through the model and returns
        the outputs, including spike values.

        Args:
            input (:obj:`Sparse`,`numpy.ndarray`): a Sparse object of shape
                (w, h, f) containing the events, or a numpy.ndarray of
                shape (n, h, w, c) containing the n images.
                (grayscale (c=1) or RGB (c=3))
            input_labels (list(int), optional): input labels.
                Must have one label per input, or a single label for all inputs.
                If a label exceeds the defined number of classes, the input will
                be discarded. (Default value = None).

        Returns:
           :obj:`Sparse`: a sparse tensor of shape (n, x, y, f).

        Raises:
            TypeError: if the input doesn't have the correct type
                (Sparse, numpy.ndarray).
            ValueError: if the input doesn't match the required shape,
                format, etc.

        """
        if input_labels is None:
            input_labels = []
        elif isinstance(input_labels, int):
            input_labels = [input_labels]
        if (not isinstance(input_labels, list)
            and not isinstance(input_labels, np.ndarray)):
            raise TypeError("fit expects list, numpy array or an int as labels")
        if isinstance(input, Sparse):
            return super(Model, self).fit(input, input_labels)
        elif isinstance(input, np.ndarray):
            if input.flags['C_CONTIGUOUS']:
                dense = Dense(input)
            else:
                dense = Dense(np.ascontiguousarray(input))
            spikes = super(Model, self).fit(dense, input_labels)
        else:
            raise TypeError("fit expects Sparse or numpy array as input")
        return spikes

    def forward(self, input):
        """Forwards a set of images or events through the model.

        Forwards input data (images or events) through the model and returns
        the outputs, including spike values.

        Args:
            input (:obj:`Sparse`,`numpy.ndarray`): a Sparse object of shape
                (w, h, f) containing the events, or a numpy.ndarray of
                shape (n, h, w, c) containing the n images.
                (grayscale (c=1) or RGB (c=3))

        Returns:
           :obj:`Sparse`: a sparse tensor of shape (n, x, y, f).

        Raises:
            TypeError: if the input doesn't have the correct type
                (Sparse, numpy.ndarray).
            ValueError: if the input doesn't match the required shape,
                format, etc.

        """
        if isinstance(input, Sparse):
            return super(Model, self).forward(input)
        elif isinstance(input, np.ndarray):
            if input.flags['C_CONTIGUOUS']:
                dense = Dense(input)
            else:
                dense = Dense(np.ascontiguousarray(input))
            spikes = super(Model, self).forward(dense)
        else:
            raise TypeError("forward expects Sparse or numpy array as input")
        return spikes

    def evaluate(self, input):
        """Evaluates a set of images or events propagation through the model.

        This method propagates a set of events through the model and returns the
        results in the form of a numpy array of float values.
        It applies ONLY on models whithout an activation on the last layer.
        The output values are obtained from the model discrete potentials by
        applying a shift and a scale.

        Args:
            input (:obj:`Sparse`,`numpy.ndarray`): a Sparse object of shape
                (w, h, f) containing the events, or a numpy.ndarray of
                shape (n, h, w, c) containing the n images.
                (grayscale (c=1) or RGB (c=3))

        Returns:
           :obj:`numpy.ndarray`: an array of shape (n, w, h, c).

        Raises:
            TypeError: if the input doesn't have the correct type
                (Sparse, numpy.ndarray).
            RuntimeError: if the model last layer has an activation.
            ValueError: if the input doesn't match the required shape,
                format, or if the model only has an InputData layer.

        """
        if isinstance(input, Sparse):
            outputs = super(Model, self).evaluate(input)
        elif isinstance(input, np.ndarray):
            if input.flags['C_CONTIGUOUS']:
                dense = Dense(input)
            else:
                dense = Dense(np.ascontiguousarray(input))
            outputs = super(Model, self).evaluate(dense)
        else:
            raise TypeError("forward expects Sparse or numpy array as input")
        return outputs.to_numpy()

    def summary(self):
        """Prints a string summary of the model.

        This method prints a summary of the model with details for every layer:

        - name and type in the first column
        - hardware compatibility in the 'HW' column. When the layer is not
          compatible, a list of incompatibilities is given below the summary.
        - input shape
        - output shape
        - kernel shape
        - learning type and number of classes
        - a group of 3 metrics to check for training configuration: number of
          input connections (#InConn) is the input space (or kernel space for
          convolutional layers) for the weights. The number of weights (#Weights)
          is given to check that it is well below the number of input connections
          and threshold fire (ThFire) must be less that the number of weights.

        """
        # Formating of the table
        first_col_width = 23
        hw_col_width = 4
        col_width = 14
        last_col_width = 26
        headers = ['Layer (type)', 'HW', 'Input shape', 'Output shape',
        'Kernel shape', 'Learning (#classes)', '#InConn/#Weights/ThFire']
        simple_sep = "-" * (first_col_width + hw_col_width +
                            col_width * (len(headers) - 4) + 2 * last_col_width)
        double_sep = "=" * (first_col_width + hw_col_width +
                            col_width * (len(headers) - 4) + 2 * last_col_width)
        hardware_compatibility = []

        # Data formating nested function
        def get_column_data(data, col_width):
            """Adds data to the current line string and crop or fill to reach
            column width.

            Args:
                data: data to add.
                col_width (int): column width.

            """
            if len(data) > col_width - 1:
                formatted_data = data[:col_width - 1] + ' '
            else:
                formatted_data = data + ' ' * (col_width-len(data))

            return formatted_data

        # Line printing nested function
        def print_layer(index):
            """Prints a summary line for a given layer.

            Args:
                index (int): index of the Layer.

            """
            layer = self.get_layer(index)
            params_names = dir(layer.parameters)

            # layer name (type)
            current_line = get_column_data("{} ({})".format(
                layer.name, str(layer.parameters.layer_type).split(".")[-1]),
                first_col_width)

            # hardware compatible
            incompatiblities = self._check_hardware_compatibility(index)
            if incompatiblities:
                current_line += get_column_data("no", hw_col_width)
                hardware_compatibility.append(incompatiblities)
            else:
                current_line += get_column_data("yes", hw_col_width)

            # input shape
            input_dims = layer.input_dims
            num_filters = input_dims[-1]
            current_line += get_column_data(str(input_dims), col_width)

            # output shape
            current_line += get_column_data(str(layer.output_dims), col_width)

            # kernel shape
            if ("kernel_width" in params_names and
                    "kernel_height" in params_names):
                kw = layer.parameters.kernel_width
                kh = layer.parameters.kernel_height
                kernel_data = f"({kw} x {kh} x {num_filters})"
                input_connections = str(kw * kh * num_filters)
            else:
                kernel_data = "N/A"
                input_connections = "N/A"
            current_line += get_column_data(kernel_data, col_width)

            # learning type (#classes)
            if layer.learning is not None:
                learning_type = serialize_learning_type(
                    layer.learning.learning_type)
            else:
                learning_type = "N/A"
            if layer.learning is not None and layer.learning.num_classes > 1:
                current_line += get_column_data(f"{learning_type} " +
                                                f"({layer.learning.num_classes})",
                                                last_col_width)
            else:
                current_line += get_column_data(
                    f"{learning_type}", last_col_width)

            # input connections
            if(layer.parameters.layer_type == LayerType.FullyConnected):
                input_connections = str(
                    input_dims[0] * input_dims[1] * input_dims[2])

            # weights
            if ("weights" in layer.get_variable_names()):
                num_weights_data = np.count_nonzero(
                    layer.get_variable("weights"))
                num_neurons = layer.parameters.num_neurons
                if ("weights_pw" in layer.get_variable_names()):
                    num_weights_data += np.count_nonzero(
                        layer.get_variable("weights_pw"))
                    num_neurons += layer.parameters.num_pointwise_neurons
                num_weights_data //= num_neurons
            else:
                num_weights_data = "N/A"

            # threshold fire
            if "activations_params" in params_names:
                th_fire_data = str(
                    layer.parameters.activations_params.threshold_fire)
            else:
                th_fire_data = "N/A"

            current_line += get_column_data(f"{input_connections} / " +
                                            f"{str(num_weights_data)} / " +
                                            f"{th_fire_data}", last_col_width)

            print(current_line)
            print(simple_sep)

        # header
        print(simple_sep)
        current_line = get_column_data(headers[0], first_col_width)
        current_line += get_column_data(headers[1], hw_col_width)
        for h in headers[2:-2]:
            current_line += get_column_data(h, col_width)
        current_line += get_column_data(headers[-2], last_col_width)
        current_line += get_column_data(headers[-1], last_col_width)
        print(current_line)
        print(double_sep)

        #layers
        for i in range(self.get_layer_count()):
            print_layer(i)

        if len(hardware_compatibility):
            if len(hardware_compatibility) == 1:
                print("\nHardware incompatibility:\n")
            else:
                print("\nHardware incompatibilities:\n")

            print("\n".join(hardware_compatibility))

    def get_observer(self, layer):
        """Get the Observer object attached to the specified layer.

        Observers are containers attached to a ``Layer`` that allows to
        retrieve layer output spikes and potentials.

        Args:
            layer (:obj:`Layer`): the layer you want to observe.
        Returns:
            :obj:`Observer`: the observer attached to the layer.

        """
        return Observer(self, layer)


    def get_layer_statistics(self, layer):
        """Get the LayerStatistics object attached to the specified layer.

        LayerStatistics are containers attached to an akida.Layer that allows to
        retrieve layer statistics:

            (average sparsity, number of operations and number of possible
            spikes, row_sparsity).

        Args:
            layer (:obj:'Layer'): layer where you want to obtain the ``LayerStatistics`` object.

        Returns:
            a ``LayerStatistics`` object.

        """
        prev_layer = None
        for i in range(1, self.get_layer_count()):
            if self.get_layer(i).name == layer.name:
                prev_layer = self.get_layer(i - 1)
                break

        return LayerStatistics(self, layer, prev_layer)

