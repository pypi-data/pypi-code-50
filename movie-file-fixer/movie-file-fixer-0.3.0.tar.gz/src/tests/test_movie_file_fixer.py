import json
import os
import random
import shutil
import sys
from unittest import TestCase, mock
from unittest.mock import patch

import faker
import src.tests.blockbuster as blockbuster
import utils

import movie_file_fixer

module_under_test = "movie_file_fixer"

fake = faker.Faker()


class MovieFileFixerTestCase(TestCase):
    """
    Checks that upon instantiation with a valid directory string, all methods are being called.
    """

    def setUp(self):
        # To suppress the stdout by having verbose=True on MovieFileFixer instantiation:
        self.mock_print_patch = mock.patch("builtins.print")
        self.mock_print = self.mock_print_patch.start()

    def tearDown(self):
        self.mock_print_patch.stop()

    # TODO: Fix this failing test
    # def test_parse_args_with_real_data(self):
    #     """Ensure the `parse_args() method sets the Namespace object attributes correctly with realistic data."""
    #     directory = blockbuster.TEST_INPUT_FOLDER
    #     file_extensions = [
    #         ".idx",
    #         ".sub",
    #         ".nfo",
    #         ".dat",
    #         ".jpg",
    #         ".png",
    #         ".txt",
    #         ".exe",
    #     ]
    #     metadata_filename = "metadata.json"
    #     language = "en"
    #     test_parser = movie_file_fixer.parse_args(
    #         [
    #             "-d",
    #             directory,
    #             "-e",
    #             ".idx",
    #             "-e",
    #             ".sub",
    #             "-e",
    #             ".nfo",
    #             "-e",
    #             ".dat",
    #             "-e",
    #             ".jpg",
    #             "-e",
    #             ".png",
    #             "-e",
    #             ".txt",
    #             "-e",
    #             ".exe",
    #             "-f",
    #             metadata_filename,
    #             "-v",
    #         ]
    #     )
    #     self.assertEqual(test_parser.directory, directory)
    #     self.assertEqual(test_parser.file_extensions, file_extensions)
    #     self.assertEqual(test_parser.metadata_filename, metadata_filename)
    #     self.assertEqual(test_parser.language, language)
    #     self.assertTrue(test_parser.verbose)

    # TODO: Fix this failing test
    # def test_parse_args_with_fake_data(self):
    #     """Ensure the `parse_args() method sets the Namespace object attributes correctly with completely fake data."""
    #     fake_directory = os.path.join(fake.word(), fake.word(), fake.word())
    #     fake_file_extensions = [
    #         "." + word for word in [fake.word(), fake.word(), fake.word()]
    #     ]
    #     fake_metadata_filename = ".".join([fake.word(), fake.word()])
    #     test_parser = movie_file_fixer.parse_args(
    #         [
    #             "-d",
    #             fake_directory,
    #             "-e",
    #             fake_file_extensions[0],
    #             "-e",
    #             fake_file_extensions[1],
    #             "-e",
    #             fake_file_extensions[2],
    #             "-f",
    #             fake_metadata_filename,
    #             "-v",
    #         ]
    #     )
    #     self.assertEqual(test_parser.directory, fake_directory)
    #     self.assertEqual(test_parser.file_extensions, fake_file_extensions)
    #     self.assertEqual(test_parser.metadata_filename, fake_metadata_filename)
    #     self.assertTrue(test_parser.verbose)

    @patch(f"{module_under_test}.MovieFileFixer.get_subtitles")
    @patch(f"{module_under_test}.MovieFileFixer.get_posters")
    @patch(f"{module_under_test}.MovieFileFixer.format")
    @patch(f"{module_under_test}.MovieFileFixer.cleanup")
    @patch(f"{module_under_test}.MovieFileFixer.folderize")
    def test_all_modules_are_not_called_upon_instantiation(
        self,
        folderize_method_patch,
        cleanup_method_patch,
        format_method_patch,
        get_posters_method_patch,
        get_subtitles_method_patch,
    ):
        """Ensure the `folderize()` method is not being called when a valid instance of `MovieFileFixer` is instantiated."""
        movie_file_fixer.MovieFileFixer(directory=blockbuster.TEST_INPUT_FOLDER)
        folderize_method_patch.assert_not_called()
        cleanup_method_patch.assert_not_called()
        format_method_patch.assert_not_called()
        get_posters_method_patch.assert_not_called()
        get_subtitles_method_patch.assert_not_called()

    @patch(f"{module_under_test}.MovieFileFixer.get_subtitles")
    @patch(f"{module_under_test}.MovieFileFixer.get_posters")
    @patch(f"{module_under_test}.MovieFileFixer.format")
    @patch(f"{module_under_test}.MovieFileFixer.cleanup")
    @patch(f"{module_under_test}.MovieFileFixer.folderize")
    def test_all_modules_are_called_from_main(
        self,
        folderize_method_patch,
        cleanup_method_patch,
        format_method_patch,
        get_posters_method_patch,
        get_subtitles_method_patch,
    ):
        """

        Ensure the `folderize()`, `cleanup()`, `format()`, `get_posters()`, and `get_subtitles()`
        methods are being called when a valid instance of `MovieFileFixer` is instantiated when `main()`
        is called.
        """
        fake_directory = os.path.join(fake.word(), fake.word(), fake.word())
        fake_file_extensions = [
            "." + word for word in [fake.word(), fake.word(), fake.word()]
        ]
        fake_metadata_filename = ".".join([fake.word(), fake.word()])
        test_args = [
            f"{module_under_test}",
            "-d",
            fake_directory,
            "-e",
            fake_file_extensions[0],
            "-e",
            fake_file_extensions[1],
            "-e",
            fake_file_extensions[2],
            "-f",
            fake_metadata_filename,
            "-v",
        ]
        with patch.object(sys, "argv", test_args):
            movie_file_fixer.main()
        folderize_method_patch.assert_called_once()
        cleanup_method_patch.assert_called_once()
        format_method_patch.assert_called_once()
        get_posters_method_patch.assert_called_once()
        get_subtitles_method_patch.assert_called_once()

    @patch(f"{module_under_test}.Folderizer.unfolderize")
    @patch(f"{module_under_test}.Folderizer.folderize")
    def test_folderizer_folderize_and_unfolderize_are_called(
        self, folderize_method_patch, unfolderize_method_patch
    ):
        """Ensure that the `Folderize.folderize()` and `Folderizer.unfolderize()` methods are called when `MovieFileFixer.folderize() is called."""
        movie_file_fixer_instance = movie_file_fixer.MovieFileFixer(
            directory=blockbuster.TEST_INPUT_FOLDER
        )
        movie_file_fixer_instance.folderize()
        folderize_method_patch.assert_called_once()
        unfolderize_method_patch.assert_called_once()

    @patch(f"{module_under_test}.FileRemover.remove_files")
    def test_file_remover_remove_files_is_called(self, remove_files_method_patch):
        """Ensure that the `FileRemove.remove_files()` method is called when `MovieFileFixer.cleanup() is called."""
        movie_file_fixer_instance = movie_file_fixer.MovieFileFixer(
            directory=blockbuster.TEST_INPUT_FOLDER
        )
        movie_file_fixer_instance.cleanup()
        remove_files_method_patch.assert_called_once()

    @patch(f"{module_under_test}.Formatter.format")
    def test_formatter_format_is_called(self, format_method_patch):
        """Ensure that the `Formatter.format()` method is called when `MovieFileFixer.format() is called."""
        movie_file_fixer_instance = movie_file_fixer.MovieFileFixer(
            directory=blockbuster.TEST_INPUT_FOLDER
        )
        movie_file_fixer_instance.format()
        format_method_patch.assert_called_once()

    @patch(f"{module_under_test}.PosterFinder.get_posters")
    def test_posterfinder_get_posters_is_called(self, get_posters_method_patch):
        """Ensure that the `PosterFinder.get_posters()` method is called when `MovieFileFixer.get_posters() is called."""
        movie_file_fixer_instance = movie_file_fixer.MovieFileFixer(
            directory=blockbuster.TEST_INPUT_FOLDER
        )
        movie_file_fixer_instance.get_posters()
        get_posters_method_patch.assert_called_once()

    @patch(f"{module_under_test}.SubtitleFinder.get_subtitles")
    def test_subtitlefinder_get_subtitles_is_called(self, get_subtitles_method_patch):
        """Ensure that the `SubtitleFinder.get_subtitles()` method is called when `MovieFileFixer.get_subtitles() is called."""
        movie_file_fixer_instance = movie_file_fixer.MovieFileFixer(
            directory=blockbuster.TEST_INPUT_FOLDER
        )
        movie_file_fixer_instance.get_subtitles()
        get_subtitles_method_patch.assert_called_once()


