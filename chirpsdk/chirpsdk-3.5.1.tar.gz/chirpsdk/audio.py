# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------
#
#  This file is part of the Chirp Python SDK.
#  For full information on usage and licensing, see https://chirp.io/
#
#  Copyright (c) 2011-2019, Asio Ltd.
#  All rights reserved.
#
# ------------------------------------------------------------------------

import time
import threading

try:
    from queue import Queue
except ImportError:  # python2
    from Queue import Queue

import sounddevice as sd

from .exceptions import ChirpSDKAudioError


class Audio(object):
    """ Chirp SDK Audio I/O. """

    def __init__(self, sdk):
        self.sdk = sdk
        self.processing = None
        self.input_stream = None
        self.output_stream = None

        self.output_channels = 1
        self.wav_filename = None
        self.sample_size = 'float32'
        self.block_size = 4096

        if self.sample_size == 'float32':
            self.sample_format = 'f'
            self.process_input_fn = self.sdk.process_input
            self.process_output_fn = self.sdk.process_output
        elif self.sample_size == 'int16':
            self.sample_format = 'h'
            self.process_input_fn = self.sdk.process_shorts_input
            self.process_output_fn = self.sdk.process_shorts_output
        else:
            raise ChirpSDKAudioError(
                'Invalid audio format: %s. Only float32 and int16 are supported' %
                self.sample_size)

    def start(self, send=True, receive=True):
        """
        Start audio I/O stream and processing thread.

        Args:
            send (bool): Enable output audio processing. True by default
            receive (bool): Enable input audio processing. True by default

        Raises:
            Exception: if invalid sample rate is used in the Chirp SDK.

        """
        if receive:
            sd.check_input_settings(
                device=self.input_device, channels=1,
                dtype=self.sample_size, samplerate=self.sdk.input_sample_rate,
            )
            self.processing = AudioProcessingThread(parent=self)
            self.input_stream = sd.RawInputStream(
                device=self.input_device,
                channels=1,
                samplerate=int(self.sdk.input_sample_rate),
                dtype=self.sample_size,
                blocksize=self.block_size,
                callback=self.process_input,
            )
            self.input_stream.start()
        if send:
            sd.check_output_settings(
                device=self.output_device, channels=self.output_channels,
                dtype=self.sample_size, samplerate=self.sdk.output_sample_rate,
            )
            self.output_stream = sd.RawOutputStream(
                device=self.output_device,
                channels=self.output_channels,
                samplerate=int(self.sdk.output_sample_rate),
                dtype=self.sample_size,
                blocksize=self.block_size,
                callback=self.process_output,
            )
            self.output_stream.start()

    def stop(self):
        if self.processing:
            self.processing.stop()
        if self.input_stream:
            self.input_stream.stop()
            self.input_stream.close()
        if self.output_stream:
            self.output_stream.stop()
            self.output_stream.close()

    def process_input(self, indata, frames, time, status):
        """ Process input audio data - receive only audio callback. """
        self.processing.input_queue.put(bytes(indata))

    def process_output(self, outdata, frames, time, status):
        """ Process output audio data - send only audio callback. """
        self.process_output_fn(outdata)

    def query_devices(self):
        """ Return info about available devices. """
        return sd.query_devices()

    @property
    def input_device(self):
        return sd.default.device[0]

    @input_device.setter
    def input_device(self, index):
        sd.default.device[0] = index

    @property
    def output_device(self):
        return sd.default.device[1]

    @output_device.setter
    def output_device(self, index):
        sd.default.device[1] = index


class AudioProcessingThread(threading.Thread):
    """ Chirp SDK audio processing thread. """

    debug_audio_filename = 'chirp_audio.wav'

    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialise audio processing.

        In debug mode, the audio data is saved to file.
        """
        self.sdk = parent.sdk
        self.sample_size = parent.sample_size
        self.sample_length = 2 if self.sample_size == 'int16' else 4
        self.process_input_fn = parent.process_input_fn
        self.sample_rate = float(parent.sdk.input_sample_rate)
        self.block_period = parent.block_size / self.sample_rate

        self.input_queue = Queue()
        self.wav_filename = parent.wav_filename or self.debug_audio_filename
        super(AudioProcessingThread, self).__init__(*args, **kwargs)

        if self.sdk.debug:
            import soundfile as sf
            self.wav_file = sf.SoundFile(
                self.wav_filename, mode='w', channels=1,
                samplerate=self.sdk.input_sample_rate)

        self.daemon = True
        self.start()

    def run(self):
        """
        Continuously process any input data from the queue.

        Note: We need to sleep as much as possible in this thread
        to restrict CPU usage.

        Note: On very rare occassions, the daemon thread is still alive
        when the Python runtime has started its teardown process, so
        we check that `time` is still available to avoid accessing
        a null variable.
        """
        while self.is_alive() and time:

            tstart = time.time()
            while not self.input_queue.empty():

                data = self.input_queue.get()
                self.process_input_fn(data)
                if self.sdk.debug and not self.wav_file.closed:
                    self.wav_file.buffer_write(data, dtype=self.sample_size)

                block_size = len(data) / self.sample_length
                self.block_period = block_size / self.sample_rate

            tsleep = (self.block_period - ((time.time() - tstart)))
            if tsleep > 0:
                time.sleep(tsleep)

    def stop(self):
        """In debug mode, close wav file."""
        if self.sdk.debug:
            self.wav_file.close()
