from akida.core import Layer, InputDataParams, BackendType
from .parameters_filler import fill_input_data_params

class InputData(Layer):
    """This is the general purpose input layer. It takes events in a simple
    address-event data format; that is, each event is characterized by a trio
    of values giving x, y and feature values. The ``InputData`` layer can simply
    pass them to the rest of the model for processing or group the generated
    events into packets (packetizing option).

    Packetizing feature is mainly relevant when the events are produced as a
    continuous stream, and not already grouped in frames. When fed with a stream
    of data, packetizing will take events in the received order until a
    predefined packet_size is reached, and then the packet is sent for
    processing. If the stream ends on an incomplete packet, the layer can either
    send an incomplete packet or wait for the next call stream of events to
    resume its processing. With that configurable behaviour, the InputData layer
    can handle both small and large numbers of events at a time; small numbers,
    will be accumulated until the packet is filled, and then sent. Large numbers
    will be subdivided into multiple packets.

    Regarding the input dimension values, note that AEE expects inputs with
    zero-based indexing, i.e., if input_width is defined as 12, then the model
    expects all input events to have x-values in the range 0–11.
    The input_features dimension is simply a third input dimension, e.g.,
    certain DVS cameras generate events with x- and y-pixel values, but also
    with an event polarity, that is: on for increasing luminance, or off for
    decreasing luminance. In which case, the features-dimension would be used to
    encode the polarity and would be defined with size 2.

    Where possible:

    - The x and y dimensions should be used for discretely-sampled continuous
      domains such as space (e.g., images) or time-series (e.g., an audio
      signal).

    - The f dimension should be used for ‘category indices’, where there is no
      particular relationship between neighboring values.

    The important distinction in neural networks targeting the Akida NSoC is
    that convolutional layers are limited to performing the stride of the
    convolution in the x- and y-dimensions. Convolution across the f dimension
    is not supported. The input dimension values are used for:

    - Error checking – input events are checked and if any fall outside the
      defined input range, then the whole set of events sent on that
      processing call is rejected. An error will also be generated if the
      defined values are larger than the true input dimensions.

    - Configuring the input and output dimensions of subsequent layers in the
      model.

    """

    def __init__(self, name, input_width, input_height, input_features,
                 packet_size=0, accumulate=False):
        """Create an ``InputData`` layer from a name and parameters.

        Args:
            name (str): name of the layer.
            input_width (int): input width.
            input_height (int): input height.
            input_features (int): size of the third input dimension.
            packet_size (int, optional): size of a packet.
            accumulate (bool, optional): defines if the layer maintains its
                packetizing buffer when dealing with an incomplete packet.

        """
        params = InputDataParams()
        fill_input_data_params(params, input_width=input_width,
                               input_height=input_height,
                               input_features=input_features,
                               packet_size=packet_size,
                               accumulate=accumulate)

        # Call parent constructor to initialize C++ bindings
        # Note that we invoke directly __init__ instead of using super, as
        # specified in pybind documentation
        Layer.__init__(self, params, name)