class FolderizerTestCase(TestCase):
    def setUp(self):
        # To suppress the stdout by having verbose=True on Folderizer instantiation:
        self.mock_print_patch = mock.patch("builtins.print")
        self.mock_print = self.mock_print_patch.start()

        test_environment = blockbuster.BlockBusterBuilder(
            level="pg-13",
            test_folder=blockbuster.TEST_INPUT_FOLDER,
            file_extensions=[".file"],
            use_extensions=True,
        )
        self.test_folder, self.example_titles = (
            test_environment.create_single_file_environment()
        )
        self.folderizer = movie_file_fixer.Folderizer(
            directory=blockbuster.TEST_INPUT_FOLDER, verbose=True
        )
        self.single_files = self.folderizer._find_single_files()

    def tearDown(self):
        shutil.rmtree(self.test_folder)
        self.mock_print_patch.stop()

    def test_find_single_files(self):
        """Ensure all single files that were created were found."""
        for single_file in self.single_files:
            if single_file != blockbuster.METADATA_FILENAME:
                filename, extension = os.path.splitext(single_file)
                filename_is_in_list = utils.is_in_list(
                    element=filename, the_list=self.example_titles
                )
                self.assertTrue(filename_is_in_list)

    def test_move_files_into_folders(self):
        """Ensure that all single files that were created moved to folders of the same name."""
        self.folderizer._move_files_into_folders(filenames=self.single_files)
        for single_file in self.single_files:
            filename, extension = os.path.splitext(single_file)
            folder_name = os.path.join(blockbuster.TEST_INPUT_FOLDER, filename)
            new_filename = os.path.join(folder_name, single_file)

            # Ensure it's no longer a file:
            self.assertFalse(os.path.isfile(folder_name))
            # But it still exists (as a folder):
            self.assertTrue(os.path.exists(folder_name))
            # And also as a file inside that folder:
            self.assertTrue(os.path.isfile(new_filename))

    @patch(f"{module_under_test}.Folderizer._move_files_into_folders")
    @patch(f"{module_under_test}.Folderizer._find_single_files")
    def test_folderize(
        self, find_single_files_method_patch, move_files_into_folders_method_patch
    ):
        """Ensure all internal methods got called when the folderize() method was called."""
        self.folderizer.folderize()
        find_single_files_method_patch.assert_called_once()
        move_files_into_folders_method_patch.assert_called_once()

    def test_unfolderize(self):
        """Ensure all files inside a given directory get unfolderized."""
        fake_folder_name = fake.word()
        fake_filename = fake.word()
        fake_file_extension = "." + fake.word()
        self.folderizer.folderize()
        # Set up the test area inside each folder by creating an arbitrary file
        # with an arbitrary file extension inside an arbitrary folder:
        for root, dirs, files in os.walk(blockbuster.TEST_INPUT_FOLDER):
            new_folder_name = os.path.join(root, fake_folder_name)
            os.mkdir(new_folder_name)
            new_filename = os.path.join(
                new_folder_name, fake_filename + fake_file_extension
            )
            open(new_filename, "a").close()

            # Test that the setup worked and created the file in the correct place:
            should_not_exist = os.path.join(root, fake_filename + fake_file_extension)
            # It is not a single file name in the movie folder:
            self.assertFalse(os.path.isfile(should_not_exist))
            # It is a folder name however:
            self.assertTrue(os.path.exists(new_folder_name))
            # and also a file name inside that folder:
            self.assertTrue(os.path.isfile(new_filename))

        self.folderizer.unfolderize(folder_name=fake_folder_name)

        for root, dirs, files in os.walk(blockbuster.TEST_INPUT_FOLDER):
            new_folder_name = os.path.join(root, fake_folder_name)
            new_filename = os.path.join(
                new_folder_name, fake_filename + fake_file_extension
            )

            # Test that unfolderize pulled the files out of the folder and deleted the folder:
            should_exist_now = os.path.join(root, fake_filename + fake_file_extension)
            # Now it is a single file name in the movie folder (unfolderized):
            self.assertTrue(os.path.isfile(should_exist_now))
            # and no longer a folder name (folder is deleted):
            self.assertFalse(os.path.exists(new_folder_name))
            # nor is it a single file inside that folder:
            self.assertFalse(os.path.isfile(new_filename))

    def test_unfolderize_all(self):
        """This test does nothing until we've implemented that method."""
        fake_result = self.folderizer.unfolderize_all()
        self.assertEqual(fake_result, None)


class FileRemoverTestCase(TestCase):
    def setUp(self):
        # To suppress the stdout by having verbose=True on FileRemover instantiation:
        self.mock_print_patch = mock.patch("builtins.print")
        self.mock_print = self.mock_print_patch.start()

        self.good_file_extensions = [".avi", ".mov", ".mp4", ".mkv", ".srt"]
        self.bad_file_extensions = [
            ".txt",
            ".dat",
            ".nfo",
            ".bmp",
            ".gif",
            ".jpg",
            ".png",
            ".exe",
        ]
        test_environment = blockbuster.BlockBusterBuilder(
            level="pg-13",
            test_folder=blockbuster.TEST_INPUT_FOLDER,
            file_extensions=self.good_file_extensions + self.bad_file_extensions,
            use_extensions=True,
        )
        self.test_folder, self.example_titles = (
            test_environment.create_single_file_environment()
        )
        self.file_remover = movie_file_fixer.FileRemover(
            directory=blockbuster.TEST_INPUT_FOLDER,
            file_extensions=self.bad_file_extensions,
            verbose=True,
        )

    def tearDown(self):
        shutil.rmtree(self.test_folder)
        self.mock_print_patch.stop()

    def test_remove_files(self):
        """Ensure all files with `bad_extensions` are removed."""
        self.file_remover.remove_files()
        for root, dirs, files in os.walk(self.test_folder):
            for file in files:
                filename, extension = os.path.splitext(file)
                self.assertIn(extension, self.good_file_extensions)
                self.assertNotIn(extension, self.bad_file_extensions)


