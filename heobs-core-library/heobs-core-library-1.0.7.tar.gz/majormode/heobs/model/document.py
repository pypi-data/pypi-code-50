# Copyright (C) 2019 Heritage Observatory.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Heritage Observatory or one of its subsidiaries.  You shall not
# disclose this confidential information and shall use it only in
# accordance with the terms of the license agreement or other applicable
# agreement you entered into with Heritage Observatory.
#
# HERITAGE OBSERVATORY MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR
# A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  HERITAGE OBSERVATORY SHALL
# NOT BE LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A
# RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS
# DERIVATIVES.

import csv
import re

from majormode.perseus.model.enum import Enum
from majormode.perseus.model.locale import Locale
from majormode.perseus.model.geolocation import GeoPoint
from majormode.perseus.utils import cast


class Document(object):
    """
    Represent the attributes of a postcard or an old photograph.
    """
    SceneType = Enum(
        # Any form of life such as plant or living creature, would it be human
        # or any other animal.
        'being',

        # A place of cultural, historical, or natural significance for a group
        # or society.
        'heritage',

        # Any form of landscapes that show little or no human activity and are
        # created in the pursuit of a pure, unsullied depiction of nature.
        'scenery',

        # Any other type that doesn't represent a photograph, such as painting,
        # illustration, etc.
        'other',
    )

    # List of the tokens that can be used to modify a date.
    #
    # @warning: the longest tokens MUST be declared first, as the function
    #     ``_check_single_date_expression`` requires it:
    #
    #    for token in Document.DATE_MODIFIER_TOKENS:
    #        if date.startswith(token):
    DATE_MODIFIER_TOKENS = [ '<=', '>=', '~', '<', '>' ]

    # Regular expression to mach the expression of a simple date such as:
    #
    #     YYYY | YYYx | YYxx | YYYY-MM | YYYY-MM-DD
    SIMPLE_DATE_REGEX = re.compile(r'\d{4}|\d{3}x|\d{2}x{2}|\d{4}-\d{2}|\d{4}-\d{2}-\d{2}')


    def __init__(
            self,
            inventory_number,
            titles,
            author_name=None,
            collection_name=None,
            date=None,
            file_name=None,
            image_url=None,
            location_names=None,
            point=None,
            notes=None,
            scene_type=None,
            is_royalty_free=True):
        """
        Build a new instance ``Document``.


        @param inventory_number: inventory number of the photograph as defined
            by the organisation that is entrusted this photograph.

        @param titles: a tuple or a list of tuples corresponding to the
            caption of the photograph, written in a specified locale::

                (title:string, locale:Locale)

        @param author_name: name of the photographer.

        @param collection_name: name of the collection this photograph belongs to.

        @param file_name: file name of the photograph's image.  If a file name
             is not defined, it is built after the inventory name of the
             document.

        @param image_url: Uniform Resource Locator of the photograph’s image,
            if the image is shared online by the organisation that is
            entrusted this photograph.

        @param point: an instance containing the following attributes:

            * ``longitude``: longitude-angular distance, expressed in decimal
              degrees (WGS84 datum), measured from the center of the Earth, of a
              point east or west of the Prime Meridian.

            * ``latitude``: latitude-angular distance, expressed in decimal degrees
              (WGS84 datum), measured from the center of the Earth, of a point north
              or south of the Equator.

        @param location_names: list of names of the subdivisions of the
            location where the photograph has been taken.

        @param notes: a tuple or a list of tuples corresponding to the
            description of the photograph, written in a specified locale::

                (title:string, locale:Locale)

        @param date: precise or approximate date when this photograph has been
            taken.  This date MUST respect the specification ``time_spec``
            defined with the following Augmented Backus–Naur Form (ABNF)::

                time = YYYY | YYYx | YYxx | YYYY-MM | YYYY-MM-DD
                time_uncertainty = ?
                time_def = time | time time_uncertainty

                time_modifier = ~ | < | > | <= | >=
                time_expr = time_def | time_modifier time_def

                time_spec = time_expr | [time_expr, time_expr]

        @param scene_type: an item of ``SceneType`` that indicates the
            category of the subject taken in photo.

        @param is_royalty_free: indicate whether the photograph can be freely
            used.  Royalty free, or RF, refers to the right to use copyrighted
            material or intellectual property without the need to pay
            royalties or license fees for each use or per volume sold, or some
            time period of use or sales.
        """
        self.inventory_number = inventory_number
        assert inventory_number, 'No inventory number is provided'

        self.titles = titles and [ (content.strip(), locale if isinstance(locale, Locale) else Locale(locale))
                for (content, locale) in (titles if isinstance(titles, (list, set)) else [ titles ])
                    if content and len(content.strip()) ]
        assert self._check_i10n_labels(self.titles), 'Invalid titles format expression'

        self.author_name = author_name and author_name.strip()
        self.collection_name = collection_name and collection_name.strip()

        if not self._check_date_expression(date):
            print('[ERROR] Invalid date format expression "%s"' % date)
            date = None

        self.date = date

        self.file_name = file_name or '%s.jpg' % self.inventory_number

        self.image_url = image_url

        self.location_names = location_names and (location_names if isinstance(location_names, (list, set, tuple)) else [ location_names ])
        self.point = point

        self.notes = notes and [ (content.strip(), locale if isinstance(locale, Locale) else Locale(locale))
                for (content, locale) in (notes if isinstance(notes, (list, set)) else [ notes ])
                    if len(content.strip()) ]
        assert self._check_i10n_labels(self.notes), 'Invalid notes format expression'

        if scene_type:
            assert scene_type in Document.SceneType, 'The scene type MUST be an item of ``SceneType``'
        self.scene_type = scene_type

        self.is_royalty_free = is_royalty_free


    @staticmethod
    def _check_single_date_expression(date):
        """
        Check whether the given date expression respects the format
        specification ``time_expr``::

            time = YYYY | YYYx | YYxx | YYYY-MM | YYYY-MM-DD
            time_uncertainty = ?
            time_def = time | time time_uncertainty

            time_modifier = ~ | < | > | <= | >=
            time_expr = time_def | time_modifier time_def


        @param date: the string representation of a single date expression.


        @return: ``True`` if the given date respects the format specification
            of a single date; ``False`` otherwise.
        """
        if not date or len(date) == 0:
            return False

        # Check whether the date is prefixed with a modifier token.
        date_modifier = None
        for token in Document.DATE_MODIFIER_TOKENS:
            if date.startswith(token):
                date_modifier = token
                date = date[len(date_modifier):]
                if len(date) == 0:
                    return False
                break

        # Check whether the date is postfixed with the uncertainty token.
        is_date_uncertain = date[len(date) - 1] == '?'
        if is_date_uncertain:
            date = date[:len(date) - 1]
            if len(date) == 0:
                return False

        return Document.SIMPLE_DATE_REGEX.match(date)


    @staticmethod
    def _check_date_expression(date):
        """
        Check whether the given date expression respects the format
        specification ``time_spec``::

            time = YYYY | YYYx | YYxx | YYYY-MM | YYYY-MM-DD
            time_uncertainty = ?
            time_def = time | time time_uncertainty

            time_modifier = ~ | < | > | <= | >=
            time_expr = time_def | time_modifier time_def

            time_spec = time_expr | [time_expr, time_expr]


        @param date: a string representation of a date expression.


        @return: ``True`` if the given date respects the format specification
            of a date range or a single date; ``False`` otherwise.
        """
        if not date or len(date) == 0:
            return True

        # Check if the date expression corresponds to a date range.
        if date[0] == '[':
            if date[len(date) - 1] != ']':
                return False

            dates = [ _.strip() for _ in date[1:-1].split(',') ]
            if len(dates) != 2:
                return False

            [ date1, date2 ] = dates

            is_expression_valid = Document._check_single_date_expression(date1) and \
                    Document._check_single_date_expression(date2)

        else:
            is_expression_valid = Document._check_single_date_expression(date)

        return is_expression_valid


    @staticmethod
    def _check_i10n_labels(labels):
        """
        Check whether the given labels have all a locale defined.


        @param labels: a list of tuples ``(text, locale)`` where ``text`` is
            the string content of the label and ``locale`` is an instance
            ``Locale``.


        @return: ``True`` if the specified labels have all a locale defined;
            ``False`` otherwise.
        """
        return labels is None or (
                isinstance(labels, list) and \
                all([ isinstance(locale, Locale) for (_, locale) in labels ]))


