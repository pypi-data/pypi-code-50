import os
import random
import shutil
from unittest import TestCase, mock
from unittest.mock import patch

import faker
import src.tests.blockbuster as blockbuster
import utils

module_under_test = "utils"

fake = faker.Faker()


class UtilsTestCase(TestCase):
    """
    Checks that all methods in the `utils` module work correctly.
    """

    def setUp(self):
        test_environment = blockbuster.BlockBusterBuilder(
            level="pg-13",
            test_folder=blockbuster.TEST_INPUT_FOLDER,
            file_extensions=[".file"],
            use_extensions=True,
        )
        self.test_folder, self.example_titles = (
            test_environment.create_empty_environment()
        )

    def tearDown(self):
        shutil.rmtree(self.test_folder)

    def test_listdir_fullpath(self):
        """

        Ensures the full path of every file or folder is returned in a given directory
        when the `listdir_fullpath() method is called.
        """
        fake_filepaths = []
        min_value = 0
        max_value = 10
        iterations = fake.pyint(min_value=min_value, max_value=max_value)
        root = self.test_folder

        for iteration in range(iterations):
            filename = fake.word()
            fake_filepath = os.path.join(root, filename)
            fake_filepaths.append(fake_filepath)
            os.makedirs(fake_filepath)

        test_filepaths = utils.listdir_fullpath(directory=root)

        self.assertEqual(sorted(test_filepaths), sorted(fake_filepaths))

    def test_is_in_list_with_list(self):
        """Ensures the `is_in_list()` method returns True when an element is in a list and False when it is not."""
        element_in_list = fake.word()
        element_not_in_list = fake.word()
        the_list = [fake.word(), element_in_list]
        self.assertTrue(utils.is_in_list(element=element_in_list, the_list=the_list))
        self.assertFalse(
            utils.is_in_list(element=element_not_in_list, the_list=the_list)
        )

    def test_is_in_list_with_list_of_lists(self):
        """Ensures the `is_in_list()` method returns True when an element is in a list of lists and False when it is not."""
        element_in_list = fake.word()
        element_not_in_list = fake.word()
        the_list = [fake.word(), element_in_list]
        list_of_lists = [the_list]
        self.assertTrue(
            utils.is_in_list(element=element_in_list, the_list=list_of_lists)
        )
        self.assertFalse(
            utils.is_in_list(element=element_not_in_list, the_list=list_of_lists)
        )

    def test_is_in_folder(self):
        """Ensures the `is_in_folder()` method returns True when a file is in a given folder."""
        file_in_list = fake.word()
        file_not_in_list = fake.word()
        folder_to_write = os.path.join(self.test_folder, file_in_list)
        folder_not_to_write = os.path.join(self.test_folder, file_not_in_list)
        os.makedirs(folder_to_write)
        file_to_write = os.path.join(folder_to_write, file_in_list)
        open(file_to_write, "wb").close()

        self.assertTrue(utils.is_in_folder(path=folder_to_write, name=file_in_list))
        self.assertFalse(
            utils.is_in_folder(path=folder_to_write, name=file_not_in_list)
        )
        self.assertFalse(
            utils.is_in_folder(path=folder_not_to_write, name=file_not_in_list)
        )

    def test_find_single_files(self):
        """Ensures the `find_single_files()` method returns all the single files in a given directory."""
        fake_single_files = []
        min_value = 0
        max_value = 10
        iterations = fake.pyint(min_value=min_value, max_value=max_value)
        root = self.test_folder

        for iteration in range(iterations):
            fake_single_filename = fake.word()
            fake_single_filepath = os.path.join(root, fake_single_filename)
            fake_single_files.append(fake_single_filename)
            open(fake_single_filepath, "wb").close()

        test_single_files = utils.find_single_files(directory=root)
        self.assertEqual(sorted(test_single_files), sorted(fake_single_files))

    def test_find_folders(self):
        """Ensures the `find_folders()` method returns all the folders in a given directory."""
        fake_folders = []
        min_value = 0
        max_value = 10
        iterations = fake.pyint(min_value=min_value, max_value=max_value)
        root = self.test_folder

        for iteration in range(iterations):
            fake_folder_name = fake.word()
            fake_folder_path = os.path.join(root, fake_folder_name)
            fake_folders.append(fake_folder_path)
            os.makedirs(fake_folder_path)

        test_folders = utils.find_folders(directory=root)
        self.assertEqual(sorted(test_folders), sorted(fake_folders))

    def test_get_parent_and_child(self):
        """Ensures the `get_parent_and_child()` method returns the correct parent and child file or folder names."""
        fake_parent_path = os.path.join(self.test_folder, fake.word())
        fake_child_name = fake.word()
        # os.makedirs(fake_parent_path)
        fake_filepath = os.path.join(fake_parent_path, fake_child_name)
        test_parent_path, test_child = utils.get_parent_and_child(path=fake_filepath)
        self.assertEqual(test_parent_path, fake_parent_path)
        self.assertEqual(test_child, fake_child_name)

    def test_silent_remove_if_folder_exists(self):
        """Ensures the `silent_remove()` method removes the given folder, if the given folder exists."""
        fake_folder_name = fake.word()
        fake_folder_path = os.path.join(self.test_folder, fake_folder_name)
        os.makedirs(fake_folder_path)
        self.assertTrue(os.path.exists(fake_folder_path))
        utils.silent_remove(path=fake_folder_path)
        self.assertFalse(os.path.exists(fake_folder_path))

    # def test_silent_remove_raises_oserror_if_folder_does_not_exist(self):
    #     """Ensures the `silent_remove()` method raises OSError, if the given folder does not exist."""
    #     fake_folder_name = fake.word()
    #     fake_folder_path = os.path.join(self.test_folder, fake_folder_name)
    #     self.assertFalse(os.path.exists(fake_folder_path))
    #     try:
    #         utils.silent_remove(path=fake_folder_path)
    #     except Exception as error:
    #         self.assertIsInstance(error, OSError)

    def test_silent_remove_if_file_exists(self):
        """Ensures the `silent_remove()` method removes the given file, if the given file exists."""
        fake_filename = fake.word()
        fake_filepath = os.path.join(self.test_folder, fake_filename)
        open(fake_filepath, "wb").close()
        self.assertTrue(os.path.exists(fake_filepath))
        self.assertTrue(os.path.isfile(fake_filepath))
        utils.silent_remove(path=fake_filepath)
        self.assertFalse(os.path.exists(fake_filepath))

    # def test_silent_remove_raises_oserror_if_file_does_not_exist(self):
    #     """Ensures the `silent_remove()` method raises OSError, if the given file does not exist."""
    #     fake_filename = fake.word()
    #     fake_filepath = os.path.join(self.test_folder, fake_filename)
    #     test_error = None
    #     self.assertFalse(os.path.exists(fake_filepath))
    #     try:
    #         utils.silent_remove(path=fake_filepath)
    #     except Exception as error:
    #         test_error = error

    #    self.assertIsInstance(test_error, OSError)

    # def test_silent_remove_raises_oserror_if_file_exists_and_is_open(self):
    #     """Ensures the `silent_remove()` method raises OSError, if the given file exists, but is open while trying to remove it."""
    #     fake_filename = fake.word()
    #     fake_filepath = os.path.join(self.test_folder, fake_filename)
    #     test_error = None
    #     open(fake_filepath, "wb").close()
    #     self.assertTrue(os.path.exists(fake_filepath))
    #     self.assertTrue(os.path.isfile(fake_filepath))
    #     with open(fake_filepath, "wb"):
    #         try:
    #             utils.silent_remove(path=fake_filepath)
    #         except Exception as error:
    #             test_error = error
    #
    #     self.assertIsInstance(test_error, OSError)
    #     self.assertTrue(os.path.exists(fake_filepath))
    #     self.assertTrue(os.path.isfile(fake_filepath))

    def test_create_trimmed_file(self):
        """Ensures the `create_trimmed_file()` method trims the given file to the desired size."""
        root = self.test_folder
        fake_filename = fake.word()
        fake_filepath = os.path.join(root, fake_filename)
        fake_filesize = random.randrange(8, 257, 2)
        test_full_file_hash = utils.create_random_file(
            directory=root, filename=fake_filename, filesize=fake_filesize, units="kb"
        )
        # If you use a chunksize of
        test_trimmed_file_hash = utils.create_trimmed_file(
            filepath=fake_filepath, chunksize=int(fake_filesize / 2)
        )
        self.assertEqual(test_full_file_hash, test_trimmed_file_hash)
        test_trimmed_file_hash = utils.create_trimmed_file(
            filepath=fake_filepath, chunksize=int(fake_filesize / 4)
        )
        self.assertNotEqual(test_full_file_hash, test_trimmed_file_hash)