class FormatterTestCase(TestCase):
    def setUp(self):
        # To suppress the stdout by having verbose=True on Formatter instantiation:
        self.mock_print_patch = mock.patch("builtins.print")
        self.mock_print = self.mock_print_patch.start()

        self.file_extensions = [".file"]
        test_environment = blockbuster.BlockBusterBuilder(
            level="pg-13",
            test_folder=blockbuster.TEST_INPUT_FOLDER,
            file_extensions=self.file_extensions,
            use_extensions=True,
        )
        self.test_folder, self.example_titles = (
            test_environment.create_folderized_environment()
        )
        self.formatter = movie_file_fixer.Formatter(
            directory=blockbuster.TEST_INPUT_FOLDER,
            metadata_filename=blockbuster.METADATA_FILENAME,
            verbose=True,
        )

    def tearDown(self):
        shutil.rmtree(self.test_folder)
        self.mock_print_patch.stop()

    def test_initialize_metadata_file_if_nonexistent(self):
        """Ensures metadata file is created and initialized if non-existent."""
        metadata_filepath = os.path.join(
            self.test_folder, blockbuster.METADATA_FILENAME
        )

        # Ensure the file doesn't already exist in the test folder:
        if os.path.exists(metadata_filepath):
            os.remove(metadata_filepath)

        # Ensure there is no metadata file:
        self.assertFalse(os.path.exists(metadata_filepath))

        # Now, this should create a new metadata file:
        metadata_file = self.formatter.initialize_metadata_file()

        # So let's ensure that that is indeed created:
        self.assertTrue(os.path.exists(metadata_filepath))

        # and that it's a new metadata file (all lists should be empty:
        empty_list = []
        test_titles = metadata_file.get("titles")
        test_metadata = metadata_file.get("metadata")
        test_errors = metadata_file.get("errors")
        self.assertListEqual(test_titles, empty_list)
        self.assertListEqual(test_metadata, empty_list)
        self.assertListEqual(test_errors, empty_list)

    def test_initialize_metadata_file_if_existent(self):
        """Ensures metadata file is initialized if it does exist."""
        metadata_filepath = os.path.join(
            self.test_folder, blockbuster.METADATA_FILENAME
        )

        # Ensure the file doesn't already exist in the test folder:
        if os.path.exists(metadata_filepath):
            os.remove(metadata_filepath)

        # Ensure there is no metadata file:
        self.assertFalse(os.path.exists(metadata_filepath))

        # Now, let's create a file with some fake "pre-existing" contents:
        fake_titles = fake.words()
        fake_metadata = fake.words()
        fake_errors = fake.words()
        metadata = {
            "titles": fake_titles,
            "metadata": fake_metadata,
            "errors": fake_errors,
        }
        with open(os.path.join(metadata_filepath), mode="w") as outfile:
            json.dump(metadata, outfile, indent=4)

        # Ensure this file does indeed exist now:
        self.assertTrue(os.path.exists(metadata_filepath))

        # Now, this should not create a new one:
        metadata_file = self.formatter.initialize_metadata_file()

        # So let's ensure the file was initialized correctly:
        test_titles = metadata_file.get("titles")
        test_metadata = metadata_file.get("metadata")
        test_errors = metadata_file.get("errors")
        self.assertListEqual(test_titles, fake_titles)
        self.assertListEqual(test_metadata, fake_metadata)
        self.assertListEqual(test_errors, fake_errors)

    def test_strip_punctuation(self):
        """

        Ensures all punctuation that might confused the search method are stripped
        from the given phrase.
        """

        # Punctuation characters that confuse the search method:
        punctuation_characters = ".-_"
        # Convert the random phrase string to a list to do insertions (without any initial punctuation:
        random_phrase = " ".join(fake.words())
        random_phrase_list = list(random_phrase)

        # Put a random punctuation character in place of every space
        for i in range(len(random_phrase_list) - 1):
            if random_phrase_list[i] == " ":
                # Choose a random punctuation character:
                random_punctuation_character_index = fake.pyint(
                    min_value=0, max_value=len(punctuation_characters) - 1
                )
                random_punctuation_character = punctuation_characters[
                    random_punctuation_character_index
                ]
                random_phrase_list[i] = random_punctuation_character

        test_punctuated_phrase = "".join(random_phrase_list)

        test_depunctuated_phrase = self.formatter._strip_punctuation(
            phrase=test_punctuated_phrase
        )

        self.assertEqual(test_depunctuated_phrase, random_phrase.lower())

    def test_get_release_year_from_search_terms_with_a_release_year(self):
        """Ensure release year can be found."""
        release_year = fake.year()
        random_text = fake.sentence()
        more_random_text = fake.sentence()
        search_terms = " ".join([random_text, release_year, more_random_text])

        test_release_year = self.formatter._get_release_year(search_terms=search_terms)

        self.assertEqual(release_year, test_release_year)

    def test_get_release_year_from_search_terms_without_a_release_year(self):
        """Ensure release year can be found."""
        release_year = None
        random_text = fake.sentence()
        more_random_text = fake.sentence()
        search_terms = " ".join([random_text, more_random_text])

        test_release_year = self.formatter._get_release_year(search_terms=search_terms)

        self.assertEqual(test_release_year, release_year)

    def test_get_clean_title_candidate_and_release_year_with_example_titles(self):
        """Ensure title and release year can be found, given real world example titles."""
        for example_title in self.example_titles:
            for original_filename, metadata in example_title.items():
                title = metadata.get("title")
                # Punctuation-free title, safe for searching
                search_safe_title = self.formatter._strip_punctuation(phrase=title)
                # Final (formatted) file names are all "folder/file safe", meaning they don't contain illegal characters:
                release_year = metadata.get("release_year")
                test_filename = " ".join([search_safe_title, release_year])
                test_clean_title_candidate, test_release_year = self.formatter._get_clean_title_candidate_and_release_year(
                    search_terms=test_filename
                )
                self.assertEqual(test_clean_title_candidate, search_safe_title)
                if test_release_year is not None:
                    self.assertEqual(test_release_year, release_year)

    def test_get_clean_title_candidate_and_release_year_with_contrived_title_and_release_year(
        self
    ):
        """Ensure title and release year can be found, given a contrived example title and release year."""
        fake_title = " ".join(fake.words())
        fake_title_list = fake_title.split()
        fake_release_year = fake.year()
        fake_title_list.extend([fake_release_year, "1080", "720", "480"])
        fake_search_terms = ".".join(fake_title_list)
        test_title_candidate, test_release_year = self.formatter._get_clean_title_candidate_and_release_year(
            search_terms=fake_search_terms
        )

        self.assertEqual(test_title_candidate, fake_title.lower())
        self.assertEqual(test_release_year, fake_release_year)

    @patch(f"omdb.Api.search")
    def test_search(self, omdb_search_method_patch_patch):
        """Ensure that the `omdb.Api.search()` method is called when `formatter._search()` is called."""

        search_terms = fake.sentence()
        imdb_id = fake.word()
        title = fake.sentence()
        result_type = fake.word()
        release_year = fake.year()
        plot = fake.word()
        page = fake.pyint()
        callback = fake.url()
        season = fake.pyint()
        episode = fake.pyint()

        self.formatter._search(
            search_terms=search_terms,
            imdb_id=imdb_id,
            title=title,
            result_type=result_type,
            release_year=release_year,
            plot=plot,
            page=page,
            callback=callback,
            season=season,
            episode=episode,
        )

        omdb_search_method_patch_patch.assert_called_once()

    def test_fuzzy_search(self):
        """Ensure fuzzy searching works as expected."""
        fake_search_query = " ".join(fake.words())
        fake_search_key = fake.word()
        fake_result_key = fake.word()
        fake_result_value = fake.word()

        fake_search_list = [
            {fake_search_key: fake_search_query, fake_result_key: fake_result_value}
        ]

        # Create a bunch of extraneous bad matches to test against:
        min_value = 1
        max_value = 10
        iterations = fake.pyint(min_value=min_value, max_value=max_value)
        for iteration in range(min_value, iterations):
            fake_random_words = " ".join(fake.words())
            new_fake_result_value = fake.word()
            fake_data = {
                fake_search_key: fake_search_query + (fake_random_words * iteration),
                fake_result_key: new_fake_result_value,
            }
            fake_search_list.append(fake_data)

        test_result_value, fuzzy_score = self.formatter._fuzzy_search(
            search_query=fake_search_query,
            search_key=fake_search_key,
            search_list=fake_search_list,
            result_key=fake_result_key,
        )

        self.assertEqual(test_result_value, fake_result_value)

    def test_strip_illegal_characters(self):
        """Ensures all characters that aren't allowed in files or folders are stripped from the given phrase."""
        # Characters that are not allowed when creating a file or folder:
        illegal_characters = '\\/:*?"<>|'
        # Convert the random phrase string to a list to do insertions:
        random_phrase = fake.sentence()
        random_phrase_list = list(random_phrase)
        # How many illegal characters we will be inserting into the random phrase:
        iterations = fake.pyint(min_value=0, max_value=len(random_phrase) - 1)

        # For a random number of iterations (up to a max of the length of the random phrase):
        for i in range(iterations):
            # Choose a random illegal_character:
            random_illegal_character_index = fake.pyint(
                min_value=0, max_value=len(illegal_characters) - 1
            )
            random_illegal_character = illegal_characters[
                random_illegal_character_index
            ]

            # and a random index to place the illegal character:
            random_index = fake.pyint(
                min_value=0, max_value=len(random_phrase_list) - 1
            )
            random_phrase_list.insert(random_index, random_illegal_character)

        test_illegal_phrase = "".join(random_phrase_list)

        test_legalized_phrase = self.formatter._strip_illegal_characters(
            phrase=test_illegal_phrase
        )

        self.assertEqual(test_legalized_phrase, random_phrase)

    def test_write_metadata_using_correct_content_key(self):
        """Ensure `_write_metadata()` method writes data to the metadata file as expected if the correct `content_key` is used."""
        content_keys = ["titles", "metadata", "errors"]
        content = {content_key: [] for content_key in content_keys}

        for content_key in content_keys:
            # Create some fake data:
            fake_key = fake.word()
            fake_value = fake.word()
            fake_data = {fake_key: fake_value}
            # and keep track of that fake data:
            content[content_key].append(fake_data)
            self.formatter._write_metadata(
                new_content=fake_data, content_key=content_key
            )

        metadata_file = self.formatter.initialize_metadata_file()

        # Ensure all the data is congruent:
        for content_key in content_keys:
            self.assertEqual(metadata_file.get(content_key), content.get(content_key))

    def test_write_metadata_using_incorrect_content_key_raises_keyerror_exception(self):
        """Ensure `_write_metadata()` method raises a KeyError exception if the incorrect `content_key` is used."""
        fake_content_key = fake.word()

        try:
            fake_key = fake.word()
            fake_value = fake.word()
            fake_data = {fake_key: fake_value}
            self.formatter.initialize_metadata_file()
            self.formatter._write_metadata(
                new_content=fake_data, content_key=fake_content_key
            )
        except Exception as error:
            self.assertIsInstance(error, KeyError)

    def test_write_metadata_using_incorrect_content_key_writes_nothing(self):
        """Ensure `_write_metadata()` method raises a KeyError exception and doesn't write anything if the incorrect `content_key` is used."""
        content_keys = ["titles", "metadata", "errors"]

        fake_content_key = fake.word()
        fake_key = fake.word()
        fake_value = fake.word()
        fake_data = {fake_key: fake_value}

        try:
            self.formatter._write_metadata(
                new_content=fake_data, content_key=fake_content_key
            )
        except Exception as error:
            self.assertIsInstance(error, KeyError)

        metadata = self.formatter.initialize_metadata_file()

        for content_key in content_keys:
            self.assertNotEqual(metadata.get(content_key), fake_data)

    @patch(f"{module_under_test}.Formatter._write_metadata")
    def test_write_all_metadata(self, write_metadata_method_patch):
        """Ensure all metadata gets written as expected."""
        fake_imdb_id = fake.word()
        fake_poster = fake.url()
        fake_imdb_object = {"imdbID": fake_imdb_id, "Poster": fake_poster}
        fake_original_filename = " ".join(fake.words())
        fake_final_title = " ".join(fake.words())

        fake_title_metadata = {
            "original_filename": fake_original_filename,
            "title": fake_final_title,
            "imdb_id": fake_imdb_id,
            "poster": fake_poster,
        }

        self.formatter._write_all_metadata(
            imdb_object=fake_imdb_object,
            original_filename=fake_original_filename,
            final_title=fake_final_title,
        )

        write_metadata_method_patch.assert_any_call(
            new_content=fake_title_metadata,
            content_key="titles",
            directory=blockbuster.TEST_INPUT_FOLDER,
            metadata_filename=blockbuster.METADATA_FILENAME,
        )
        write_metadata_method_patch.assert_any_call(
            new_content=fake_imdb_object,
            content_key="metadata",
            directory=blockbuster.TEST_INPUT_FOLDER,
            metadata_filename=blockbuster.METADATA_FILENAME,
        )

    def test_rename_file_without_recursion(self):
        """Ensure files are being renamed appropriately."""
        fake_new_filenames = []
        original_filenames = []

        # Rename all the files in the `test_folder`:
        for root, dirs, files in os.walk(self.test_folder):
            for file in files:
                # Keep track of the original filenames:
                original_filenames.append(file)

                # Create a fake new filename:
                fake_new_filename = fake.word()
                # and keep track of those fake new filenames:
                fake_new_filenames.append(fake_new_filename)
                # Rename that file!
                self.formatter._rename_file(
                    current_filepath=root,
                    original_filename=file,
                    proposed_new_filename=fake_new_filename,
                )

        # Now let's check that all the files were renamed:
        for root, dirs, files in os.walk(self.test_folder):
            for file in files:
                filename, extension = os.path.splitext(file)
                # They should exist in the fake new filenames list:
                self.assertIn(filename, fake_new_filenames)
                # and not in the original filenames list:
                self.assertNotIn(filename, original_filenames)

    def test_rename_file_with_recursion(self):
        """Ensure files are being renamed appropriately if more than one file with that filename exists."""
        fake_new_filenames = []
        original_filenames = []
        min_value = 0
        max_value = 10
        root = self.test_folder

        # Create a special separate area to do this testing:
        special_test_folder = os.path.join(root, "special_test_folder")
        os.makedirs(special_test_folder)

        # This time, we'll use the same fake new filename for all the files
        # to test the recursive renaming functionality:
        fake_new_name = fake.word()
        fake_file_extension = fake.word()
        fake_new_filename = ".".join([fake_new_name, fake_file_extension])

        # Create a fake file to conflict with the first renaming:
        fake_new_filepath = os.path.join(special_test_folder, fake_new_filename)
        open(fake_new_filepath, "a").close()
        counter = 2

        # Add the first fake new filename to the list:
        fake_new_filenames.append(fake_new_name)

        # For a random number of times, rename the file that many times.
        iterations = fake.pyint(min_value=min_value, max_value=max_value)
        for iteration in range(iterations):
            # Create a random file:
            fake_name = fake.word()
            # But use the same extension:
            fake_filename = ".".join([fake_name, fake_file_extension])
            fake_filepath = os.path.join(special_test_folder, fake_filename)
            open(fake_filepath, "a").close()

            # Keep track of the original filenames:
            original_filenames.append(fake_name)

            # Rename the first file to the second's name:
            self.formatter._rename_file(
                current_filepath=special_test_folder,
                original_filename=fake_filename,
                proposed_new_filename=fake_new_name,
            )

            # Update the counter suffix for the next iteration:
            fake_new_filename_to_add = "_".join([fake_new_name, str(counter)])
            counter += 1

            # and keep track of those fake new filenames
            # (this should be identical to the list of the files that were actually created):
            fake_new_filenames.append(fake_new_filename_to_add)

        # Now let's check that all the files were renamed:
        for file in os.listdir(special_test_folder):
            filename, extension = os.path.splitext(file)
            # They should exist in the fake new filenames list:
            self.assertIn(filename, fake_new_filenames)
            # and not in the original filenames list:
            self.assertNotIn(filename, original_filenames)

    @patch(f"{module_under_test}.Formatter._rename_file")
    def test_rename_folder_and_contents_with_directory(self, rename_file_method_patch):
        """Ensure folders and their contents are renamed correctly, when a valid directory is provided."""
        min_value = 0
        max_value = 10
        num_files = fake.pyint(min_value=min_value, max_value=max_value)
        fake_folder_name = " ".join(fake.words())
        fake_new_name = " ".join(fake.words())

        # Create a fake folder:
        fake_folder_path = os.path.join(self.test_folder, fake_folder_name)
        os.makedirs(fake_folder_path)
        # And fake files:
        for i in range(num_files):
            fake_filename = " ".join(fake.words())
            fake_filepath = os.path.join(fake_folder_path, fake_filename)
            open(fake_filepath, "a").close()

        self.formatter.rename_folder_and_contents(
            directory=self.test_folder,
            original_name=fake_folder_name,
            new_name=fake_new_name,
        )
        self.assertEqual(rename_file_method_patch.call_count, num_files)

    @patch(f"{module_under_test}.Formatter._rename_file")
    def test_rename_folder_and_contents_without_directory(
        self, rename_file_method_patch
    ):
        """Ensure folders and their contents are renamed correctly, when a valid directory is not provided."""
        min_value = 0
        max_value = 10
        num_files = fake.pyint(min_value=min_value, max_value=max_value)
        fake_folder_name = " ".join(fake.words())
        fake_new_name = " ".join(fake.words())

        # Create a fake folder:
        fake_folder_path = os.path.join(self.test_folder, fake_folder_name)
        os.makedirs(fake_folder_path)
        # And fake files:
        for i in range(num_files):
            fake_filename = " ".join(fake.words())
            fake_filepath = os.path.join(fake_folder_path, fake_filename)
            open(fake_filepath, "a").close()

        self.formatter.rename_folder_and_contents(
            original_name=fake_folder_name, new_name=fake_new_name
        )
        self.assertEqual(rename_file_method_patch.call_count, num_files)

    @patch(f"{module_under_test}.Formatter._get_release_year")
    @patch(f"{module_under_test}.Formatter._search")
    def test_search_by_search_terms_without_release_year(
        self, search_method_patch, get_release_year_method_patch
    ):
        """

        Ensure searching by some `search_terms` without the `release_year`
        calls the `_get_release_year()` and `_search()` methods.
        """
        call_counter = 0
        for example_title in self.example_titles:
            for original_filename, metadata in example_title.items():
                search_terms = original_filename
                self.formatter.search_by_search_terms(search_terms=search_terms)
                call_counter += 1
        self.assertEqual(get_release_year_method_patch.call_count, call_counter)
        self.assertEqual(search_method_patch.call_count, call_counter)

    @patch(f"{module_under_test}.Formatter._get_release_year")
    @patch(f"{module_under_test}.Formatter._search")
    def test_search_by_search_terms_with_release_year(
        self, search_method_patch, get_release_year_method_patch
    ):
        """

        Ensure searching by some `search_terms` with the `release_year` calls the `_search()`
        method, but not the `_get_release_year()` method.
        """
        call_counter = 0
        for example_title in self.example_titles:
            for original_filename, metadata in example_title.items():
                search_terms = original_filename
                release_year = fake.year()
                self.formatter.search_by_search_terms(
                    search_terms=search_terms, release_year=release_year
                )
                call_counter += 1
        get_release_year_method_patch.assert_not_called()
        self.assertEqual(search_method_patch.call_count, call_counter)

    @patch(f"{module_under_test}.Formatter._search")
    def test_search_by_imdb_id(self, search_method_patch):
        """Ensure searching by an IMDb ID calls the `_search()` method."""
        call_counter = 0
        for example_title in self.example_titles:
            for original_filename, metadata in example_title.items():
                imdb_id = metadata["imdb_id"]
                self.formatter.search_by_imdb_id(imdb_id=imdb_id)
                call_counter += 1
        self.assertEqual(search_method_patch.call_count, call_counter)

    @patch(f"{module_under_test}.Formatter._get_release_year")
    @patch(f"{module_under_test}.Formatter._search")
    def test_search_by_title_without_release_year(
        self, search_method_patch, get_release_year_method_patch
    ):
        """

        Ensure searching by a title without the `release_year` calls the `_get_release_year()`
        and `_search()` methods.
        """
        call_counter = 0
        for example_title in self.example_titles:
            for original_filename, metadata in example_title.items():
                title = metadata["title"]
                self.formatter.search_by_title(title=title)
                call_counter += 1
        self.assertEqual(get_release_year_method_patch.call_count, call_counter)
        self.assertEqual(search_method_patch.call_count, call_counter)

    @patch(f"{module_under_test}.Formatter._get_release_year")
    @patch(f"{module_under_test}.Formatter._search")
    def test_search_by_title_with_release_year(
        self, search_method_patch, get_release_year_method_patch
    ):
        """

        Ensure searching by a title with the `release_year` calls the `_search()` method,
        but not the `_get_release_year()` method.
        """
        call_counter = 0
        for example_title in self.example_titles:
            for original_filename, metadata in example_title.items():
                title = metadata["title"]
                release_year = fake.year()
                self.formatter.search_by_title(title=title, release_year=release_year)
                call_counter += 1
        get_release_year_method_patch.assert_not_called()
        self.assertEqual(search_method_patch.call_count, call_counter)

    def test_get_imdb_object_by_search_query(self):
        """Ensure that an IMDb object can be correctly retrieved, given a `search_query`"""

        for example_title in self.example_titles:
            for original_filename, metadata in example_title.items():
                imdb_id = metadata.get("imdb_id")
                title = metadata.get("title")
                release_year = metadata.get("release_year")

                # Get a test IMDb object from the "formatted" title and release year:
                test_imdb_object = self.formatter.get_imdb_object(
                    search_query=title, release_year=release_year
                )
                # This should return an object that contains the correct IMDb object:
                test_imdb_id = test_imdb_object.get("imdbID")
                test_title = self.formatter._strip_illegal_characters(
                    phrase=test_imdb_object.get("Title")
                )
                test_release_year = test_imdb_object.get("Year")

                self.assertEqual(test_imdb_id, imdb_id)
                self.assertEqual(test_title, title)
                self.assertEqual(test_release_year, release_year)

    def test_get_imdb_object_by_imdb_id(self):
        """Ensure that an IMDb object can be correctly retrieved, given an `imdb_id"""
        for example_title in self.example_titles:
            for original_filename, metadata in example_title.items():
                imdb_id = metadata.get("imdb_id")
                title = metadata.get("title")
                release_year = metadata.get("release_year")

                # Get a test IMDb object from the "formatted" title, an IMDb ID, and release year:
                test_imdb_object = self.formatter.get_imdb_object(
                    search_query=title, imdb_id=imdb_id, release_year=release_year
                )
                # This should return an object that contains the correct IMDb object:
                test_imdb_id = test_imdb_object.get("imdbID")
                test_title = self.formatter._strip_illegal_characters(
                    phrase=test_imdb_object.get("Title")
                )
                test_release_year = test_imdb_object.get("Year")

                self.assertEqual(test_imdb_id, imdb_id)
                self.assertEqual(test_title, title)
                self.assertEqual(test_release_year, release_year)

    # TODO: Fix this failing test
    # def test_format_creates_correct_files_and_folders(self):
    #     """Ensure formatting happens as expected, given a directory of poorly formatted title folders with files."""
    #     self.formatter.format()
    #
    #     root_directory = self.test_folder
    #
    #     for example_title in self.example_titles:
    #         for original_filename, metadata in example_title.items():
    #             # Original file should no longer exist:
    #             original_folder_path = os.path.join(root_directory, original_filename)
    #             self.assertFalse(os.path.exists(original_folder_path))
    #             formatted_filename = (
    #                 f"{metadata.get('title')} [{metadata.get('release_year')}]"
    #             )
    #             formatted_folder_path = os.path.join(root_directory, formatted_filename)
    #             # Check that all the file extensions are formatted:
    #             for file_extension in self.file_extensions:
    #                 formatted_filename_with_extension = (
    #                     formatted_filename + file_extension
    #                 )
    #                 formatted_filepath = os.path.join(
    #                     formatted_folder_path, formatted_filename_with_extension
    #                 )
    #                 bad_filepath = os.path.join(
    #                     original_folder_path, formatted_filename_with_extension
    #                 )
    #                 self.assertFalse(os.path.exists(bad_filepath))
    #                 self.assertTrue(os.path.exists(formatted_filepath))

    # TODO: Fix this failing test
    # def test_format_writes_correct_metadata(self):
    #     """Ensure `format()` writes the correct metadata to the metadata file."""
    #     self.formatter.format()
    #
    #     title_data = {}
    #     metadata_data = {}
    #
    #     metadata_file = self.formatter.initialize_metadata_file()
    #     for title in metadata_file.get("titles"):
    #         title_data[title.get("imdb_id")] = {
    #             "original_filename": title.get("original_filename"),
    #             "imdb_id": title.get("imdb_id"),
    #             "title": title.get("title"),
    #         }
    #
    #     for metadata in metadata_file.get("metadata"):
    #         metadata_data[metadata.get("imdbID")] = {
    #             "title": metadata.get("Title"),
    #             "release_year": metadata.get("Year"),
    #             "imdb_id": metadata.get("imdbID"),
    #         }
    #
    #     for example_title in self.example_titles:
    #         for original_filename, metadata in example_title.items():
    #             title = metadata.get("title")
    #             imdb_id = metadata.get("imdb_id")
    #             release_year = metadata.get("release_year")
    #
    #             # First check titles:
    #             title_data_object = title_data[imdb_id]
    #             self.assertEqual(
    #                 original_filename, title_data_object.get("original_filename")
    #             )
    #             self.assertEqual(imdb_id, title_data_object.get("imdb_id"))
    #             self.assertEqual(
    #                 f"{title} [{release_year}]", title_data_object.get("title")
    #             )
    #
    #             # Then check metadata:
    #             metadata_data_object = metadata_data[imdb_id]
    #             test_title = self.formatter._strip_illegal_characters(
    #                 phrase=metadata_data_object.get("title")
    #             )
    #             test_release_year = metadata_data_object.get("release_year")
    #             test_imdb_id = metadata_data_object.get("imdb_id")
    #             self.assertEqual(test_title, title)
    #             self.assertEqual(test_release_year, release_year)
    #             self.assertEqual(test_imdb_id, imdb_id)

    def test_format_with_crazy_data(self):
        """Ensure `format()` raises an exception and writes to error log appropriately, if input is insane."""
        min_value = 1
        max_value = 10
        iterations = fake.pyint(min_value=min_value, max_value=max_value)
        root = self.test_folder
        error_titles = []

        # Create a special separate area to do this testing:
        special_test_folder = os.path.join(root, "special_test_folder")
        os.makedirs(special_test_folder)

        for iteration in range(iterations):
            # Minimum release year range (between 0 and 1900)
            min_year_start = 0
            min_year_end = 1900
            min_year = fake.pyint(min_value=min_year_start, max_value=min_year_end)

            # Maximum release year range (between 2100 and 9999)
            max_year_start = 2100
            max_year_end = 9999
            max_year = fake.pyint(min_value=max_year_start, max_value=max_year_end)

            # Choose a random year that is before or after the threshold release years:
            release_year = random.choice([min_year, max_year])
            folder_name = fake.word() + str(release_year)
            error_titles.append(folder_name)
            folder_path = os.path.join(special_test_folder, folder_name)
            os.makedirs(folder_path)

        self.formatter.initialize_metadata_file(directory=special_test_folder)

        self.formatter.format(directory=special_test_folder)

        metadata = self.formatter.initialize_metadata_file(
            directory=special_test_folder
        )

        # There should be errors:
        self.assertNotEqual(len(metadata.get("errors")), 0)
        # In fact, there should be exactly `iterations` amount of errors:
        self.assertEqual(len(metadata.get("errors")), iterations)

        # And all of those errors should be the fake filenames we created:
        for error_data in metadata.get("errors"):
            self.assertIn(error_data.get("original_filename"), error_titles)


