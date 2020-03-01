import markdown
import unittest

import markdown_vidify

class VidifyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_input(self):
        inString = ""
        outString = markdown.markdown(inString, extensions = [markdown_vidify.VidifyExtension()], output_format="html5")
        self.assertEqual(inString, outString)

    def test_no_images(self):
        inString = """\
This is a test.

It contains multiple paragraphs and some [links](https://example.com)

* Some
* Lists
* Too

# This is a heading

Nothing should change when using markdown_vidify."""
        expectedString = markdown.markdown(inString)
        outString = markdown.markdown(inString, extensions = [markdown_vidify.VidifyExtension()], output_format="html5")
        self.assertEqual(expectedString, outString)

    def test_no_videos(self):
        inString = """\
This is a test.

It contains multiple paragraphs and some [links](https://example.com)

* Some
* Lists
* Too

# This is a heading

[But this time there's an image too](/content/image.png "It even has a title!")

Nothing should change when using markdown_vidify."""
        expectedString = markdown.markdown(inString)
        outString = markdown.markdown(inString, extensions = [markdown_vidify.VidifyExtension()], output_format="html5")
        self.assertEqual(expectedString, outString)
        
    def test_simple_video(self):
        inString= """\
![videos do not have alt text](/content/video.webm "Videos can have titles")"""
        expectedString = """\
<p><video src="/content/video.webm" title="Videos can have titles"></video></p>"""
        outString = markdown.markdown(inString, extensions = [markdown_vidify.VidifyExtension()], output_format="html5")
        self.assertEqual(expectedString, outString)
        
    def test_advanced_video(self):
        inString= """\
![videos do not have alt text](/content/video.webm "Videos can have titles")"""
        expectedString = """\
<p><video autoplay controls loop muted src="/content/video.webm" title="Videos can have titles"></video></p>"""
        outString = markdown.markdown(inString, extensions = [markdown_vidify.VidifyExtension(
            autoplay=True,
            controls=True,
            loop=True,
            muted=True,
        )], output_format="html5")
        self.assertEqual(expectedString, outString)
