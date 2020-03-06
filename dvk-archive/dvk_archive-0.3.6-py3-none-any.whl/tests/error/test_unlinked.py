from pathlib import Path
from shutil import rmtree
from dvk_archive.file.dvk import Dvk
from dvk_archive.file.dvk_handler import DvkHandler
from dvk_archive.error.unlinked import unlinked_media


class TestUnlinkedMedia():
    """
    Unit tests for the unlinked.py module.
    Attributes:
        test_dir (Path): Directory for holding test files.
    """

    def set_up(self):
        """
        Sets up test files before running unit tests.
        """
        self.test_dir = Path("finding")
        self.test_dir.mkdir(exist_ok=True)
        self.test_dir.joinpath("file0").touch()
        sub = Path(self.test_dir.joinpath("sub").absolute())
        sub.mkdir(exist_ok=True)
        sub2 = Path(self.test_dir.joinpath("sub2").absolute())
        sub2.mkdir(exist_ok=True)
        # CREATE UNLINKED FILE
        file = sub2.joinpath("noDVK.txt")
        file.touch()
        # DVK 1
        dvk = Dvk(self.test_dir.joinpath("dvk1.dvk").absolute())
        file = self.test_dir.joinpath("file1.txt")
        file.touch()
        dvk.set_id("id1")
        dvk.set_title("title1")
        dvk.set_artist("artist")
        dvk.set_page_url("/page/url")
        dvk.set_media_file(file)
        file = self.test_dir.joinpath("fileSecond.no")
        file.touch()
        dvk.set_secondary_file(file)
        dvk.write_dvk()
        # DVK 2
        file = sub.joinpath("file2.png")
        file.touch()
        dvk.set_id("id2")
        dvk.set_title("title2")
        dvk.set_file(sub.joinpath("dvk2.dvk").absolute())
        dvk.set_media_file(file)
        file = sub.joinpath("second.dmf")
        dvk.set_secondary_file(file)
        dvk.write_dvk()
        # DVK 3
        sub.joinpath("file1.txt").touch()
        file = sub.joinpath("file3.svg")
        dvk.set_id("id1")
        dvk.set_title("title3")
        dvk.set_file(sub.joinpath("dvk3.dvk").absolute())
        dvk.set_media_file(file)
        dvk.set_secondary_file(None)
        dvk.write_dvk()
        # DVK 4
        file = self.test_dir.joinpath("file4.ogg")
        dvk.set_title("title4")
        dvk.set_file(self.test_dir.joinpath("dvk4.dvk").absolute())
        dvk.set_media_file(file)
        dvk.write_dvk()

    def tear_down(self):
        """
        Deletes test files after ErrorFinding testing.
        """
        rmtree(self.test_dir.absolute())

    def test_unlinked_media(self):
        """
        Tests the unlinked_media function.
        """
        try:
            self.set_up()
            missing = unlinked_media([self.test_dir.absolute()])
            assert len(missing) == 2
            assert missing[0].name == "file0"
            assert missing[1].name == "file1.txt"
            assert unlinked_media() == []
            handler = DvkHandler()
            handler.load_dvks([self.test_dir.joinpath("sub").absolute()])
            missing = unlinked_media(dvk_handler=handler)
            assert len(missing) == 1
            assert missing[0].name == "file1.txt"
        finally:
            self.tear_down()

    def run_all(self):
        """
        Tests all functions of the unlinked.py module.
        """
        self.test_unlinked_media()
