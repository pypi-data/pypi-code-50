import unittest
import trellotool.command


class TestCommand(unittest.TestCase):

    def test_add(self):

        def _dummy():
            pass

        c = trellotool.command.Command("baz")
        c.add("fred", _dummy, "foo", "bar")
        self.assertEqual("baz", c.name)
        self.assertEqual(_dummy, c.commands["fred"]["func"])
        self.assertEqual("bar", c.commands["fred"]["valid_args"])
        self.assertEqual("foo", c.commands["fred"]["help_text"])
