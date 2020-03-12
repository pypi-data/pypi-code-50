import torch


class RNNLayer(torch.nn.Module[torch.Tensor]):
    """
    RNN layer is a ``Module`` that is the same as default rnn pytorch layers,
    but registrable and has ``get_output_dim`` method
    """

    def get_output_dim(self) -> int:
        """
        Returns output dim based on input data
        """
        raise NotImplementedError
