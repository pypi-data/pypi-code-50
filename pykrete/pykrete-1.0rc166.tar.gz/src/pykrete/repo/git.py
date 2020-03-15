"""
GIT repository management
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import re
from git import Repo


class Git:
    """Handles a GIT repository"""

    def __init__(self, path='.'):
        self._repo = Repo.init(path)

    def get_all_tags(self):
        """Gets all tags from the current branch in the repo

        :return: A list of tag info tuples (name, message)
        """
        return self._get_tags()

    def get_tags_from(self, pattern, is_must=False):
        """Gets all tags from the current branch in the repo, from the tag whose name matches the
         supplied pattern.

        :param pattern: name pattern to match
        :param is_must: True to raise an error if no match is found, False to return all tags in
        that case.
        :return: A list of tag info tuples (name, message)
        """
        return self._get_tags(lambda tag_refs: self.__filter_tags_from(pattern, is_must, tag_refs))

    def _get_tags(self, tag_ref_filter=None):
        tag_refs = list(self._repo.tags)
        requested_tag_references = tag_ref_filter(tag_refs) if tag_ref_filter else tag_refs
        return self.__tag_refs_to_name_message_tuples(requested_tag_references)

    def __filter_tags_from(self, pattern, is_must, tag_refs):
        from_index = self.__find_tag_index(pattern, tag_refs)
        if is_must and from_index == -1:
            raise KeyError("No tag found to match pattern " + pattern)
        return tag_refs[from_index if from_index > 0 else 0:]

    @staticmethod
    def __find_tag_index(pattern, tag_refs):
        compiled_pattern = re.compile(pattern)
        for i in range(len(tag_refs) - 1, -1, -1):
            if compiled_pattern.match(tag_refs[i].name):
                return i
        return -1

    @staticmethod
    def __tag_refs_to_name_message_tuples(tags):
        return [(tag.name, tag.tag.message if tag.tag else None) for tag in tags]
