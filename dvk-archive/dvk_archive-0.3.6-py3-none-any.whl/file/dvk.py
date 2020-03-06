from os import remove, rename
from json import dump, load
from pathlib import Path
from random import seed, randint
from dvk_archive.processing.html_processing import add_escapes_to_html
from dvk_archive.processing.list_processing import clean_list
from dvk_archive.processing.string_processing import extend_int
from dvk_archive.processing.string_processing import get_filename
from dvk_archive.processing.string_processing import get_extension
from dvk_archive.web.basic_connect import download, get_last_modified


class Dvk:
    """
    Class for handling DVK files.

    Attributes:
        dvk_file (Path): File path of the current DVK file
        id (str): DVK ID
        title (str): DVK title
        artists (list): DVK artist List
        time (str): DVK Time of publication (YYYY/MM/DD|hh:mm)
        web_tags (list): DVK web tag list
        description (str): DVK description
        page_url (str): DVK Page URL
        direct_url (str): DVK Direct URL
        secondary_url (str): DVK Secondary URL
        media_file (Path): DVK media file path
        secondary_file (Path): DVK secondary media file path
        previous_ids (list): Previous IDs in a DVK sequence
        next_ids (list): Next IDs in a DVK sequence
        section_first (bool): If DVK is first in a sequence section
        section_last (bool): If DVK is last in a sequence section
        sequence_title (str): DVK sequence title
        section_title (str): DVK section title
        branch_titles (list): DVK sequence branch titles
        rating (int): DVK rating
        views (int): DVK views
        user_tags (list): DVK user tags
    """

    def __init__(self, file_path: str = None):
        """
        Initializes all DVK values, reading from a DVK file, if given.
        """
        # CLEAR DVK VALUES
        self.dvk_file = ""
        self.set_file(file_path)
        self.clear_dvk()

        if self.get_file() is not None:
            self.read_dvk()

    def clear_dvk(self):
        """
        Sets all DVK data to their default values.
        """
        self.set_id()
        self.set_title()
        self.set_artist()
        self.set_time()
        self.set_web_tags()
        self.set_description()
        # WEB
        self.set_page_url()
        self.set_direct_url()
        self.set_secondary_url()
        # FILE
        self.set_media_file()
        self.set_secondary_file()
        self.set_previous_ids()
        self.set_next_ids()
        self.set_section_first()
        self.set_section_last()
        # USER
        self.set_sequence_title()
        self.set_section_title()
        self.set_branch_titles()
        self.set_rating()
        self.set_views()
        self.set_user_tags()

    def write_dvk(self):
        """
        Writes DVK data to the currently set DVK file.
        """
        if self.can_write():
            data = dict()
            data["file_type"] = "dvk"
            data["id"] = self.get_id()
            # INFO
            dvk_info = dict()
            dvk_info["title"] = self.get_title()
            dvk_info["artists"] = self.get_artists()
            value = self.get_time()
            if not self.get_time() == "0000/00/00|00:00":
                dvk_info = self.add_to_dict(dvk_info, "time", value)
            value = self.get_web_tags()
            dvk_info = self.add_to_dict(dvk_info, "web_tags", value)
            value = self.get_description()
            dvk_info = self.add_to_dict(dvk_info, "description", value)
            data = self.add_to_dict(data, "info", dvk_info)
            # WEB
            dvk_web = dict()
            value = self.get_page_url()
            dvk_web = self.add_to_dict(dvk_web, "page_url", value)
            value = self.get_direct_url()
            dvk_web = self.add_to_dict(dvk_web, "direct_url", value)
            value = self.get_secondary_url()
            dvk_web = self.add_to_dict(dvk_web, "secondary_url", value)
            data = self.add_to_dict(data, "web", dvk_web)
            # FILE
            dvk_fd = dict()
            value = self.get_media_file().name
            dvk_fd = self.add_to_dict(dvk_fd, "media_file", value)
            if self.get_secondary_file() is not None:
                value = self.get_secondary_file().name
                dvk_fd = self.add_to_dict(dvk_fd, "secondary_file", value)
            value = self.get_previous_ids()
            dvk_fd = self.add_to_dict(dvk_fd, "previous_ids", value)
            value = self.get_next_ids()
            dvk_fd = self.add_to_dict(dvk_fd, "next_ids", value)
            value = self.get_section_first()
            dvk_fd = self.add_to_dict(dvk_fd, "section_first", value)
            value = self.get_section_last()
            dvk_fd = self.add_to_dict(dvk_fd, "section_last", value)
            data = self.add_to_dict(data, "file", dvk_fd)
            # USER
            dvk_user = dict()
            value = self.get_sequence_title()
            dvk_user = self.add_to_dict(dvk_user, "sequence_title", value)
            value = self.get_section_title()
            dvk_user = self.add_to_dict(dvk_user, "section_title", value)
            value = self.get_branch_titles()
            dvk_user = self.add_to_dict(dvk_user, "branch_titles", value)
            if not self.get_rating() == 0:
                value = self.get_rating()
                dvk_user = self.add_to_dict(dvk_user, "rating", value)
            value = self.get_views()
            dvk_user = self.add_to_dict(dvk_user, "views", value)
            value = self.get_user_tags()
            dvk_user = self.add_to_dict(dvk_user, "user_tags", value)
            data = self.add_to_dict(data, "user", dvk_user)
            # WRITE
            try:
                with open(self.get_file().absolute(), "w") as out_file:
                    dump(data, out_file, indent=4, separators=(",", ": "))

            except IOError as e:
                print("File error: " + str(e))

    def write_media(self, get_time: bool = False):
        """
        Writes the DVK file and downloads associated media, if available.
        Nothing is writen if DVK or media URLs are invalid.

        Parameters:
            get_time (bool): Whether to get the last modified time of URL
                             for the DVK's time published
        """
        self.write_dvk()
        if self.get_file().exists():
            # DOWNLOAD MEDIA FILE
            mf = str(self.get_media_file().absolute())
            headers = download(self.get_direct_url(), mf)
            if self.get_media_file().exists():
                # DOWNLOAD SECONDARY FILE
                if self.get_secondary_url() is not None:
                    download(
                        self.get_secondary_url(),
                        self.get_secondary_file().absolute())
                    if not self.get_secondary_file().exists():
                        remove(str(self.get_media_file().absolute()))
                        remove(str(self.get_file().absolute()))
            else:
                remove(str(self.get_file().absolute()))
        if get_time and self.get_file().exists():
            self.set_time(get_last_modified(headers))
            self.write_dvk()

    def read_dvk(self):
        """
        Reads DVK data from the currently set DVK file.
        """
        self.clear_dvk()
        if self.get_file() is not None and self.get_file().is_file():
            try:
                with open(self.get_file().absolute()) as in_file:
                    data = load(in_file)
                    if data["file_type"] == "dvk":
                        # INFO
                        keys = ["id"]
                        org = self.get_id()
                        value = self.get_from_dict(data, keys, org)
                        self.set_id(value)
                        keys = ["info", "title"]
                        org = self.get_title()
                        value = self.get_from_dict(data, keys, org)
                        self.set_title(value)
                        keys = ["info", "artists"]
                        org = self.get_artists()
                        value = self.get_from_dict(data, keys, org)
                        self.set_artists(value)
                        keys = ["info", "time"]
                        org = self.get_time()
                        value = self.get_from_dict(data, keys, org)
                        self.set_time(value)
                        keys = ["info", "web_tags"]
                        org = self.get_web_tags()
                        value = self.get_from_dict(data, keys, org)
                        self.set_web_tags(value)
                        keys = ["info", "description"]
                        org = self.get_description()
                        value = self.get_from_dict(data, keys, org)
                        self.set_description(value)

                        # WEB
                        keys = ["web", "page_url"]
                        org = self.get_page_url()
                        value = self.get_from_dict(data, keys, org)
                        self.set_page_url(value)
                        keys = ["web", "direct_url"]
                        org = self.get_direct_url()
                        value = self.get_from_dict(data, keys, org)
                        self.set_direct_url(value)
                        keys = ["web", "secondary_url"]
                        org = self.get_secondary_url()
                        value = self.get_from_dict(data, keys, org)
                        self.set_secondary_url(value)

                        # FILE
                        keys = ["file", "media_file"]
                        org = self.get_media_file()
                        value = self.get_from_dict(data, keys, org)
                        self.set_media_file(value)
                        keys = ["file", "secondary_file"]
                        org = self.get_secondary_file()
                        value = self.get_from_dict(data, keys, org)
                        self.set_secondary_file(value)
                        keys = ["file", "previous_ids"]
                        org = self.get_previous_ids()
                        value = self.get_from_dict(data, keys, org)
                        self.set_previous_ids(value)
                        keys = ["file", "next_ids"]
                        org = self.get_next_ids()
                        value = self.get_from_dict(data, keys, org)
                        self.set_next_ids(value)
                        keys = ["file", "section_first"]
                        org = self.get_section_first()
                        value = self.get_from_dict(data, keys, org)
                        self.set_section_first(value)
                        keys = ["file", "section_last"]
                        org = self.get_section_last()
                        value = self.get_from_dict(data, keys, org)
                        self.set_section_last(value)

                        # USER
                        keys = ["user", "sequence_title"]
                        org = self.get_sequence_title()
                        value = self.get_from_dict(data, keys, org)
                        self.set_sequence_title(value)
                        keys = ["user", "section_title"]
                        org = self.get_section_title()
                        value = self.get_from_dict(data, keys, org)
                        self.set_section_title(value)
                        keys = ["user", "branch_titles"]
                        org = self.get_branch_titles()
                        value = self.get_from_dict(data, keys, org)
                        self.set_branch_titles(value)
                        keys = ["user", "rating"]
                        org = self.get_rating()
                        value = self.get_from_dict(data, keys, org)
                        self.set_rating(value)
                        keys = ["user", "views"]
                        org = self.get_views()
                        value = self.get_from_dict(data, keys, org)
                        self.set_views(value)
                        keys = ["user", "user_tags"]
                        org = self.get_user_tags()
                        value = self.get_from_dict(data, keys, org)
                        self.set_user_tags(value)
            except IOError:
                print("Error reading DVK")
                self.clear_dvk()

    def add_to_dict(
            self,
            dictionary: dict = None,
            key: str = None,
            value=None) -> dict:
        """
        Adds a key-value pair to dictionary unless values are invalid.

        Parameters:
            dictionary (dict): Dictionary of which to add values
            key (str): Dictionary key
            value(str): Value to pair to key

        Returns:
            dict: Dictionary with values added
        """
        return_dict = dictionary
        if dictionary is not None and key is not None and value is not None:
            return_dict[key] = value
        return return_dict

    def get_from_dict(
            self,
            dictionary: dict = None,
            keys: list = None,
            original=None):
        """
        Returns the value of a dictionary from given keys.

        Parameters:
            dictionary (dict): Dictionary to read from
            keys (list): List of keys to read from dictionary
            original: Original value to return if key or dictionary are invalid

        Returns:
            Value of dictionary from keys
        """
        result = original
        if dictionary is not None and keys is not None and not keys == []:
            cur_dict = dictionary
            try:
                for key in keys:
                    result = cur_dict[key]
                    cur_dict = result
            except KeyError:
                result = original
        return result

    def can_write(self) -> bool:
        """
        Returns whether the current DVK file is valid for writing.
        Returns false if DVK does not have enough information
        (No title, artists, etc.)

        Returns:
            bool: Whether the current DVK can be written to disk
        """
        if (self.get_file() is None
                or self.get_id() == ""
                or self.get_title() is None
                or self.get_artists() == []
                or self.get_page_url() is None
                or self.get_media_file() is None):
            return False
        return True

    def get_filename(self) -> str:
        """
        Returns a filename for the DVK based on its title and ID.

        Returns:
            str: Filename
        """
        if self.get_title() is None or self.get_id() == "":
            return ""
        return get_filename(self.get_title()) + '_' + self.get_id()

    def rename_files(self, filename: str = None):
        """
        Renames the current Dvk file and any linked media files.

        Parameters:
            filename (str): Name to rename files. If none, use default.
        """
        if (self.get_file() is not None and self.get_file().exists()):
            rfile = filename
            if filename is None:
                rfile = self.get_filename()
            parent = Path(self.get_file().parent)
            # RENAME DVK
            remove(str(self.get_file().absolute()))
            self.set_file(parent.joinpath(rfile + ".dvk"))
            # RENAME MEDIA FILE
            media = self.get_media_file()
            if media is not None and media.exists():
                num = 0
                extension = get_extension(str(media.absolute()))
                ifile = "xxtempXXTEMP" + self.get_id() + "_N"
                path = parent.joinpath(ifile + str(num) + extension)
                while path.exists():
                    num = num + 1
                    path = parent.joinpath(ifile + str(num) + extension)
                rename(media.absolute(), path.absolute())
                rpath = parent.joinpath(rfile + extension)
                rename(path.absolute(), rpath.absolute())
                self.set_media_file(parent.joinpath(rfile + extension))
            else:
                self.set_media_file("NULL-invalid-file.none")
            # RENAME SECONDARY FILE
            secondary = self.get_secondary_file()
            if secondary is not None and secondary.exists():
                num = 0
                extension = get_extension(str(secondary.absolute()))
                ifile = "xxtempXXTEMP" + self.get_id() + "_N"
                path = parent.joinpath(ifile + str(num) + extension)
                while path.exists():
                    num = num + 1
                    path = parent.joinpath(ifile + str(num) + extension)
                rename(secondary.absolute(), path.absolute())
                rpath = parent.joinpath(rfile + extension)
                rename(path.absolute(), rpath.absolute())
                self.set_secondary_file(parent.joinpath(rfile + extension))
            self.write_dvk()

    def set_file(self, file_path: str = None):
        """
        Sets the current path for the DVK file.

        Parameters:
            file_path (str): Path for the DVK file
        """
        if file_path is None or file_path == "":
            self.dvk_file = None
        else:
            self.dvk_file = Path(file_path)

    def get_file(self) -> Path:
        """
        Returns the current path of the DVK file.

        Returns:
            path: DVK file path
        """
        return self.dvk_file

    def generate_id(self, prefix: str = "", extra: str = ""):
        """
        Generates a psudorandom deterministic ID.
        Based on title, artists, and page URL.

        Parameters:
            prefix (str): String at the start of ID
            extra (str): Extra string for changing random seed
        """
        if (self.get_title() is not None
                and len(self.get_artists()) > 0
                and self.get_page_url() is not None):
            s = self.get_title() + str(self.get_artists())
            s = s + self.get_page_url() + extra
            seed(s)
            self.set_id(prefix + str(randint(1, 9999999999)))

    def set_id(self, id_str: str = None):
        """
        Sets the ID for the current DVK file.

        Parameters:
            id_str (str): DVK ID
        """
        if id_str is None:
            self.id = ""
        else:
            self.id = id_str.upper()

    def get_id(self) -> str:
        """
        Returns the ID for the current DVK file.

        Returns:
            str: DVK ID
        """
        return self.id.upper()

    def set_title(self, title_str: str = None):
        """
        Sets the title for the current DVK file.

        Parameters:
            title_str (str): DVK title
        """
        self.title = title_str

    def get_title(self) -> str:
        """
        Returns the title for the current DVK file.

        Returns:
            str: DVK title
        """
        return self.title

    def set_artist(self, artist_str: str = None):
        """
        Sets the artists for the current DVK file for just a single artist.

        Parameters:
            artist_str (str): DVK Artist
        """
        a_list = [artist_str]
        self.set_artists(a_list)

    def set_artists(self, artist_list: list = None):
        """
        Sets the artists for the current DVK file.

        Parameters:
            artist_list (list): DVK artists
        """
        if artist_list is None:
            self.artists = []
        else:
            self.artists = sorted(clean_list(artist_list))

    def get_artists(self) -> list:
        """
        Returns a list of artists for the current DVK file.

        Returns:
            list: DVK artists
        """
        return self.artists

    def set_time_int(
            self,
            year_int: int = 0,
            month_int: int = 0,
            day_int: int = 0,
            hour_int: int = 0,
            minute_int: int = 0):
        """
        Sets the Dvk's time published.
        Uses int values representing individual time units.

        Parameters:
            year_int (int): Int value of year published
            month_int (int): Int value of month published
            day_int (int): Int value of day published
            hour_int (int): Int value of hour published
            minute_int (int): Int value of minute published
        """
        if (year_int is None or year_int < 1
                or month_int is None or month_int < 1 or month_int > 12
                or day_int is None or day_int < 1 or day_int > 31
                or hour_int is None or hour_int < 0 or hour_int > 23
                or minute_int is None or minute_int < 0 or minute_int > 59):
            self.time = "0000/00/00|00:00"
        else:
            year_str = extend_int(year_int, 4)
            month_str = extend_int(month_int, 2)
            day_str = extend_int(day_int, 2)
            hour_str = extend_int(hour_int, 2)
            minute_str = extend_int(minute_int, 2)
            date = year_str + "/" + month_str + "/" + day_str
            self.time = date + "|" + hour_str + ":" + minute_str

    def set_time(self, time_str: str = None):
        """
        Sets the current Dvk's time published using a formatted time string.
        If time string is invalid, sets the date to 0000/00/00|00:00

        Parameters:
            time_str (str): String representation of time published.
                            Should be formatted: YYYY/MM/DD/hh/mm
        """
        if time_str is None or not len(time_str) == 16:
            self.time = "0000/00/00|00:00"
        else:
            try:
                year = int(time_str[0:4])
                month = int(time_str[5:7])
                day = int(time_str[8:10])
                hour = int(time_str[11:13])
                minute = int(time_str[14:16])
                self.set_time_int(year, month, day, hour, minute)
            except ValueError:
                self.time = "0000/00/00|00:00"

    def get_time(self) -> str:
        """
        Returns the time published for the current DVK file.

        Returns:
            str: Time string of the time published for the DVK file
        """
        return self.time

    def set_web_tags(self, web_tag_list: list = None):
        """
        Sets the web tags for the current DVK file.

        Parameters:
            web_tag_list (list): DVK web tags
        """
        if web_tag_list is None or web_tag_list == []:
            self.web_tags = None
        else:
            self.web_tags = clean_list(web_tag_list)

    def get_web_tags(self) -> list:
        """
        Returns the web tags for the current DVK file.

        Returns:
            list: DVK web tags
        """
        return self.web_tags

    def set_description(self, description_str: str = None):
        """
        Sets the description for the current DVK file.

        Parameters:
            description_str (str): DVK description
        """
        if description_str is None or description_str == "":
            self.description = None
        else:
            self.description = add_escapes_to_html(description_str)

    def get_description(self) -> str:
        """
        Returns the description for the current DVK file.

        Returns:
            str: DVK description
        """
        return self.description

    def set_page_url(self, page_url_str: str = None):
        """
        Sets the page URL for the current DVK file.

        Parameters:
            page_url_str (str): Page URL
        """
        if page_url_str == "":
            self.page_url = None
        else:
            self.page_url = page_url_str

    def get_page_url(self) -> str:
        """
        Returns the page URL for the current DVK file.

        Returns:
            str: Page URL
        """
        return self.page_url

    def set_direct_url(self, direct_url_str: str = None):
        """
        Sets the direct media URL for the current DVK file.

        Parameters:
            direct_url_str (str): Direct media URL
        """
        if direct_url_str == "":
            self.direct_url = None
        else:
            self.direct_url = direct_url_str

    def get_direct_url(self) -> str:
        """
        Returns the direct media URL for the current DVK file.

        Returns:
            str: Direct media URL
        """
        return self.direct_url

    def set_secondary_url(self, secondary_url_str: str = None):
        """
        Sets the secondary media URL for the current DVK file.

        Parameters:
            secondary_url_str (str): Secondary media URL
        """
        if secondary_url_str == "":
            self.secondary_url = None
        else:
            self.secondary_url = secondary_url_str

    def get_secondary_url(self) -> str:
        """
        Returns the secondary media URL for the current DVK file.

        Returns:
            str: Secondary media URL
        """
        return self.secondary_url

    def set_media_file(self, file_name: str = None):
        """
        Sets the media file for the current DVK file based on a given filename.
        Sets file in the same directory as the DVK file.

        Parameters:
            file_name (str): Media filename for the current DVK file
        """
        if file_name is None or file_name == "" or self.get_file() is None:
            self.media_file = None
        else:
            parent = Path(self.get_file().parent)
            self.media_file = parent.joinpath(file_name).absolute()

    def get_media_file(self) -> Path:
        """
        Returns the media file for the current DVK file.

        Returns:
            path: DVK media file
        """
        return self.media_file

    def set_secondary_file(self, file_name: str = None):
        """
        Sets the secondary media file for the current DVK file.
        Sets file in the same directory as the DVK file.

        Parameters:
            file_name (str): Secondary media filename for the current DVK file
        """
        if file_name is None or file_name == "" or self.get_file() is None:
            self.secondary_file = None
        else:
            parent = Path(self.get_file().parent)
            self.secondary_file = parent.joinpath(file_name).absolute()

    def get_secondary_file(self) -> Path:
        """
        Returns the secondary media file for the current DVK file.

        Returns:
            path: DVK secondary media file
        """
        return self.secondary_file

    def set_previous_ids(self, id_list: list = None):
        """
        Sets the IDs of the previous DVK files in a DVK sequence.

        Parameters:
            id_list (list): List of IDs for previous DVK files
        """
        if id_list is None:
            self.previous_ids = None
        else:
            count = 0
            self.previous_ids = []
            while count < len(id_list):
                if id_list[count] is None or id_list[count] == "":
                    self.previous_ids = []
                    break
                else:
                    self.previous_ids.append(id_list[count].upper())
                count = count + 1

    def get_previous_ids(self) -> list:
        """
        Returns a list of IDs for the previous DVK files in a DVK sequence.

        Returns:
            list: IDs of previous DVK files
        """
        return self.previous_ids

    def set_next_ids(self, id_list: list = None):
        """
        Sets the IDs of the next DVK files in a DVK sequence.

        Parameters:
            id_list (list): List of IDs for next DVK files
        """
        if id_list is None:
            self.next_ids = None
        else:
            count = 0
            self.next_ids = []
            while count < len(id_list):
                if id_list[count] is None or id_list[count] == "":
                    self.next_ids = []
                    break
                else:
                    self.next_ids.append(id_list[count].upper())
                count = count + 1

    def get_next_ids(self) -> list:
        """
        Returns a list of IDs for the next DVK files in a DVK sequence.

        Returns:
            list: IDs of next DVK files
        """
        return self.next_ids

    def set_section_first(self, first_bool: bool = False):
        """
        Sets whether current DVK is the first in a sequence section.

        Parameters:
            first_bool (bool): Whether DVK is first in a section
        """
        self.section_first = first_bool
        self.section_first = self.get_section_first()

    def get_section_first(self) -> bool:
        """
        Returns whether current DVK is the first in a sequence section.

        Returns:
            bool: Whether DVK is first in a section
        """
        if (self.section_first
                and self.get_previous_ids() is not None
                and self.get_next_ids() is not None):
            if (not self.get_previous_ids() == []
                    or not self.get_next_ids() == []):
                return True
        return False

    def set_section_last(self, last_bool: bool = False):
        """
        Sets whether current DVK is the last in a sequence section.

        Parameters:
            first_bool (bool): Whether DVK is last in a section
        """
        self.section_last = last_bool
        self.section_last = self.get_section_last()

    def get_section_last(self) -> bool:
        """
        Returns whether current DVK is the last in a sequence section.

        Returns:
            bool: Whether DVK is last in a section
        """
        if (self.section_last
                and self.get_previous_ids() is not None
                and self.get_next_ids() is not None):
            if (not self.get_previous_ids() == []
                    or not self.get_next_ids() == []):
                return True
        return False

    def set_sequence_title(self, sequence_title_str: str = None):
        """
        Sets the sequence title for the current DVK file.

        Parameters:
            sequence_title (str): DVK sequence title
        """
        self.sequence_title = sequence_title_str
        self.sequence_title = self.get_sequence_title()

    def get_sequence_title(self) -> str:
        """
        Returns the sequence title for the current DVK file.

        Returns:
            str: DVK sequence title
        """
        if (not self.sequence_title == ""
                and self.get_previous_ids() is not None
                and self.get_next_ids() is not None):
            if (not self.get_previous_ids() == []
                    or not self.get_next_ids() == []):
                return self.sequence_title
        return None

    def set_section_title(self, section_title_str: str = None):
        """
        Sets the sequence section title for the current DVK file.

        Parameters:
            section_title (str): DVK sequence section title
        """
        self.section_title = section_title_str
        self.section_title = self.get_section_title()

    def get_section_title(self) -> str:
        """
        Return the sequence section title for the current DVK file.

        Returns:
            str: DVK sequence section title
        """
        if (not self.section_title == ""
                and self.get_previous_ids() is not None
                and self.get_next_ids() is not None):
            if (not self.get_previous_ids() == []
                    or not self.get_next_ids() == []):
                return self.section_title
        return None

    def set_branch_titles(self, branch_title_list: list = None):
        """
        Sets sequence branch titles for the current DVK file.

        Parameters:
            branch_title_list (list): List of DVK sequence branch titles
        """
        if (branch_title_list is None
                or branch_title_list == []
                or self.get_next_ids() is None
                or len(branch_title_list) < 2
                or not len(branch_title_list) == len(self.get_next_ids())):
            self.branch_titles = None
        else:
            self.branch_titles = branch_title_list

    def get_branch_titles(self) -> list:
        """
        Returns sequence branch titles for the current DVK file.

        Returns:
            list: DVK sequence branch titles
        """
        return self.branch_titles

    def set_rating(self, rating_int: int = 0):
        """
        Sets the rating for the current DVK file, from 1 to 5.

        Parameters:
            rating_int (int): DVK rating
        """
        if (rating_int is None
                or rating_int < 0
                or rating_int > 5):
            self.rating = 0
        else:
            self.rating = rating_int

    def get_rating(self) -> int:
        """
        Returns the rating for the current DVK file.

        Returns:
            int: DVK rating
        """
        return self.rating

    def set_views(self, view_int: int = 0):
        """
        Sets the number of views for the current DVK file.

        Parameters:
            view_int (int): DVK views
        """
        if view_int is None or view_int < 0:
            self.views = 0
        else:
            self.views = view_int

    def get_views(self) -> int:
        """
        Returns the number of views for the current DVK file.

        Returns:
            int: DVK views
        """
        return self.views

    def set_user_tags(self, user_tag_list: list = None):
        """
        Sets the user tags for the current DVK file.

        Parameters:
            user_tag_list (list): DVK web tags
        """
        if user_tag_list is None or user_tag_list == []:
            self.user_tags = None
        else:
            self.user_tags = clean_list(user_tag_list)

    def get_user_tags(self) -> list:
        """
        Returns the user tags for the current DVK file.

        Returns:
            list: DVK user tags
        """
        return self.user_tags
