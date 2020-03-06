from pathlib import Path
from dvk_archive.file.dvk import Dvk


class DvkDirectory:
    """
    Class for handling all the DVK files within a given directory.

    Parameters:
        directory_path (Path): Path of DVK directory
        group_artists (bool): Whether to group DVKs of the same artist together
        dvks (list): List of Dvk objects read from directory_path
    """

    def __init__(self):
        """
        Initializes the DvkDirectory class.
        """
        self.directory_path = Path()
        self.group_artists = False
        self.dvks = []

    def read_dvks(self, directory_str: str = None):
        """
        Reads all of the DVK files in a given directory.
        Add DVKs to dvk list.

        Parameters:
            directory_str (str): String path of the DVK directory
        """
        self.dvks = []
        if directory_str is not None and not directory_str == "":
            self.directory_path = Path(directory_str)
            dvk_files = self.directory_path.glob("*.dvk")
            for dvk_file in dvk_files:
                dvk = Dvk()
                dvk.set_file(dvk_file.absolute())
                dvk.read_dvk()
                self.dvks.append(dvk)

    def get_size(self) -> int:
        """
        Returns the size of the dvks list.

        Returns:
            int: Size of the dvks list.
        """
        if self.dvks is None:
            return 0
        else:
            return len(self.dvks)

    def get_dvk(self, index_int: int = 0) -> Dvk:
        """
        Returns the Dvk object from the dvks list of the given index.
        If index is out of range, returns a default DVK.

        Returns:
            Dvk: Dvk object from the given index
        """
        if (index_int is None
                or index_int < 0
                or not index_int < self.get_size()):
            return Dvk()
        else:
            return self.dvks[index_int]
