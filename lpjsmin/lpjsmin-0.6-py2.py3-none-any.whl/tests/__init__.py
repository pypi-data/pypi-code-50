"""
lpjsmin tests

"""
import glob
import os

from subprocess import call
from subprocess import PIPE
from subprocess import Popen
from unittest import TestCase

from nose.tools import eq_
from nose.tools import ok_
import six

# we're testing this module
import lpjsmin


TEST_TOP = os.path.dirname(__file__)
MINIMIZED1 = """
var test=function(one){console.log('something');};"""
MINIMIZED2 = """
var test2=function(one){console.log('something2');};"""
SAMPLE1 = os.path.join(TEST_TOP, "jsfiles", "sample1.js")
RES1 = os.path.join(TEST_TOP, "jsfiles", "sample1-min.js")
SAMPLE2 = os.path.join(TEST_TOP, "jsfiles", "sample2.js")
RES2 = os.path.join(TEST_TOP, "jsfiles", "sample2-min.js")


class TestMinify(TestCase):
    """Initial set of minifying tests"""

    def tearDown(self):
        """Make sure we remove generated files"""
        for f in glob.glob(os.path.join(TEST_TOP, 'jsfiles', '*-min.js')):
            os.remove(f)

    def test_sample1(self):
        """Verify we can minimize an initial sample file"""
        lpjsmin.minify(SAMPLE1)
        ok_(os.path.isfile(RES1), "The -min.js file should exist in place")

        content = open(RES1).read()
        eq_(MINIMIZED1, content,
            "The content should be minimized and just like this: " + content)

class TestCmdLine(TestCase):
    """Verify that our cmd line client is working"""

    def tearDown(self):
        """Make sure we remove generated files"""
        for f in glob.glob(os.path.join(TEST_TOP, 'jsfiles', '*-min.js')):
            os.remove(f)

    def test_single_file(self):
        """Make sure we can give the cmd line a single file"""
        call(['lpjsmin', '-p', SAMPLE1])
        ok_(os.path.isfile(RES1), "The -min.js file should exist in place")

        content = open(RES1).read()
        eq_(MINIMIZED1, content,
            "The content should be minimized and just like this: " + content)

    def test_directory(self):
        """Now try to min the entire directory in one swoop via the cmdline"""
        call(['lpjsmin', '-p', os.path.join(TEST_TOP, 'jsfiles')])

        ok_(os.path.isfile(RES1), "The -min.js file should exist in place")
        content = open(RES1).read()
        eq_(MINIMIZED1, content,
            "The content should be minimized and just like this: " + content)

        ok_(os.path.isfile(RES2), "The -min.js file should exist in place")
        content = open(RES2).read()
        eq_(MINIMIZED2, content,
            "The content should be minimized and just like this: " + content)

    def test_stdin(self):
        """Verify we can minimize over stdin"""
        # output=`dmesg | grep hda`
        # becomes
        p1 = Popen(["cat", SAMPLE1], stdout=PIPE, universal_newlines=True)
        p2 = Popen(
            ["lpjsmin"], stdin=p1.stdout, stdout=PIPE, universal_newlines=True)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        out = p2.communicate()[0]
        eq_(MINIMIZED1, out,
            "The content should be minimized and just like this: " + out)
        p2.stdout.close()


    def test_skip_min(self):
        """Verify we don't double minify files."""
        filenames = [
            'test.min.js',
            'test-min.js'
        ]

        for f in filenames:
            ok_(lpjsmin.is_min(f))

    def test_skip_css_files(self):
        """We don't attempt to process no js files."""
        expected_filenames = [
            os.path.join(TEST_TOP, 'jsfiles', 'sample1.js'),
            os.path.join(TEST_TOP, 'jsfiles', 'sample2.js'),
        ]

        eq_(expected_filenames,
            list(lpjsmin.dirwalk(os.path.join(TEST_TOP, 'jsfiles'))))


class TestStream(TestCase):
    """Verify we can minify streams of IO successfully"""

    def test_file(self):
        """Given the input stream of a file, minify it"""
        in_stream = open(SAMPLE1)
        out_stream = six.StringIO()

        lpjsmin.minify_stream(in_stream, out_stream)

        res = out_stream.getvalue()
        eq_(MINIMIZED1, out_stream.getvalue(),
            "The minimized input should match the out stream")