class PosterFinderTestCase(TestCase):
    def setUp(self):
        # To suppress the stdout by having verbose=True on PosterFinder instantiation:
        self.mock_print_patch = mock.patch("builtins.print")
        self.mock_print = self.mock_print_patch.start()

        self.mock_requests_patch = mock.patch(
            f"{module_under_test}.poster_finder.requests", autospec=True
        )
        self.mock_requests = self.mock_requests_patch.start()

        self.file_extensions = [".file"]
        test_environment = blockbuster.BlockBusterBuilder(
            level="pg-13",
            test_folder=blockbuster.TEST_INPUT_FOLDER,
            file_extensions=self.file_extensions,
            use_extensions=False,
        )
        self.test_folder, self.example_titles = (
            test_environment.create_empty_environment()
        )

        self.formatter = movie_file_fixer.Formatter(
            directory=blockbuster.TEST_INPUT_FOLDER,
            metadata_filename=blockbuster.METADATA_FILENAME,
            verbose=True,
        )

        self.poster_finder = movie_file_fixer.PosterFinder(
            directory=blockbuster.TEST_INPUT_FOLDER,
            metadata_filename=blockbuster.METADATA_FILENAME,
            verbose=True,
        )

    def tearDown(self):
        shutil.rmtree(self.test_folder)
        self.mock_print_patch.stop()
        self.mock_requests_patch.stop()

    def test_download_with_headers(self):
        """Ensure the `requests.get()` method is called when `_download()` is called and headers are provided."""
        fake_url = fake.url()
        fake_headers = fake.pydict()
        self.poster_finder._download(url=fake_url, headers=fake_headers)
        self.mock_requests.get.assert_called_once()

    def test_download_without_headers(self):
        """Ensure the `requests.get()` method is called when `_download()` is called and headers are not provided."""
        fake_url = fake.url()
        self.poster_finder._download(url=fake_url)
        self.mock_requests.get.assert_called_once()

    @patch(f"{module_under_test}.PosterFinder._download")
    def test_get_posters_if_folder_exists(self, download_method_patch):
        """

        Ensure the `_download()` method is called when `get_posters()` is called, the correct parameter
        values are specified, and the folder and `poster.jpg` files exist.
        """
        min_value = 0
        max_value = 10
        iterations = fake.pyint(min_value=min_value, max_value=max_value)
        fake_poster_urls = []

        # Create a new metadata file:
        self.formatter.initialize_metadata_file()

        for iteration in range(iterations):
            fake_poster_url = fake.url()
            fake_poster_urls.append(fake_poster_url)
            poster_folder_name = fake.word()
            full_poster_folder_path = os.path.join(self.test_folder, poster_folder_name)
            os.mkdir(full_poster_folder_path)
            fake_title_data = {"title": poster_folder_name, "poster": fake_poster_url}
            self.formatter._write_metadata(
                new_content=fake_title_data, content_key="titles"
            )

        fake_content = " ".join([word for word in fake.words()])
        download_method_patch.return_value.status_code = 200
        download_method_patch.return_value.content = bytes(
            fake_content, encoding="utf-8"
        )

        self.poster_finder.get_posters()

        for fake_poster_url in fake_poster_urls:
            download_method_patch.assert_any_call(url=fake_poster_url)

        metadata = self.formatter.initialize_metadata_file(directory=self.test_folder)

        for title in metadata.get("titles", []):
            filepath = os.path.join(self.test_folder, title["title"], "poster.jpg")
            self.assertTrue(os.path.exists(filepath))
            self.assertTrue(os.path.isfile(filepath))

    @patch(f"{module_under_test}.PosterFinder._download")
    def test_get_posters_if_folder_is_nonexistent(self, download_method_patch):
        """

        Ensure the `_download()` method is not called when `get_posters()` is called when the correct parameter
        values are specified, but the folder does not exist.
        """
        min_value = 0
        max_value = 10
        iterations = fake.pyint(min_value=min_value, max_value=max_value)

        # Create a new metadata file:
        self.formatter.initialize_metadata_file()

        for iteration in range(iterations):
            fake_poster_url = fake.url()
            poster_folder_name = fake.word()
            fake_title_data = {"title": poster_folder_name, "poster": fake_poster_url}
            self.formatter._write_metadata(
                new_content=fake_title_data, content_key="titles"
            )

        self.poster_finder.get_posters()

        download_method_patch.assert_not_called()


