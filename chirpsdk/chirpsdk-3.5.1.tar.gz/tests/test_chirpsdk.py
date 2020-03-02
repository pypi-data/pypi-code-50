# -*- coding: utf-8 -*-
"""
To run tests:
    python -m tests.test_chirpsdk
"""
import array as ar
import configparser
from datetime import datetime
import os
import sys
import unittest

try:
    from unittest.mock import patch
except:
    from mock import patch  # py2

from chirpsdk import (
    CHIRP_SDK_STATE_STOPPED,
    CHIRP_SDK_STATE_RUNNING,
    CHIRP_SDK_STATE_SENDING,
    ChirpSDK, ChirpSDKError
)


class TestChirpSDK(unittest.TestCase):
    BUFFER_SIZE = 1024
    TEST_PAYLOAD_LENGTH = 3

    @classmethod
    def setUpClass(cls):
        config = configparser.ConfigParser()
        config.read(os.path.expanduser('~/.chirprc'))

        try:
            cls.app_key = config.get('test', 'app_key')
            cls.app_secret = config.get('test', 'app_secret')
            cls.app_config = config.get('test', 'app_config')
        except configparser.NoSectionError:
            raise Exception("Couldn't find test credentials. Please add a [test] section to your ~/.chirprc.")

        cls.is2 = sys.version[0] == '2'

        # Mock functions causing errors from sounddevice in Python 2
        cls.sd_exit = patch('sounddevice._exit_handler')
        cls.sd_patch = cls.sd_exit.start()
        cls.thread_base = patch('concurrent.futures._base')
        cls.thread_patch = cls.thread_base.start()

    def setUp(self):
        self.sdk = ChirpSDK(self.app_key, self.app_secret, self.app_config)
        self.sdk.audio = None

        self.async_request = patch('requests_futures.sessions.FuturesSession.post')
        self.async_patch = self.async_request.start()
        self.addCleanup(self.async_request.stop)

        self.length = None
        self.channel = None

    def tearDown(self):
        self.sdk.close()
        self.sdk = None

    def test_version(self):
        version = self.sdk.version
        for data in ['name', 'version', 'build']:
            self.assertIn(data, version)
            self.assertTrue(len(version[data]) > 0)

    def test_read_chirprc(self):
        self.sdk.close()
        self.sdk.config = None
        self.sdk.read_chirprc('test')
        self.assertIsNotNone(self.sdk.config)

    # -- Getters & Setters

    def test_volume(self):
        self.assertEqual(self.sdk.volume, 1.0)

    def test_set_volume(self):
        self.sdk.volume = 0.33
        self.assertEqual(self.sdk.volume, 0.33)

    def test_input_sample_rate(self):
        self.assertEqual(self.sdk.input_sample_rate, 44100)

    def test_output_sample_rate(self):
        self.assertEqual(self.sdk.output_sample_rate, 44100)

    def test_set_input_sample_rate(self):
        self.sdk.input_sample_rate = 48000
        self.assertEqual(self.sdk.input_sample_rate, 48000)
        with self.assertRaises(ChirpSDKError):
            self.sdk.input_sample_rate = 0

    def test_set_output_sample_rate(self):
        self.sdk.output_sample_rate = 48000
        self.assertEqual(self.sdk.output_sample_rate, 48000)
        with self.assertRaises(ChirpSDKError):
            self.sdk.output_sample_rate = 0

    def test_default_state(self):
        self.assertEqual(self.sdk.state, CHIRP_SDK_STATE_STOPPED)

    def test_get_listen_to_self(self):
        self.assertFalse(self.sdk.listen_to_self)

    def test_set_listen_to_self(self):
        self.sdk.listen_to_self = True
        self.assertTrue(self.sdk.listen_to_self)

    def test_protocol_name(self):
        self.assertEqual(self.sdk.protocol_name, 'standard')

    def test_protocol_version(self):
        self.assertIsInstance(self.sdk.protocol_version, int)

    def test_protocol_duration(self):
        self.assertEqual(self.sdk.get_duration(10), 2.04)

    def test_expiry(self):
        self.assertIsInstance(self.sdk.expiry, datetime)

    def test_channel_count(self):
        self.assertEqual(self.sdk.channel_count, 1)

    def test_transmission_channel(self):
        self.assertEqual(self.sdk.transmission_channel, 0)

    def test_get_state_for_channel(self):
        self.sdk.start()
        self.assertEqual(self.sdk.get_state_for_channel(0), CHIRP_SDK_STATE_RUNNING)
        payload = self.sdk.random_payload(self.TEST_PAYLOAD_LENGTH)
        self.sdk.send(payload)
        self.assertEqual(self.sdk.get_state_for_channel(0), CHIRP_SDK_STATE_SENDING)

    # -- States

    def test_start(self):
        self.sdk.start()
        self.assertEqual(self.sdk.state, CHIRP_SDK_STATE_RUNNING)

    def test_already_started(self):
        self.sdk.start()
        with self.assertRaises(ChirpSDKError):
            self.sdk.start()

    def test_stop(self):
        self.sdk.start()
        self.sdk.stop()
        self.assertEqual(self.sdk.state, CHIRP_SDK_STATE_STOPPED)

    def test_already_stopped(self):
        with self.assertRaises(ChirpSDKError):
            self.sdk.stop()

    # -- Callbacks

    def stub_chirpsdk_state_callback(self, old, new):
        self.old = old
        self.new = new

    def stub_chirpsdk_callback(self, payload, channel):
        self.length = len(payload)
        self.channel = channel

    def stub_receiving_callback(self, channel):
        self.recv = True
        self.channel = channel

    def test_state_changed_callback(self):
        self.sdk.callbacks.on_state_changed = self.stub_chirpsdk_state_callback
        self.sdk.trigger_callbacks([0, 1, 2, 3, 4])
        self.assertIsNotNone(self.old)
        self.assertIsNotNone(self.new)

    def test_sending_callback(self):
        self.sdk.callbacks.on_sending = self.stub_chirpsdk_callback
        self.sdk.trigger_callbacks([0, 1, 2, 3, 4])
        self.assertIsNotNone(self.length)
        self.assertIsNotNone(self.channel)

    def test_sent_callback(self):
        self.sdk.callbacks.on_sent = self.stub_chirpsdk_callback
        self.sdk.trigger_callbacks([0, 1, 2, 3, 4])
        self.assertIsNotNone(self.length)
        self.assertIsNotNone(self.channel)

    def test_receiving_callback(self):
        self.sdk.callbacks.on_receiving = self.stub_receiving_callback
        self.sdk.trigger_callbacks([0, 1, 2, 3, 4])
        self.assertTrue(self.recv)
        self.assertIsNotNone(self.channel)

    def test_received_callback(self):
        self.sdk.callbacks.on_received = self.stub_chirpsdk_callback
        self.sdk.trigger_callbacks([0, 1, 2, 3, 4])
        self.assertIsNotNone(self.length)
        self.assertIsNotNone(self.channel)

    # -- Processing

    def test_process_input(self):
        indata = ar.array('f', [0.025] * self.BUFFER_SIZE)
        self.sdk.start()
        self.sdk.process_input(getattr(indata, 'tostring' if self.is2 else 'tobytes')())

    def test_process_input_not_started(self):
        indata = ar.array('f', [0.025] * self.BUFFER_SIZE)
        with self.assertRaises(ChirpSDKError):
            self.sdk.process_input(getattr(indata, 'tostring' if self.is2 else 'tobytes')())

    def test_process_output(self):
        outdata = ar.array('f', [0.05] * self.BUFFER_SIZE)
        self.sdk.start()
        self.sdk.process_output(outdata)

    def test_process_output_not_started(self):
        outdata = ar.array('f', [0.05] * self.BUFFER_SIZE)
        with self.assertRaises(ChirpSDKError):
            self.sdk.process_output(outdata)

    def test_process_shorts_input(self):
        indata = ar.array('h', [128] * self.BUFFER_SIZE)
        self.sdk.start()
        self.sdk.process_shorts_input(getattr(indata, 'tostring' if self.is2 else 'tobytes')())

    def test_process_shorts_output(self):
        outdata = ar.array('h', [-128] * self.BUFFER_SIZE)
        self.sdk.start()
        self.sdk.process_shorts_output(outdata)

    # -- Payload

    def test_get_max_payload_length(self):
        self.assertIsInstance(self.sdk.max_payload_length, int)
        self.assertTrue(self.sdk.max_payload_length > 0)

    def test_new_payload_string(self):
        payload = self.sdk.new_payload('test'.encode())
        self.assertIsInstance(payload, bytearray)

    def test_new_payload_array(self):
        payload = self.sdk.new_payload([64, 27, 33, 27])
        self.assertIsInstance(payload, bytearray)

    def test_random_payload(self):
        payload = self.sdk.random_payload(self.TEST_PAYLOAD_LENGTH)
        self.assertIsInstance(payload, bytearray)
        for byte in range(0, len(payload)):
            self.assertIsInstance(payload[byte], int)

    def test_pseudo_random_payload(self):
        self.sdk.set_random_seed(0)
        self.assertEqual(
            self.sdk.random_payload(0),
            [47, 117, 192, 67, 251, 195, 103, 9, 211,
             21, 242, 36, 87])

    def test_is_valid(self):
        payload = self.sdk.random_payload(self.TEST_PAYLOAD_LENGTH)
        self.assertTrue(self.sdk.is_valid(payload))

    def test_payload_is_valid(self):
        payload = self.sdk.random_payload(self.TEST_PAYLOAD_LENGTH)
        self.assertTrue(payload.isvalid())

    def test_payload_string(self):
        payload = self.sdk.new_payload(b'hello')
        self.assertEqual(payload.decode('utf8'), 'hello')

    def test_payload_string_to_hexstring(self):
        payload = self.sdk.new_payload(b'hello')
        self.assertEqual(payload.hex(), '68656c6c6f')

    def test_payload_string_to_list(self):
        payload = self.sdk.new_payload(b'hello')
        self.assertEqual(list(payload), [104, 101, 108, 108, 111])

    def test_payload_list_to_hexstring(self):
        payload = self.sdk.new_payload([0, 1, 2, 3])
        self.assertEqual(payload.hex(), '00010203')

    def test_payload_unicode_to_hexstring(self):
        data = 'hi 🙂'
        if self.is2:
            payload = self.sdk.new_payload(data.decode('utf-8').encode('utf-8'))
        else:
            payload = self.sdk.new_payload(data.encode('utf-8'))
        self.assertEqual(payload.hex(), '686920f09f9982')

    def test_send(self):
        self.sdk.start()
        payload = self.sdk.random_payload(self.TEST_PAYLOAD_LENGTH)
        self.assertIsNone(self.sdk.send(payload))

    def test_null_payload(self):
        with self.assertRaises(ValueError):
            self.sdk.new_payload([])

    def test_payload_too_long(self):
        payload = self.sdk.new_payload('hello'.encode('ascii'))
        with self.assertRaises(ValueError):
            payload.extend('this-is-wayyyyy-toooooo-long')


if __name__ == '__main__':
    unittest.main()
