import json, os, uuid, re
from .text_tools import TextTools

class FileTools():
    """ """

    def __init__(self, filename):
        """Initialize FileTools."""
        self.filename = filename

    def generate_unique_filename(self):
        """Generate unique filename."""
        unique_id = uuid.uuid4().hex
        filename = TextTools().clean_text(os.path.splitext(self.filename)[0])
        extension = os.path.splitext(self.filename)[1][1:]
        new_filename = "%s-%s.%s" % (filename, unique_id, extension)
        return new_filename

    def process_json_file(self):
        """Return processed json file dict."""
        with open(self.filename) as file:
            json_file_bytes = file.read()
            file.close()

        return json.loads(json_file_bytes)
