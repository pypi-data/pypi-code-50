import unittest
import subprocess

import audio.ffmpeg

class FFMPEGTests(unittest.TestCase):
    def test_call_normal(self):
        p = audio.ffmpeg.call(["-h"])
        self.assertTrue(isinstance(p, subprocess.Popen))

    def test_call_err(self):
        with self.assertRaises(TypeError):
            audio.ffmpeg.call("test")