class SubtitleFinderTestCase(TestCase):
    def setUp(self):
        # To suppress the stdout by having verbose=True on SubtitleFinder instantiation:
        self.mock_print_patch = mock.patch("builtins.print")
        self.mock_print = self.mock_print_patch.start()

        self.file_extensions = [".file"]
        test_environment = blockbuster.BlockBusterBuilder(
            level="pg-13",
            test_folder=blockbuster.TEST_INPUT_FOLDER,
            file_extensions=self.file_extensions,
            use_extensions=False,
        )
        self.test_folder, self.example_titles = (
            test_environment.create_empty_environment()
        )

        self.formatter = movie_file_fixer.Formatter(
            directory=blockbuster.TEST_INPUT_FOLDER,
            metadata_filename=blockbuster.METADATA_FILENAME,
            verbose=True,
        )

        self.subtitle_finder = movie_file_fixer.SubtitleFinder(
            directory=blockbuster.TEST_INPUT_FOLDER,
            metadata_filename=blockbuster.METADATA_FILENAME,
            language="en",
            verbose=True,
        )

    def tearDown(self):
        shutil.rmtree(self.test_folder)
        self.mock_print_patch.stop()

    def test_is_movie_file_with_legit_extension(self):
        """Ensures that a legit movie filename (one that ends in a legit movie file extension) returns True."""
        legit_movie_file_extensions = [".avi", ".mp4", ".mkv", ".mov"]
        fake_legit_movie_filename = fake.word() + random.choice(
            legit_movie_file_extensions
        )
        test_is_movie_file = self.subtitle_finder._is_movie_file(
            filename=fake_legit_movie_filename
        )
        self.assertTrue(test_is_movie_file)

    def test_is_movie_file_with_a_non_movie_extension(self):
        """Ensures that a non-movie filename (one that does not end in a legit movie file extension) returns False."""
        not_movie_file_extensions = [".jpg", ".mp3", ".png", ".exe", fake.word()]
        fake_not_a_movie_filename = fake.word() + random.choice(
            not_movie_file_extensions
        )
        test_is_movie_file = self.subtitle_finder._is_movie_file(
            filename=fake_not_a_movie_filename
        )
        self.assertFalse(test_is_movie_file)

    def test_get_movie_file_paths(self):
        """Ensures all supported types of movie files are handled appropriately."""
        root = self.test_folder
        # Create some example files using the support movie file extensions:
        movie_file_extensions = [".avi", ".mp4", ".mkv", ".mov"]
        movie_file_paths = []
        for movie_file_extension in movie_file_extensions:
            movie_file_name = fake.word() + movie_file_extension
            movie_file_path = os.path.join(root, movie_file_name)
            movie_file_paths.append(movie_file_path)
            open(movie_file_path, "a").close()

        test_movie_file_paths = self.subtitle_finder._get_movie_file_paths(
            directory=root
        )
        self.assertEqual(sorted(test_movie_file_paths), sorted(movie_file_paths))

    def test_get_hash_with_real_files(self):
        """

        Ensure that `_get_hash()` returns the right hash when using real movie files.

        Example files taken from http://thesubdb.com/api/samples/dexter.mp4
        and http://thesubdb.com/api/samples/justified.mp4 and trimmed down to 128KB
        using utils.utils.create_trimmed_file() to save space on the GIT repo.
        """

        dexter_hash = "ffd8d4aa68033dc03d1c8ef373b9028c"
        justified_hash = "edc1981d6459c6111fe36205b4aff6c2"
        file_hashes = [dexter_hash, justified_hash]

        root = os.path.join(blockbuster.TEST_FOLDER, "test_examples")
        for file_hash in file_hashes:
            filepath = os.path.join(root, file_hash)
            test_hash = self.subtitle_finder._get_hash(filepath=filepath)
            self.assertEqual(test_hash, file_hash)

    def test_get_hash_with_contrived_files(self):
        """

        Ensure that `_get_hash()` returns the right hash when using contrived files.
        """
        root = self.test_folder
        min_value = 0
        max_value = 10
        iterations = fake.pyint(min_value=min_value, max_value=max_value)

        for iteration in range(iterations):
            # First, create a file that is 3x the size we want to test against:
            large_filename = "testing"
            utils.create_random_file(
                directory=root, filename=large_filename, filesize=3 * 128
            )
            large_filepath = os.path.join(root, large_filename)
            file_hash = utils.create_trimmed_file(filepath=large_filepath)
            filepath = os.path.join(root, file_hash)
            test_hash = self.subtitle_finder._get_hash(filepath=filepath)
            self.assertEqual(test_hash, file_hash)

    @patch(f"{module_under_test}.subtitle_finder.requests")
    def test_download_with_headers_calls_requests_get(self, requests_method_patch):
        """Ensure the `requests.get()` method is called when `_download()` is called and headers are provided."""
        fake_url = fake.url()
        fake_headers = fake.pydict()
        self.subtitle_finder._download(url=fake_url, headers=fake_headers)
        requests_method_patch.get.assert_called_once()

    @patch(f"{module_under_test}.subtitle_finder.requests")
    def test_download_without_headers_calls_requests_get(self, requests_method_patch):
        """Ensure the `requests.get()` method is called when `_download()` is called and headers are not provided."""
        fake_url = fake.url()
        self.subtitle_finder._download(url=fake_url)
        requests_method_patch.get.assert_called_once()

    @patch(f"{module_under_test}.SubtitleFinder._download")
    def test_search_subtitles_calls_download_subtitles(self, download_method_patch):
        """Ensure the `_download()` function is called when `_search_subtitles()` is called."""
        hashcode = fake.word()
        payload = {"action": "search", "hash": hashcode}
        self.subtitle_finder._search_subtitles(hashcode=hashcode)
        download_method_patch.assert_called_once()
        download_method_patch.assert_called_with(payload=payload)

    @patch(f"{module_under_test}.SubtitleFinder._download")
    def test_download_subtitles_calls_download_subtitles(self, download_method_patch):
        """Ensure that the `_download()` function is called when `_download_subtitles()` is called."""
        language = fake.word()
        hashcode = fake.word()
        payload = {"action": "download", "hash": hashcode, "language": language}
        self.subtitle_finder._download_subtitles(language=language, hashcode=hashcode)
        download_method_patch.assert_called_once()
        download_method_patch.assert_called_with(payload=payload)

    @patch(f"{module_under_test}.SubtitleFinder._download_subtitles")
    def test_get_subtitles_calls_download_subtitles_with_legit_file_extensions(
        self, download_subtitles_method_patch
    ):
        """

        Ensure that the `_download_subtitles()` function is called when `get_subtitles()` is called when the directory
        has legit movie files (ones that end in a legit movie file extension)
        """
        fake_movie_folder_paths = []
        language = "en"
        dexter_hash = "ffd8d4aa68033dc03d1c8ef373b9028c"
        justified_hash = "edc1981d6459c6111fe36205b4aff6c2"
        file_hashes = [dexter_hash, justified_hash]
        legit_movie_file_extensions = [".avi", ".mp4", ".mkv", ".mov"]

        example_root = os.path.join(blockbuster.TEST_FOLDER, "test_examples")
        test_root = self.test_folder
        self.formatter.initialize_metadata_file(directory=test_root)

        for file_hash in file_hashes:
            filepath = os.path.join(example_root, file_hash)
            fake_original_filename = fake.word()
            fake_movie_title = file_hash + random.choice(legit_movie_file_extensions)
            fake_imdb_id = fake.word()
            fake_poster_url = fake.url()
            fake_title_metadata = {
                "original_filename": fake_original_filename,
                "title": file_hash,
                "imdb_id": fake_imdb_id,
                "poster": fake_poster_url,
            }
            self.formatter._write_metadata(
                new_content=fake_title_metadata, content_key="titles"
            )

            fake_movie_folder_path = os.path.join(test_root, file_hash)
            fake_movie_file_path = os.path.join(
                fake_movie_folder_path, fake_movie_title
            )
            fake_movie_folder_paths.append(fake_movie_folder_path)
            os.makedirs(fake_movie_folder_path)
            shutil.copy(filepath, fake_movie_file_path)

        self.subtitle_finder.get_subtitles(directory=test_root, language=language)

        self.assertEqual(download_subtitles_method_patch.call_count, 2)

    @patch(f"{module_under_test}.SubtitleFinder._download_subtitles")
    def test_get_subtitles_does_not_call_download_subtitles_with_fake_language(
        self, download_subtitles_method_patch
    ):
        """

        Ensure that the `_download_subtitles()` function is not called when `get_subtitles()` is called with a fake language.
        """
        fake_movie_folder_paths = []
        language = fake.word()
        dexter_hash = "ffd8d4aa68033dc03d1c8ef373b9028c"
        justified_hash = "edc1981d6459c6111fe36205b4aff6c2"
        file_hashes = [dexter_hash, justified_hash]
        legit_movie_file_extensions = [".avi", ".mp4", ".mkv", ".mov"]

        example_root = os.path.join(blockbuster.TEST_FOLDER, "test_examples")
        test_root = self.test_folder
        self.formatter.initialize_metadata_file(directory=test_root)

        for file_hash in file_hashes:
            filepath = os.path.join(example_root, file_hash)
            fake_original_filename = fake.word()
            fake_movie_title = file_hash + random.choice(legit_movie_file_extensions)
            fake_imdb_id = fake.word()
            fake_poster_url = fake.url()
            fake_title_metadata = {
                "original_filename": fake_original_filename,
                "title": file_hash,
                "imdb_id": fake_imdb_id,
                "poster": fake_poster_url,
            }
            self.formatter._write_metadata(
                new_content=fake_title_metadata, content_key="titles"
            )

            fake_movie_folder_path = os.path.join(test_root, file_hash)
            fake_movie_file_path = os.path.join(
                fake_movie_folder_path, fake_movie_title
            )
            fake_movie_folder_paths.append(fake_movie_folder_path)
            os.makedirs(fake_movie_folder_path)
            shutil.copy(filepath, fake_movie_file_path)

        self.subtitle_finder.get_subtitles(directory=test_root, language=language)

        download_subtitles_method_patch.assert_not_called()

    @patch(f"{module_under_test}.SubtitleFinder._download_subtitles")
    def test_get_subtitles_does_not_call_download_subtitles_with_no_movie_file(
        self, download_subtitles_method_patch
    ):
        """

        Ensure that the `_download_subtitles()` function is not called when `get_subtitles()` is called when no movie file exists.
        """
        fake_movie_folder_paths = []
        language = "en"
        dexter_hash = "ffd8d4aa68033dc03d1c8ef373b9028c"
        justified_hash = "edc1981d6459c6111fe36205b4aff6c2"
        file_hashes = [dexter_hash, justified_hash]

        test_root = self.test_folder
        self.formatter.initialize_metadata_file(directory=test_root)

        for file_hash in file_hashes:
            fake_original_filename = fake.word()
            fake_imdb_id = fake.word()
            fake_poster_url = fake.url()
            fake_title_metadata = {
                "original_filename": fake_original_filename,
                "title": file_hash,
                "imdb_id": fake_imdb_id,
                "poster": fake_poster_url,
            }
            self.formatter._write_metadata(
                new_content=fake_title_metadata, content_key="titles"
            )

            fake_movie_folder_path = os.path.join(test_root, file_hash)
            fake_movie_folder_paths.append(fake_movie_folder_path)
            os.makedirs(fake_movie_folder_path)

        self.subtitle_finder.get_subtitles(directory=test_root, language=language)

        download_subtitles_method_patch.assert_not_called()

    @patch(f"{module_under_test}.SubtitleFinder._download_subtitles")
    def test_get_subtitles_does_not_call_download_subtitles_with_subtitle_file(
        self, download_subtitles_method_patch
    ):
        """

        Ensure that the `_download_subtitles()` function is not called when `get_subtitles()` is called
        and a subtitle file already exists.
        """
        fake_movie_folder_paths = []
        language = "en"
        subtitle_filename = f"{language}_subtitles.srt"
        dexter_hash = "ffd8d4aa68033dc03d1c8ef373b9028c"
        justified_hash = "edc1981d6459c6111fe36205b4aff6c2"
        file_hashes = [dexter_hash, justified_hash]
        legit_movie_file_extensions = [".avi", ".mp4", ".mkv", ".mov"]

        example_root = os.path.join(blockbuster.TEST_FOLDER, "test_examples")
        test_root = self.test_folder
        self.formatter.initialize_metadata_file(directory=test_root)

        for file_hash in file_hashes:
            filepath = os.path.join(example_root, file_hash)
            fake_original_filename = fake.word()
            fake_movie_title = file_hash + random.choice(legit_movie_file_extensions)
            fake_imdb_id = fake.word()
            fake_poster_url = fake.url()
            fake_title_metadata = {
                "original_filename": fake_original_filename,
                "title": file_hash,
                "imdb_id": fake_imdb_id,
                "poster": fake_poster_url,
            }
            self.formatter._write_metadata(
                new_content=fake_title_metadata, content_key="titles"
            )

            fake_movie_folder_path = os.path.join(test_root, file_hash)
            fake_movie_file_path = os.path.join(
                fake_movie_folder_path, fake_movie_title
            )
            fake_movie_folder_paths.append(fake_movie_folder_path)
            os.makedirs(fake_movie_folder_path)
            shutil.copy(filepath, fake_movie_file_path)
            # Write a subtitle file, so a new one doesn't get created:
            subtitle_filepath = os.path.join(fake_movie_folder_path, subtitle_filename)
            open(subtitle_filepath, "wb").close()

        self.subtitle_finder.get_subtitles(directory=test_root, language=language)

        download_subtitles_method_patch.assert_not_called()

    @patch(f"{module_under_test}.SubtitleFinder._download_subtitles")
    def test_get_subtitles_does_not_call_download_subtitles_with_non_movie_file_extensions(
        self, download_subtitles_method_patch
    ):
        """

        Ensure that the `_download_subtitles()` function is not called when `get_subtitles()` is called when the directory
        has non-movie files (ones that do not end in a legit movie file extension)
        """
        fake_movie_folder_paths = []
        language = "en"
        dexter_hash = "ffd8d4aa68033dc03d1c8ef373b9028c"
        justified_hash = "edc1981d6459c6111fe36205b4aff6c2"
        file_hashes = [dexter_hash, justified_hash]
        not_movie_file_extensions = [".jpg", ".mp3", ".png", ".exe", fake.word()]

        example_root = os.path.join(blockbuster.TEST_FOLDER, "test_examples")
        test_root = self.test_folder
        self.formatter.initialize_metadata_file(directory=test_root)

        for file_hash in file_hashes:
            filepath = os.path.join(example_root, file_hash)
            fake_original_filename = fake.word()
            fake_movie_title = file_hash + random.choice(not_movie_file_extensions)
            fake_imdb_id = fake.word()
            fake_poster_url = fake.url()
            fake_title_metadata = {
                "original_filename": fake_original_filename,
                "title": file_hash,
                "imdb_id": fake_imdb_id,
                "poster": fake_poster_url,
            }
            self.formatter._write_metadata(
                new_content=fake_title_metadata, content_key="titles"
            )

            fake_movie_folder_path = os.path.join(test_root, file_hash)
            fake_movie_file_path = os.path.join(
                fake_movie_folder_path, fake_movie_title
            )
            fake_movie_folder_paths.append(fake_movie_folder_path)
            os.makedirs(fake_movie_folder_path)
            shutil.copy(filepath, fake_movie_file_path)

        self.subtitle_finder.get_subtitles(directory=test_root, language=language)

        download_subtitles_method_patch.assert_not_called()

    def test_get_subtitles(self):
        """Ensure that the `get_subtitles()` method actually downloads posters."""
        fake_movie_folder_paths = []
        language = "en"
        dexter_hash = "ffd8d4aa68033dc03d1c8ef373b9028c"
        justified_hash = "edc1981d6459c6111fe36205b4aff6c2"
        file_hashes = [dexter_hash, justified_hash]
        legit_movie_file_extensions = [".avi", ".mp4", ".mkv", ".mov"]

        example_root = os.path.join(blockbuster.TEST_FOLDER, "test_examples")
        test_root = self.test_folder
        self.formatter.initialize_metadata_file(directory=test_root)

        for file_hash in file_hashes:
            filepath = os.path.join(example_root, file_hash)
            fake_original_filename = fake.word()
            fake_movie_title = file_hash + random.choice(legit_movie_file_extensions)
            fake_imdb_id = fake.word()
            fake_poster_url = fake.url()
            fake_title_metadata = {
                "original_filename": fake_original_filename,
                "title": file_hash,
                "imdb_id": fake_imdb_id,
                "poster": fake_poster_url,
            }
            self.formatter._write_metadata(
                new_content=fake_title_metadata, content_key="titles"
            )

            fake_movie_folder_path = os.path.join(test_root, file_hash)
            fake_movie_file_path = os.path.join(
                fake_movie_folder_path, fake_movie_title
            )
            fake_movie_folder_paths.append(fake_movie_folder_path)
            os.makedirs(fake_movie_folder_path)
            shutil.copy(filepath, fake_movie_file_path)

        self.subtitle_finder.get_subtitles(language=language)

        for fake_movie_folder_path in fake_movie_folder_paths:
            fake_movie_subtitle_path = os.path.join(
                fake_movie_folder_path, f"{language}_subtitles.srt"
            )
            self.assertTrue(os.path.exists(fake_movie_subtitle_path))
            self.assertTrue(os.path.isfile(fake_movie_subtitle_path))
