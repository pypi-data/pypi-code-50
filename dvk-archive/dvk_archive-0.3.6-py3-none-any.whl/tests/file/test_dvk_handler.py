from shutil import rmtree
from pathlib import Path
from dvk_archive.file.dvk import Dvk
from dvk_archive.file.dvk_handler import DvkHandler


class TestDvkHandler():
    """
    Unit tests for the DvkHandler class.

    Attributes:
        test_dir (Path): Directory for holding test files.
    """

    def set_up(self):
        """
        Sets up test files before running tests.
        """
        self.test_dir = Path("handlerTest")
        self.test_dir.mkdir(exist_ok=True)
        dvk = Dvk()
        dvk.set_file(self.test_dir.joinpath("dvk.dvk").absolute())
        dvk.set_id("Unimportant")
        dvk.set_page_url("/unimportant")
        dvk.set_direct_url("/thing")
        dvk.set_media_file("unimportant")
        count = 0
        while count < 2:
            dvk_file = self.test_dir.joinpath("dvk" + str(count) + ".dvk")
            dvk.set_file(dvk_file.absolute())
            dvk.set_title("DVK " + str(10 - count))
            dvk.set_artist("Thing")
            dvk.set_time_int(2019, 11, 8, 12, 20 - count)
            dvk.set_rating(5 - count)
            dvk.set_views(10 - count)
            dvk.write_dvk()
            count = count + 1
        # SUB-DIRECTORY 1
        sub1 = Path(self.test_dir.joinpath("sub1").absolute())
        sub1.mkdir(exist_ok=True)
        while count < 4:
            dvk_file = sub1.joinpath("dvk" + str(10 - count) + ".dvk")
            dvk.set_file(dvk_file.absolute())
            dvk.set_title("DVK " + str(10 - count))
            dvk.set_artist("Artist" + str(10 - count))
            dvk.set_time_int(2019, 11, 8, 12, 10 - count)
            dvk.set_rating(5 - count)
            dvk.set_views(80 - count)
            dvk.write_dvk()
            count = count + 1
        # SUB-DIRECTORY 2
        sub2 = Path(self.test_dir.joinpath("sub2").absolute())
        sub2.mkdir(exist_ok=True)
        while count < 6:
            dvk_file = sub2.joinpath("dvk" + str(10 - count) + ".dvk")
            dvk.set_file(dvk_file.absolute())
            dvk.set_title("DVK " + str(10 - count))
            dvk.set_artist("Thing")
            dvk.set_time_int(2019, 11, 8, 12, 30 - count)
            dvk.set_rating(7 - count)
            dvk.set_views(60 - count)
            dvk.write_dvk()
            count = count + 1
        # INTERNAL SUB-DIRECTORY
        int_sub = Path(sub2.joinpath("intSub").absolute())
        int_sub.mkdir(exist_ok=True)
        while count < 8:
            dvk_file = int_sub.joinpath("dvk" + str(10 - count) + ".dvk")
            dvk.set_file(dvk_file.absolute())
            dvk.set_title("DVK " + str(10 - count))
            dvk.set_artist("Thing")
            dvk.set_time_int(2019, 11, 8, 12, 10 - count)
            dvk.set_rating(9 - count)
            dvk.set_views(70 - count)
            dvk.write_dvk()
            count = count + 1
        empty_sub = Path(sub2.joinpath("empty").absolute())
        empty_sub.mkdir(exist_ok=True)

    def tear_down(self):
        """
        Removes all test files.
        """
        rmtree(self.test_dir.absolute())

    def test_reset_sorted(self):
        """
        Tests the reset_sorted function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            assert dvk_handler.get_size() == 8
            count = 0
            while count < len(dvk_handler.sorted):
                assert dvk_handler.sorted[count] == count
                count = count + 1
            dvk_handler.load_dvks()
            assert dvk_handler.sorted == []
        finally:
            self.tear_down()

    def test_get_dvk_direct(self):
        """
        Tests the get_dvk_direct function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            assert dvk_handler.get_dvk_direct().title is None
            assert dvk_handler.get_dvk_direct(-1).title is None
            assert dvk_handler.get_dvk_direct(8).title is None
            titles = []
            for i in range(0, 8):
                dvk = dvk_handler.get_dvk_direct(i)
                assert dvk.title not in titles
                titles.append(dvk.title)
        finally:
            self.tear_down()

    def test_get_size(self):
        """
        Tests the get_size function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            assert dvk_handler.get_size() == 8
            dvk_handler.load_dvks(None)
            assert dvk_handler.get_size() == 0
            dvk_file = self.test_dir.joinpath("sub1").absolute()
            dvk_handler.load_dvks([Path(dvk_file).absolute()])
            assert dvk_handler.get_size() == 2
        finally:
            self.tear_down()

    def test_get_directories(self):
        """
        Tests the get_directories function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            paths = dvk_handler.get_directories([self.test_dir.absolute()])
            assert len(paths) == 4
            assert paths[0].name == "handlerTest"
            assert paths[1].name == "sub1"
            assert paths[2].name == "sub2"
            assert paths[3].name == "intSub"
            dvk_file = self.test_dir.joinpath("sub2").absolute()
            paths = dvk_handler.get_directories([Path(dvk_file).absolute()])
            assert len(paths) == 2
            assert paths[0].name == "sub2"
            assert paths[1].name == "intSub"
            assert dvk_handler.get_directories() == []
            assert dvk_handler.get_directories(None) == []
            assert dvk_handler.get_directories("lskdfjo") == []
            s_paths = []
            s_paths.append(self.test_dir.joinpath("sub1").absolute())
            s_paths.append(self.test_dir.joinpath("sub2").absolute())
            paths = dvk_handler.get_directories(s_paths)
            assert len(paths) == 3
            assert paths[0].name == "sub1"
            assert paths[1].name == "sub2"
            assert paths[2].name == "intSub"
            # EMPTY FOLDER
            empty_dir = self.test_dir.joinpath("empty")
            empty_dir.mkdir(exist_ok=True)
            paths = dvk_handler.get_directories([empty_dir.absolute()])
            assert len(paths) == 1
            assert paths[0].name == "empty"
        finally:
            self.tear_down()

    def test_contains_page_url(self):
        """
        Tests the contains_page_url function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            assert not dvk_handler.contains_page_url()
            assert not dvk_handler.contains_page_url("bleh")
            dvk_handler.load_dvks([self.test_dir.absolute()])
            assert not dvk_handler.contains_page_url()
            assert not dvk_handler.contains_page_url("bleh")
            assert dvk_handler.contains_page_url("/unimportant")
        finally:
            self.tear_down()

    def test_contains_direct_url(self):
        """
        Tests the contains_page_url function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            assert not dvk_handler.contains_direct_url()
            assert not dvk_handler.contains_direct_url("bleh")
            dvk_handler.load_dvks([self.test_dir.absolute()])
            assert not dvk_handler.contains_direct_url()
            assert not dvk_handler.contains_direct_url("bleh")
            assert dvk_handler.contains_direct_url("/thing")
        finally:
            self.tear_down()

    def test_contains_id(self):
        """
        Tests the contains_id function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            assert not dvk_handler.contains_id()
            assert not dvk_handler.contains_id("bleh")
            dvk_handler.load_dvks([self.test_dir.absolute()])
            assert not dvk_handler.contains_id()
            assert not dvk_handler.contains_id("bleh")
            assert dvk_handler.contains_id("UNIMPORTANT")
        finally:
            self.tear_down()

    def test_add_dvk(self):
        """
        Tests the add_dvk function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            assert dvk_handler.get_size() == 8
            dvk_handler.add_dvk()
            assert dvk_handler.get_size() == 8
            dvk = Dvk()
            dvk.set_title()
            dvk_handler.add_dvk(dvk)
            assert dvk_handler.get_size() == 9
        finally:
            self.tear_down()

    def test_sort_dvks_alpha(self):
        """
        Tests alpha-numeric sorting with the sort_dvks function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            dvk_handler.sort_dvks("a", False)
            assert dvk_handler.get_dvk_sorted(0).get_title() == "DVK 3"
            assert dvk_handler.get_dvk_sorted(1).get_title() == "DVK 4"
            assert dvk_handler.get_dvk_sorted(2).get_title() == "DVK 5"
            assert dvk_handler.get_dvk_sorted(3).get_title() == "DVK 6"
            assert dvk_handler.get_dvk_sorted(4).get_title() == "DVK 7"
            assert dvk_handler.get_dvk_sorted(5).get_title() == "DVK 8"
            assert dvk_handler.get_dvk_sorted(6).get_title() == "DVK 9"
            assert dvk_handler.get_dvk_sorted(7).get_title() == "DVK 10"
            # GROUP ARTISTS
            dvk_handler.sort_dvks("a", True)
            assert dvk_handler.get_dvk_sorted(0).get_title() == "DVK 7"
            assert dvk_handler.get_dvk_sorted(0).get_artists() == ["Artist7"]
            assert dvk_handler.get_dvk_sorted(1).get_title() == "DVK 8"
            assert dvk_handler.get_dvk_sorted(1).get_artists() == ["Artist8"]
            assert dvk_handler.get_dvk_sorted(2).get_title() == "DVK 3"
            assert dvk_handler.get_dvk_sorted(2).get_artists() == ["Thing"]
            assert dvk_handler.get_dvk_sorted(3).get_title() == "DVK 4"
            assert dvk_handler.get_dvk_sorted(4).get_title() == "DVK 5"
            assert dvk_handler.get_dvk_sorted(5).get_title() == "DVK 6"
            assert dvk_handler.get_dvk_sorted(6).get_title() == "DVK 9"
            assert dvk_handler.get_dvk_sorted(7).get_title() == "DVK 10"
            # EMPTY
            dvk_handler.load_dvks()
            dvk_handler.sort_dvks("a", False)
            assert dvk_handler.get_size() == 0
        finally:
            self.tear_down()

    def test_sort_dvks_time(self):
        """
        Tests sorting by time with the sort_dvks function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            dvk_handler.sort_dvks("t", False)
            time = "2019/11/08|12:03"
            assert dvk_handler.get_dvk_sorted(0).get_time() == time
            time = "2019/11/08|12:04"
            assert dvk_handler.get_dvk_sorted(1).get_time() == time
            time = "2019/11/08|12:07"
            assert dvk_handler.get_dvk_sorted(2).get_time() == time
            time = "2019/11/08|12:08"
            assert dvk_handler.get_dvk_sorted(3).get_time() == time
            time = "2019/11/08|12:19"
            assert dvk_handler.get_dvk_sorted(4).get_time() == time
            time = "2019/11/08|12:20"
            assert dvk_handler.get_dvk_sorted(5).get_time() == time
            time = "2019/11/08|12:25"
            assert dvk_handler.get_dvk_sorted(6).get_time() == time
            time = "2019/11/08|12:26"
            assert dvk_handler.get_dvk_sorted(7).get_time() == time
            # GROUP ARTISTS
            dvk_handler.sort_dvks("t", True)
            time = "2019/11/08|12:07"
            assert dvk_handler.get_dvk_sorted(0).get_time() == time
            assert dvk_handler.get_dvk_sorted(0).get_artists() == ["Artist7"]
            time = "2019/11/08|12:08"
            assert dvk_handler.get_dvk_sorted(1).get_time() == time
            assert dvk_handler.get_dvk_sorted(1).get_artists() == ["Artist8"]
            time = "2019/11/08|12:03"
            assert dvk_handler.get_dvk_sorted(2).get_time() == time
            assert dvk_handler.get_dvk_sorted(2).get_artists() == ["Thing"]
            time = "2019/11/08|12:04"
            assert dvk_handler.get_dvk_sorted(3).get_time() == time
            time = "2019/11/08|12:19"
            assert dvk_handler.get_dvk_sorted(4).get_time() == time
            time = "2019/11/08|12:20"
            assert dvk_handler.get_dvk_sorted(5).get_time() == time
            time = "2019/11/08|12:25"
            assert dvk_handler.get_dvk_sorted(6).get_time() == time
            time = "2019/11/08|12:26"
            assert dvk_handler.get_dvk_sorted(7).get_time() == time
            # EMPTY
            dvk_handler.load_dvks()
            dvk_handler.sort_dvks("t", False)
            assert dvk_handler.get_size() == 0
        finally:
            self.tear_down()

    def test_sort_dvks_ratings(self):
        """
        Tests sorting by ratings with the sort_dvks function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            dvk_handler.sort_dvks("r", False)
            assert dvk_handler.get_dvk_sorted(0).get_rating() == 2
            assert dvk_handler.get_dvk_sorted(0).get_title() == "DVK 3"
            assert dvk_handler.get_dvk_sorted(1).get_rating() == 2
            assert dvk_handler.get_dvk_sorted(1).get_title() == "DVK 5"
            assert dvk_handler.get_dvk_sorted(2).get_rating() == 2
            assert dvk_handler.get_dvk_sorted(2).get_title() == "DVK 7"
            assert dvk_handler.get_dvk_sorted(3).get_rating() == 3
            assert dvk_handler.get_dvk_sorted(3).get_title() == "DVK 4"
            assert dvk_handler.get_dvk_sorted(4).get_rating() == 3
            assert dvk_handler.get_dvk_sorted(4).get_title() == "DVK 6"
            assert dvk_handler.get_dvk_sorted(5).get_rating() == 3
            assert dvk_handler.get_dvk_sorted(5).get_title() == "DVK 8"
            assert dvk_handler.get_dvk_sorted(6).get_rating() == 4
            assert dvk_handler.get_dvk_sorted(7).get_rating() == 5
            # GROUP ARTISTS
            dvk_handler.sort_dvks("r", True)
            assert dvk_handler.get_dvk_sorted(0).get_rating() == 2
            assert dvk_handler.get_dvk_sorted(0).get_artists() == ["Artist7"]
            assert dvk_handler.get_dvk_sorted(1).get_rating() == 3
            assert dvk_handler.get_dvk_sorted(1).get_artists() == ["Artist8"]
            assert dvk_handler.get_dvk_sorted(2).get_rating() == 2
            assert dvk_handler.get_dvk_sorted(2).get_artists() == ["Thing"]
            assert dvk_handler.get_dvk_sorted(2).get_title() == "DVK 3"
            assert dvk_handler.get_dvk_sorted(3).get_rating() == 2
            assert dvk_handler.get_dvk_sorted(3).get_title() == "DVK 5"
            assert dvk_handler.get_dvk_sorted(4).get_rating() == 3
            assert dvk_handler.get_dvk_sorted(4).get_title() == "DVK 4"
            assert dvk_handler.get_dvk_sorted(5).get_rating() == 3
            assert dvk_handler.get_dvk_sorted(5).get_title() == "DVK 6"
            assert dvk_handler.get_dvk_sorted(6).get_rating() == 4
            assert dvk_handler.get_dvk_sorted(7).get_rating() == 5
            # EMPTY
            dvk_handler.load_dvks()
            dvk_handler.sort_dvks("r", False)
            assert dvk_handler.get_size() == 0
        finally:
            self.tear_down()

    def test_sort_dvks_views(self):
        """
        Tests sorting by view count with the sort_dvks function.
        """
        try:
            self.set_up()
            dvk_handler = DvkHandler()
            dvk_handler.load_dvks([self.test_dir.absolute()])
            dvk_handler.sort_dvks("v", False)
            assert dvk_handler.get_dvk_sorted(0).get_views() == 9
            assert dvk_handler.get_dvk_sorted(1).get_views() == 10
            assert dvk_handler.get_dvk_sorted(2).get_views() == 55
            assert dvk_handler.get_dvk_sorted(3).get_views() == 56
            assert dvk_handler.get_dvk_sorted(4).get_views() == 63
            assert dvk_handler.get_dvk_sorted(5).get_views() == 64
            assert dvk_handler.get_dvk_sorted(6).get_views() == 77
            assert dvk_handler.get_dvk_sorted(7).get_views() == 78
            dvk_handler.sort_dvks("v", True)
            assert dvk_handler.get_dvk_sorted(0).get_views() == 77
            assert dvk_handler.get_dvk_sorted(0).get_artists() == ["Artist7"]
            assert dvk_handler.get_dvk_sorted(1).get_views() == 78
            assert dvk_handler.get_dvk_sorted(1).get_artists() == ["Artist8"]
            assert dvk_handler.get_dvk_sorted(2).get_views() == 9
            assert dvk_handler.get_dvk_sorted(2).get_artists() == ["Thing"]
            assert dvk_handler.get_dvk_sorted(3).get_views() == 10
            assert dvk_handler.get_dvk_sorted(4).get_views() == 55
            assert dvk_handler.get_dvk_sorted(5).get_views() == 56
            assert dvk_handler.get_dvk_sorted(6).get_views() == 63
            assert dvk_handler.get_dvk_sorted(7).get_views() == 64
            # EMPTY
            dvk_handler.load_dvks()
            dvk_handler.sort_dvks("v", False)
            assert dvk_handler.get_size() == 0
        finally:
            self.tear_down()

    def run_all(self):
        """
        Tests all functions in DvkHandler class.
        """
        self.test_reset_sorted()
        self.test_get_dvk_direct()
        self.test_get_size()
        self.test_get_directories()
        self.test_contains_id()
        self.test_contains_page_url()
        self.test_contains_direct_url()
        self.test_add_dvk()
        self.test_sort_dvks_alpha()
        self.test_sort_dvks_time()
        self.test_sort_dvks_views()
        self.test_sort_dvks_ratings()
