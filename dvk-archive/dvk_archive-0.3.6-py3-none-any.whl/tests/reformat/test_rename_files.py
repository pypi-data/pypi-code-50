from pathlib import Path
from shutil import rmtree
from dvk_archive.file.dvk import Dvk
from dvk_archive.file.dvk_handler import DvkHandler
from dvk_archive.reformat.rename_files import rename_files


class TestRenameFiles():
    """
    Unit tests for the rename_files.py module.
    Attributes:
        test_dir (Path): Directory for holding test files.
    """

    def set_up(self):
        """
        Sets up test files before running unit tests.
        """
        self.test_dir = Path("rename")
        self.test_dir.mkdir(exist_ok=True)
        # DVK 1
        dvk = Dvk()
        dvk.set_file(str(self.test_dir.joinpath("d1.dvk")))
        dvk.set_id("ID123")
        dvk.set_title("Title 1")
        dvk.set_artist("artist")
        dvk.set_page_url("/url/")
        dvk.set_media_file("d1.txt")
        dvk.get_media_file().touch()
        dvk.write_dvk()
        # DVK 2
        dvk.set_file(str(self.test_dir.joinpath("d2.dvk")))
        dvk.set_id("D2")
        dvk.set_title("Title 2")
        dvk.set_media_file("d2.txt")
        dvk.get_media_file().touch()
        dvk.set_secondary_file("d2.png")
        dvk.get_secondary_file().touch()
        dvk.write_dvk()

    def tear_down(self):
        """
        Deletes test files after ErrorFinding testing.
        """
        rmtree(self.test_dir.absolute())

    def test_rename_files(self):
        """
        Tests the rename_files function.
        """
        try:
            self.set_up()
            rename_files(str(self.test_dir.absolute()))
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            dvk_handler.sort_dvks("a")
            # DVK 1
            title = "Title 1_ID123.dvk"
            assert dvk_handler.get_dvk_sorted(0).get_file().name == title
            assert dvk_handler.get_dvk_sorted(0).get_file().exists()
            title = "Title 1_ID123.txt"
            assert dvk_handler.get_dvk_sorted(0).get_media_file().name == title
            assert dvk_handler.get_dvk_sorted(0).get_media_file().exists()
            # DVK 2
            title = "Title 2_D2.dvk"
            assert dvk_handler.get_dvk_sorted(1).get_file().name == title
            assert dvk_handler.get_dvk_sorted(1).get_file().exists()
            title = "Title 2_D2.txt"
            assert dvk_handler.get_dvk_sorted(1).get_media_file().name == title
            assert dvk_handler.get_dvk_sorted(1).get_media_file().exists()
            title = "Title 2_D2.png"
            file = dvk_handler.get_dvk_sorted(1).get_secondary_file().name
            assert file == title
            assert dvk_handler.get_dvk_sorted(1).get_secondary_file().exists()
            assert dvk_handler.get_size() == 2
        finally:
            self.tear_down()

    def run_all(self):
        """
        Tests all functions of the rename_files.py module.
        """
        self.test_rename_files()