class CommaSeparatedValueDocument(Document):
    # Define the fields used in a comma-separated value file that declare
    # documents.
    CSV_FIELD_NAME_INVENTORY_NUMBER = '#'
    CSV_FIELD_NAME_FILE_NAME = 'file'
    CSV_FIELD_NAME_IMAGE_URL = 'url'
    CSV_FIELD_NAME_TITLE = re.compile(r'title_([a-z]{3}){1}')
    CSV_FIELD_NAME_TITLE_PREFIX = 'title_'
    CSV_FIELD_NAME_NOTE = re.compile(r'note_([a-z]{3}){1}')
    CSV_FIELD_NAME_NOTE_PREFIX = 'note_'
    CSV_FIELD_NAME_AUTHOR_NAME = 'author'
    CSV_FIELD_NAME_COLLECTION_NAME = 'collection'
    CSV_FIELD_NAME_LOCATION_NAMES = 'location'
    CSV_FIELD_NAME_POINT = 'point'
    CSV_FIELD_NAME_SCENE_TYPE = 'scene'
    CSV_FIELD_NAME_DATE = 'date'
    CSV_FIELD_NAME_IS_ROYALTY_FREE = 'royalty_free'

    # Define the list of fields that are mandatory and those that are
    # optional.
    CSV_FIELDS = [
        (CSV_FIELD_NAME_INVENTORY_NUMBER, True),
        (CSV_FIELD_NAME_FILE_NAME, False),
        (CSV_FIELD_NAME_IMAGE_URL, False),
        (CSV_FIELD_NAME_TITLE, True),
        (CSV_FIELD_NAME_NOTE, False),
        (CSV_FIELD_NAME_AUTHOR_NAME, False),
        (CSV_FIELD_NAME_COLLECTION_NAME, False),
        (CSV_FIELD_NAME_LOCATION_NAMES, False),
        (CSV_FIELD_NAME_POINT, False),
        (CSV_FIELD_NAME_SCENE_TYPE, False),
        (CSV_FIELD_NAME_DATE, False),
        (CSV_FIELD_NAME_IS_ROYALTY_FREE, False)
    ]

    # Declare the list of field names.
    CSV_FIELD_NAMES = [ name for (name, is_required) in CSV_FIELDS ]

    # Declare the list of the names of the mandatory fields.
    CSV_REQUIRED_FIELD_NAMES = [ name for (name, is_required) in CSV_FIELDS if is_required ]


