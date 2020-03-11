import itertools as it
from multiprocessing.pool import ThreadPool
from queue import Queue

import numpy as np

from . import Decoder
from . import CudaTensor
from . import array_to_tensor
from . import uint8
from . import float32
from . import make_transform
from . import warp_affine
from . import add_gamma
from . import AUGPY_TO_NUMPY_DTYPES


class DecodeWarp(object):
    def __init__(
            self, batch_size, shape,
            background=None,
            dtype=uint8,
            cpu_threads=1,
            num_buffers=2,
            decode_buffer_size=None,
    ):
        self.batch_size = batch_size
        self.shape = shape
        # create num_buffers batch buffer tensors
        self.buffers = [CudaTensor((batch_size,)+tuple(shape), dtype=dtype)
                        for _ in range(num_buffers)]
        self._buffer_queue = Queue()
        for b in self.buffers:
            b.fill(0)
            self._buffer_queue.put(b)
        # create background tensor
        if background is None:
            background = (0,) * shape[0]
        self.background = array_to_tensor(np.array(background, dtype=AUGPY_TO_NUMPY_DTYPES[dtype]))
        # create buffers and decoders as necessary
        decode_buffers = [
            CudaTensor((decode_buffer_size * dtype.itemsize,), dtype=uint8)
            if decode_buffer_size else None
            for _ in range(cpu_threads)
        ]
        decoders = [Decoder() for _ in range(cpu_threads)]
        self._decoder_queue = Queue()
        for d, b in zip(decoders, decode_buffers):
            self._decoder_queue.put((d, b))
        # thread pool for decoding
        self._pool = ThreadPool(cpu_threads)

    def _decode_warp(self, args):
        i, imdata, augmentation, buffer = args
        decoder, decode_buffer = self._decoder_queue.get()
        try:
            im = decoder.decode(imdata, decode_buffer)
            m, s = make_transform(im.shape[:-1], self.shape[1:], **augmentation)
            warp_affine(im, buffer[i], m, self.background, s)
        finally:
            self._decoder_queue.put((decoder, decode_buffer))

    def __call__(self, batch):
        buffer = self._buffer_queue.get()
        self._pool.map(
            self._decode_warp,
            zip(range(self.batch_size), batch['image'], batch['augmentation'], it.cycle((buffer,)))
        )
        batch['image'] = buffer
        return batch

    def finalize_batch(self, buffer):
        self._buffer_queue.put(buffer)


class Lighting(object):
    def __init__(self, batch_size, channels=3, max_value=255):
        self.batch_size = batch_size
        self.channels = channels
        self.max_value = max_value
        self._param_buffer = CudaTensor((batch_size * (channels + 2),), dtype=float32)
        self.gray_buffer = self._param_buffer[:batch_size]
        self.contrast_buffer = self._param_buffer[batch_size:batch_size+batch_size]
        self.color_buffer = self._param_buffer[batch_size+batch_size:]

    def __call__(self, batch):
        # copy params to GPU buffer
        augmentation = batch['augmentation']
        params = [a.get('gamma_gray') or 1.0 for a in augmentation] \
            + [a.get('contrast') or 0.0 for a in augmentation]
        default_color = (1,) * self.channels
        for a in augmentation:
            params.extend(a.get('gamma_color') or default_color)
        array_to_tensor(np.array(params, dtype=np.float32), self._param_buffer)

        # apply lighting to batch
        tensor = batch['image']
        add_gamma(
            tensor,
            self.gray_buffer,
            self.color_buffer,
            self.contrast_buffer,
            self.max_value,
            tensor
        )
        return batch
