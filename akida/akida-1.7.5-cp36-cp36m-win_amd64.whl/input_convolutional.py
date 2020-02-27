from akida.core import (Layer, InputConvolutionalParams,
                        ConvolutionMode, PoolingType, BackendType)
from .parameters_filler import fill_input_conv_params

class InputConvolutional(Layer):
    """The ``InputConvolutional`` layer is an image-specific input layer.

    It is used if images are sent directly to AEE without using the
    event-generating method. If the User applies their own event-generating
    method, the resulting events should be sent to an InputData type layer
    instead.

    The InputConvolutional layer accepts images in 8-bit pixels, either
    grayscale or RGB. Images are converted to events using a combination of
    convolution kernels, activation thresholds and winner-take-all (WTA)
    policies. Note that since the layer input is dense, expect approximately one
    event per pixel – fewer if there are large contrast-free regions in the
    image, such as with the MNIST dataset.

    Note that this format is not appropriate for neuromorphic camera type input
    which data is natively event-based and should be sent to an InputData type
    input layer.

    """

    def __init__(self, name, input_width, input_height, input_channels,
                 kernel_width, kernel_height, num_neurons,
                 convolution_mode=ConvolutionMode.Same, stride_x=1, stride_y=1,
                 weights_bits=1, pooling_width=-1, pooling_height=-1,
                 pooling_type=PoolingType.NoPooling, pooling_stride_x=-1,
                 pooling_stride_y=-1, activations_enabled=True,
                 threshold_fire=0, threshold_fire_step=1, threshold_fire_bits=1,
                 padding_value=0):
        """Create an ``InputConvolutional`` layer from a name and parameters.

        Args:
            name (str): name of the layer.
            input_width (int): input width.
            input_height (int): input height.
            input_channels (int): number of channels of the input image.
            kernel_width (int): convolutional kernel width.
            kernel_height (int): convolutional kernel height.
            num_neurons (int): number of neurons (filters).
            convolution_mode (:obj:`ConvolutionMode`, optional): type of
                convolution.
            stride_x (int, optional): convolution stride X.
            stride_y (int, optional): convolution stride Y.
            weights_bits (int, optional): number of bits used to quantize weights.
            pooling_width (int, optional): pooling window width. If set to -1 it
                will be global.
            pooling_height (int, optional): pooling window height. If set to -1 it
                will be global.
            pooling_type (:obj:`PoolingType`, optional): pooling type
                (None, Max or Average).
            pooling_stride_x (int, optional): pooling stride on x dimension.
            pooling_stride_y (int, optional): pooling stride on y dimension.
            activations_enabled (bool, optional): enable or disable activation
                function.
            threshold_fire (int, optional): threshold for neurons to fire or
                generate an event.
            threshold_fire_step (float, optional): length of the potential
                quantization intervals.
            threshold_fire_bits (int, optional): number of bits used to quantize
                the neuron response.
            padding_value (int, optional): value used when padding

        """
        params = InputConvolutionalParams()
        fill_input_conv_params(params, input_width=input_width,
                               input_height=input_height,
                               input_channels=input_channels,
                               kernel_width=kernel_width,
                               kernel_height=kernel_height,
                               num_neurons=num_neurons,
                               convolution_mode=convolution_mode,
                               stride_x=stride_x,
                               stride_y=stride_y,
                               weights_bits=weights_bits,
                               pooling_width=pooling_width,
                               pooling_height=pooling_height,
                               pooling_type=pooling_type,
                               pooling_stride_x=pooling_stride_x,
                               pooling_stride_y=pooling_stride_y,
                               activations_enabled=activations_enabled,
                               threshold_fire=threshold_fire,
                               threshold_fire_step=threshold_fire_step,
                               threshold_fire_bits=threshold_fire_bits,
                               padding_value=padding_value)

        # Call parent constructor to initialize C++ bindings
        # Note that we invoke directly __init__ instead of using super, as
        # specified in pybind documentation
        Layer.__init__(self, params, name)