class CommaSeparatedValueDocumentReader(object):
    REGEX_GEOGRAPHIC_COORDINATES = re.compile(r'\(\s*(\d*(?:\.\d+)?)\s*,\s*((\d*(?:\.\d+)?))\s*\)')

    def __init__(self, file_path_name,
            delimiter='\t',
            quotechar='"'):
        with open(file_path_name, 'rt') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter, quotechar=quotechar)
            self.rows = [ row for row in reader ]

        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.next()

    @classmethod
    def __build_document(cls, row):
        titles = [ (row[match.group(0)], match.group(1))
            for match in [ CommaSeparatedValueDocument.CSV_FIELD_NAME_TITLE.match(field_name) for field_name in row ]
                if match ]

        notes = [ (row[match.group(0)], match.group(1))
            for match in [ CommaSeparatedValueDocument.CSV_FIELD_NAME_NOTE.match(field_name) for field_name in row ]
                if match ]

        geographic_coordinate_expression = row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_POINT)
        match = geographic_coordinate_expression and cls.REGEX_GEOGRAPHIC_COORDINATES.match(geographic_coordinate_expression)
        point = match and GeoPoint(match.group(1), match.group(2))

        return Document(
            row[CommaSeparatedValueDocument.CSV_FIELD_NAME_INVENTORY_NUMBER],
            titles,
            author_name=row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_AUTHOR_NAME),
            collection_name=row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_COLLECTION_NAME),
            date=row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_DATE),
            file_name=row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_FILE_NAME),
            image_url=row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_IMAGE_URL),
            location_names=row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_LOCATION_NAMES),
            point=point,
            notes=notes,
            scene_type=cast.string_to_enum(row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_SCENE_TYPE), Document.SceneType, strict=False),
            is_royalty_free=cast.string_to_boolean(row.get(CommaSeparatedValueDocument.CSV_FIELD_NAME_IS_ROYALTY_FREE)))

    def next(self):
        if self.current >= len(self.rows):
            raise StopIteration
        else:
            self.current += 1
            return self.__build_document(self.rows[self.current - 1])

