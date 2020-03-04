# Copyright (C) 2016 Majormode.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Majormode or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with
# the terms of the license agreement or other applicable agreement you
# entered into with Majormode.
#
# MAJORMODE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  MAJORMODE
# SHALL NOT BE LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE
# AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS
# DERIVATIVES.
#
# @version $Revision$

from majormode.heobs.model.photo import SceneType

from majormode.perseus.client.service.base_service import BaseService
from majormode.perseus.model.locale import DEFAULT_LOCALE
from majormode.perseus.model.obj import Object


class PhotoService(BaseService):
    BaseService._declare_custom_exceptions({
    })


    def add_bookmark(self, photo_id):
        """
        Add a bookmark to a photo on behalf the specified user.


        @param photo_id: identification of the photo the user adds a bookmark
            to.


        @return: an instance containing the following attributes:

            * ``creation_time`` (required): time when the bookmark has been added
              to this photo.

            * ``photo_id`` (required): identification of the photo the user adds a
              bookmark to.


        @raise ``DeletedObjectException``: if the specified photo has been
            deleted.

        @raise ``DisabledObjectException``: if the specified photo has been
            disabled.

        @raise ``IllegalAccessException``: if the user is not allowed to access
            this photo.

        @raise ``UndefinedObjectException``: if the specified photo is not
            registered to the platform.
        """
        return Object.from_json(
                self.send_request(
                    http_method=self.HttpMethod.POST,
                    path='/photo/(photo_id)/bookmark',
                    url_bits={
                        'photo_id': photo_id
                    },
                    authentication_required=True,
                    signature_required=True))


    def add_comment(self, photo_id, label):
        """
        Post a comment to a photo on behalf of the authenticated user.


        @param photo_id: identification number of a photo.

        @param label: an instance ``Label`` of the comment to post to the
            photo.


        @return: an instance containing the following information:

            * ``comment_id`` (required): identification of the comment posted to
              the photo.

            * ``creation_time`` (required): time when the comment has been posted
              to the photo.

            * ``photo_id`` (required): identification of the photo.
        """
        return self.send_request(
                http_method=self.HttpMethod.POST,
                path='/photo/(photo_id)/comment',
                url_bits={
                    'photo_id': photo_id
                },
                message_body={
                    'content': label.content,
                    'locale': label.locale
                },
                authentication_required=True,
                signature_required=True)


    def add_tags(self, photo_id, tags):
        """
        Add one or more tags to the specified photo on behalf of the user.


        @note: this function ignores tags that were previously added to
            this photo by this user


        @param photo_id: identification of the photo that the user adds
            tags to.

        @param tags: a list of tags to add to this photo on behalf of the
            user.


        @return: a list of instances containing the following members:

            * ``tag`` (required): tag that has been added to this photo.

            * ``update_time`` (required): time of the most recent modification of
              the tag which corresponds either to the time when this tag
              has been posted by the user to this photo for the first time,
              either the time when the user restored this tag he had removed
              from this photo.
        """
        return self.send_request(
                http_method=self.HttpMethod.POST,
                path='/photo/(photo_id)/tag',
                url_bits={
                    'photo_id': photo_id
                },
                message_body={
                    'tags': tags
                },
                authentication_required=True,
                signature_required=True)


    def delete_comment(self, photo_id, comment_id):
        """
        Delete a comment on behalf of the user who posted it.


        @param photo_id: identification of the photo the user posted
            this comment to.

        @param comment_id: identification of the comment to delete


        @return: an instance containing the following members:

            * ``account_id`` (required): identification of the user who deleted
              the comment.

            * ``comment_id`` (required): identification of the comment which
              content has been updated.

            * ``photo_id`` (required): identification of the photo which the
              comment has been posted to.

            * ``update_time`` (required): time when this photo has been
              deleted.


        @raise IllegalAccessException: if this comment has been posted by
            another user.

        @raise InvalidOperationException: if this comment has not been posted
            to the specified photo'

        @raise UndefinedObjectException: if the specified photo is not
            registered against the platform.
        """
        return self.send_request(
                http_method=self.HttpMethod.DELETE,
                path='/photo/(photo_id)/comment/(comment_id)',
                url_bits={
                    'comment_id': comment_id,
                    'photo_id': photo_id
                },
                authentication_required=True,
                signature_required=True)


    def get_bookmarks(self,
            limit=None,
            offset=None,
            sync_time=None):
        """
        Return a list of photos that the specified user has bookmarked.


        @param limit: constrain the number of photos that are returned to
            the specified number.

        @param offset: require to skip that many photos before beginning to
            return them to the client.  If both ``limit`` and ``offset`` are
            specified, then ``offset`` photos are skipped before starting
            to count the ``limit`` photos that are returned.

        @param sync_time: indicate the earliest time to return bookmarked
            photos based on the time the user has bookmarked them.  If not
            specified, the function returns any bookmarked photos, sorted by
            ascending order of the time they have been bookmarked.


        @return: an instance or a list of instances containing the following
            members:

            * ``creation_time`` (required): time when the user bookmarked this
              photo.

            * ``photo_id`` (required): identification of a bookmarked photo.
        """
        return self.send_request(
                http_method=self.HttpMethod.GET,
                path='/photo/bookmark',
                arguments={
                    'limit': limit,
                    'offset': offset,
                    'sync_time': sync_time
                },
                authentication_required=False,
                signature_required=True)


    def get_comments(self, photo_id,
            limit=None,
            offset=None):
        """
        Return a list of comments that have been posted to a photo.


        @note: comments are sorted by descending order of post time, from the
            most recent to the oldest.


        @param photo_id: identification of a photo.

        @param limit: constrain the number of comments that are returned to
            the specified number.

        @param offset: require to skip that many comments before beginning to
            return them.  If both ``limit`` and ``offset`` are specified, then
            ``offset`` comments are skipped before starting to count the
            ``limit`` comments that are returned.


        @return: a list of instances containing the following members:

            * ``account`` (required): information about the user who posted
              the comment:

              * ``account_id`` (required): identification of the user account.

              * ``fullname`` (optional): full name of the user.

              * ``username`` (optional): name of the account of the user.

              * ``picture_id`` (optional): identification of the user account's
                picture.

              * ``picture_url`` (optional): Uniform Resource Locator (URL) that
                specifies the location of the user account's picture.  The client
                application can use this URL and append the query parameter ``size``
                to specify a given pixel resolution of the user account's picture,
                such as ``thumbnail``, ``small``, ``medium``, ``large``.

            * ``content`` (required): textual content of the comment.

            * ``comment_id`` (required): identification of the comment which
              content has been updated.

            * ``locale`` (required): locale which the content is written in.  A
              locale corresponds to a tag respecting RFC 4646, which is a set of
              parameters that defines a language, country and any special variant
              references.  A locale identifier consists of at least a language
              identifier and a region identifier, i.e., a ISO 639-3 alpha-3 code
              element, optionally followed by a dash character ``-`` and a ISO
              3166-1 alpha-2 code. For example: ``eng`` (which denotes a standard
              English), ``eng-US`` (which denotes an American English).

            * ``photo_id`` (required): identification of the photo which the
              comment has been posted to.

            * ``update_time`` (required): time of the most recent modification of
              this comment and, by extension, of this photo.
        """
        return self.send_request(
                http_method=self.HttpMethod.GET,
                path='/photo/(photo_id)/comment',
                url_bits={
                    'photo_id': photo_id
                },
                arguments={
                    'limit': limit,
                    'offset': offset
                },
                authentication_required=False,
                signature_required=True)


    def get_photo(self, photo_id,
            include_comments=False,
            include_contacts=False,
            include_social_info=False,
            is_viewed=False,
            locale=None):
        """
        Return extended information about the specified photo.


        @param photo_id: identification of a photo.

        @param include_comments: indicate whether to include the most recent
            comments posted to this photo.

        @param include_contacts: indicate whether to include contact
            information of the user or the organisation who posted this photo.

        @param include_social_info: indicate whether to return statistics
            about user interactions related to this photo.

        @param is_viewed: indicate whether the client application will let the
            user view the photo just after the platform returns the
            information about this photo.  This option allows the client
            application to avoid a second round-trip with calling the function
            ``report_photo_view``.

        @param locale: an instance of ``Locale`` that specified in which
            locale any textual information of the photo needs to be returned
            in.


        @return: an instances containing the following members:

            * ``account`` (required): information about the account of the user
              who submitted this photo:

              * ``account_id`` (required): identification of the user account.

              * ``fullname`` (optional): full name of the user, if any defined.

              * ``picture_id`` (optional): identification of the user account's
                picture, if any picture defined for this user account.

              * ``picture_url`` (optional): Uniform Resource Locator (URL) that
                specifies the location of the user account's picture, if any
                defined.  The client application can use this URL and append the
                query parameter ``size`` to specify a given pixel resolution of the
                user account's picture, such as ``thumbnail``, ``small``,
                ``medium``, ``large``.

              * ``timezone`` (optional): time zone of the default location of the
                user.  It is the difference between the time at this location and
                UTC (Universal Time Coordinated).  UTC is also  known as GMT or
                Greenwich Mean Time or Zulu Time.

              * ``username`` (optional): a name used to gain access to a the
                platform, if any defined

            * ``note`` (optional): note of the photo in a given locale:

              * ``content``: textual content of the photo's note.

              * ``locale``: an instance ``Locale`` that specified in which locale
                the note of the photo is written in.

            * ``latitude`` (optional): latitude-angular distance, expressed in
              decimal degrees (WGS84 datum), measured from the center of the
              Earth, of a point north or south of the Equator corresponding to the
              location where the photo of the photo has been taken.

            * ``longitude`` (optional): longitude-angular distance, expressed in
              decimal degrees (WGS84 datum), measured from the center of the
              Earth, of a point east or west of the Prime Meridian corresponding
              to the location where the photo of the photo has been taken.

            * ``image_url`` (required): Uniform Resource Locator (URL) that
              specifies the location of the photo's image.  The client
              application can use this URL and append the query parameter ``size``
              to specify a given pixel resolution of the picture, such as
              ``thumbnail``, ``small``, ``medium``, ``large``.

            * ``photo_id`` (required): identification of the photo.

            * ``title`` (required): title of the photo in a given locale:

              * ``content``: textual content of the photo's title.

              * ``locale``: an instance ``Locale`` that specified in which locale
                the title of the photo is written in.
        """
        return self.send_request(
                http_method=self.HttpMethod.GET,
                path='/photo/(photo_id)',
                url_bits={
                    'photo_id': photo_id
                },
                arguments={
                    'include_comments': include_comments,
                    'include_contacts': include_contacts,
                    'include_social_info': include_social_info,
                    'is_viewed': is_viewed,
                    'locale': locale and str(locale)
                },
                authentication_required=False,
                signature_required=True)


    def get_photo_archive(self, photo_id,
            locale=DEFAULT_LOCALE):
        """
        Return information about the ZIP archive file of the specified photo.

        The archive of a photo includes:

        * the file of the original image this photo

        * a file containing the terms and conditions that govern the right of
          the user to use this image, which the user MUST agree to be bound by
          and comply with all these license terms.  These terms are returned in
          the specified locale

        * the JSON properties that describes this photo


        @param photo_id: identification of the photo a user is interested in
            downloading.

        @param locale: an instance of ``Locale`` that specified in which
            locale any textual information of the photo needs to be returned
            in, including the legal code of the license for this photo.


        @return: an instance containing the following members:

            * ``archive_url`` (required): Uniform Resource Locator (URL) that
              specifies the location of the ZIP archive file of the photo to be
              downloaded by the user.

            * ``collection`` (required): name of the collection this photo belongs
              to.

            * ``image_url`` (required): Uniform Resource Locator (URL) that
              specifies the location of the photo's image.  If this URL
              is handled by the Heritage Observatory's servers (``cdn.heobs.org``),
              the client application can use this URL and append the query
              parameter ``size`` to specify a given pixel resolution of the
              picture, such as ``thumbnail``, ``small``, ``medium``, ``large``.

            * ``image_alternative_url`` (optional): Uniform Resource Locator (URL)
              that specifies the location of the photo's image on the Heritage
              Observatory platform.  This URL can be used if the original URL of
              the photo's image is broken.  The client application can use this
              URL and append the query parameter ``size`` to specify a given pixel
              resolution of the picture, such as ``thumbnail``, ``small``,
              ``medium``, ``large``.

            * ``license`` (required): legal code of the license that the user must
              agree to comply with to be allowed to use the digitised image of
              this photo:

              * ``content`` (required): content of the license's legal code written
                in a given locale.

              * ``locale`` (required): the locale which this legal code is written
                in.

            * ``photo_id`` (required): identification of the photo.

            * ``team`` (optional): information about the organisation that has
              been entrusted the collection that this photo belongs to:

              * ``name`` (required): name of the organisation.

              * ``picture_id`` (optional): identification of the organisation's
                picture.

              * ``picture_url`` (optional): Uniform Resource Locator (URL) that
                specifies the location of the organisation's picture.  The client
                application can use this URL and append the query parameter ``size``
                to specify a given pixel resolution of the picture, such as
                ``thumbnail``, ``small``, ``medium``, ``large``.

              * ``team_id`` (required): identification of the organisation.

            * ``title`` (required): title of the photo in a given locale:

              * ``content``: textual content of the photo's title.

              * ``locale``: an instance ``Locale`` that specified in which locale
                the title of the photo is written in.


        @raise DeletedObjectException: if the specified photo has been
            deleted.

        @raise DisabledObjectException: if the specified photo has been
            disabled.

        @raise UndefinedObjectException: if the specified photo is not
            registered to the platform.
        """
        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.GET,
                        path='/photo/(photo_id)/archive',
                        url_bits={
                            'photo_id': photo_id
                        },
                        arguments={
                            'locale': locale
                        },
                        authentication_required=False,
                        signature_required=True))


    def get_photos(self, photo_ids,
            include_comments=False,
            include_contacts=False,
            include_labels=False,
            include_social_info=False,
            include_tags=False,
            is_viewed=False,
            locale=None):
        """
        Return up to 10 photos worth of extended information.


        @param photo_ids: a list of identifications of photos.

        @param include_comments: indicate whether to include the most recent
            comments posted to this photo.

        @param include_contacts: indicate whether to include contact
            information of the user or the organisation who posted this photo.

        @param include_labels:

        @param include_social_info:

        @param include_tags:

        @param is_viewed: indicate whether the client application will let the
            user view the photo just after the platform returns the
            information about this photo.  This option allows the client
            application to avoid a second round-trip with calling the function
            ``report_photo_view``.

        @param locale: an instance of ``Locale`` that specified in which
            locale any textual information of the photo needs to be returned
            in.


        @return:
        """
        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.GET,
                        path='/photo/(photo_ids)',
                        url_bits={
                            'photo_ids': photo_ids
                        },
                        arguments={
                            'include_comments': include_comments,
                            'include_contacts': include_contacts,
                            'include_labels': include_labels,
                            'include_social_info': include_social_info,
                            'include_tags': include_tags,
                            'is_viewed': is_viewed,
                            'locale': locale and str(locale)
                        },
                        authentication_required=False,
                        signature_required=True))


    def get_photos_by_publication_time_range(self, start_time, end_time,
            limit=None,
            locale=None,
            offset=0):
        return [ Object.from_json(payload)
                for payload in self.send_request(
                        http_method=self.HttpMethod.GET,
                        path='/photo',
                        arguments={
                            'end_time': end_time,
                            'limit': limit,
                            'locale': locale,
                            'offset': offset,
                            'start_time': start_time
                        },
                        authentication_required=False,
                        signature_required=True) ]


    def get_random_photo(self,
            orientation=None,
            remote_ip_address=None):
        """
        Return a photo chosen randomly.


        @param orientation: indicate the current orientation of the client
            application's viewport.  If provided, this function will return a
            photo with the same orientation to better fit the viewport of the
            client application.

        @param remote_ip_address: IP address of the client application.  If
            provided, the function will try to determine the location of the
            user and it will return photos that have been taken nearby this
            location.


        @return: an instance containing the following members:

            * ``account`` (required): information about the account of the user
              who submitted this photo:

              * ``account_id`` (required): identification of the user account.

              * ``fullname`` (optional): full name of the user.

              * ``picture_id`` (optional): identification of the user account's
                picture, if any picture defined for this user account.

              * ``picture_url`` (optional): Uniform Resource Locator (URL) that
                specifies the location of the user account's picture, if any
                defined.  The client application can use this URL and append the
                query parameter ``size`` to specify a given pixel resolution of the
                user account's picture, such as ``thumbnail``, ``small``,
                ``medium``, ``large``.

              * ``timezone`` (optional): time zone of the default location of the
                user.  It is the difference between the time at this location and
                UTC (Universal Time Coordinated).  UTC is also  known as GMT or
                Greenwich Mean Time or Zulu Time.

              * ``username`` (optional): a name used to gain access to a the
                platform, if any defined.

            * ``area_id`` (optional): identification of the adninistrative
              subdivision where the photo has been taken.

            * ``area_name`` (optional): human-readable address of the location where
              the photo has been taken from.

            * ``capture_time`` (required/optional): time when the image data were
              generated.  The format of this time depends on the provider who
              generated the image data:

              * ``PHOTO_TYPE_PICTURE``: local date and time when the original image data
                were generated, which, for a digital still camera, is the date and
                time the picture was taken or recorded.  For this provider, the
                capture time is required.

              * ``PHOTO_TYPE_SCAN``: precise or approximate date when this photo
                has been taken.  This date respects the specification ``time_spec``
                defined with the following Augmented Backus-Naur Form (ABNF)::

                    time = YYYY | YYYx | YYxx | YYYY-MM | YYYY-MM-DD
                    time_uncertainty = ?
                    time_def = time | time time_uncertainty
                    time_changer = ~ | < | > | <= | >=
                    time_expr = time_def | time_changer time_def
                    time_spec = time_expr | [time_expr, time_expr]

                For this provider, this capture time is optional.

            * ``creation_time`` (required): time when photo has been created.

            * ``image_alternate_url`` (optional): Uniform Resource Locator (URL)
              that specifies the location of the _photo's image on the Heritage
              Observatory platform.  This URL can be used if the original URL of
              the _photo's image is broken.  The client application can use this
              URL and append the query parameter ``size`` to specify a given pixel
              resolution of the picture, such as ``thumbnail``, ``small``,
              ``medium``, ``large``.

            * ``image_height`` (required): number of pixel rows of the photo's
              original image.

            * ``image_url`` (optional): Uniform Resource Locator (URL) that
              specifies the location of the image of this photo.  The query
              parameter ``size`` can be supplied to specify a given pixel resolution
              of the image, such as ``thumbnail``, ``small``, ``medium``, or
              ``large``.  This member is not returned if the status of the photo is
              still ``ObjectStatus.processing``.

            * ``image_width`` (required): number of pixel columns of the photo's'
              original image.

            * ``inventory_number`` (required): inventory number of the photograph as
              defined by the user or the organisation that owned or is entrusted
              this photograph.

            * ``location`` (optional): geographic location where the photo has been
              taken:

              ``accuracy`` (optonal): accuracy in meters of the measure of the
                location where the photo has been taken.

              ``altitude`` (optional): altitude in meters of the location.

              ``bearing`` (optional): angle of the direction that the camera pointed
                to when this photo has been taken.  The bearing is the number of
                degrees in the angle measured in a clockwise direction from the north
                line to the line passing through the location of the camera in the
                direction the camera was pointing at.

              ``fix_time`` (optional): time when the fix of the location has been
                calculated.

              ``latitude`` (required): latitude-angular distance, expressed in
                decimal degrees (WGS84 datum), measured from the center of the Earth,
                of a point north or south of the Equator.

              ``longitude`` (required): longitude-angular distance, expressed in
                decimal degrees (WGS84 datum), measured from the center of the Earth,
                of the location east or west of the Prime Meridian.

            * ``note`` (optional): note of the photo given in the specified locale,
              or the list of notes defined in all the available locales:

              * ``content``: textual content of the photo's note.

              * ``locale``: an instance ``Locale`` that specified in which locale
                the note of the photo is written in.

            * ``object_status`` (required): current status of this photo:

              ``OBJECT_STATUS_ENABLED``: the photo has been successfully reviewed by
                a regional expert.

            * ``orientation`` (required): indicate whether the photo is in
              landscape (the photo is wider than it is tall) or portrait (the
              photo is taller than it is wide) mode.

            * ``photo_id`` (required): identification of the photo.

            * ``place_id`` (optional): identification of the heritage site this
              photo corresponds to.

            * ``scene_type`` (optional): indicate the type of the scene depicted on
              the photo.  This classification allows the Observatory Heritage
              platform to determine whether a particular photo could be precisely
              geolocated using a mechanical turk method.  This applies to photos of
              heritage sites.

            * ``team`` (optional): information about the organisation on behalf
                which this photo has been submitted:

              * ``team_id`` (required): identification of the organisation.

              * ``name`` (required): the name of the organisation.

              * ``description`` (optional): a short textual description of the
                organisation.

              * ``account_id`` (required): identification of the account of the agent
                administrator for this organisation.

              * ``picture_id`` (optional): identification of the picture that
                represents the organisation.

              * ``picture_url`` (optional): Uniform Resource Locator (URL) that
                specifies the location of the picture representing the organisation.
                The client application can use this URL and append the query
                parameter ``size`` to specify a given pixel resolution of the
                picture, such as ``thumbnail``, ``small``, ``medium``, ``large``.

              * ``object_status``: current status of the organisation.

              * ``creation_time``: time when the organisation has been registered.

              * ``update_time``: most recent time when one or more properties of the
                organisation, has been modified.

            * ``title`` (required): title of the photo given in the specified
              locale, or the list of contents defined in all the available locales:

              * ``content``: textual content of the photo's title.

              * ``locale``: an instance ``Locale`` that specified in which locale
                the title of the photo is written in.

            * ``update_time`` (required): time of the most recent modification of
              the properties of this photo.

            * ``visibility`` (required): indicate the visibility of the photo.
        """
        return self.send_request(
                http_method=self.HttpMethod.GET,
                path='/photo/random',
                arguments={
                    'orientation': orientation,
                    'remote_ip_address': remote_ip_address
                },
                authentication_required=False,
                signature_required=True)


    def remove_bookmark(self, photo_id):
        """
        Remove a bookmark from a photo on behalf the specified user.


        @param photo_id: identification of the photo the user removes a
            bookmark from.


        @raise ``DeletedObjectException``: if the specified photo has been
            deleted.

        @raise ``DisabledObjectException``: if the specified photo has been
            disabled.

        @raise ``IllegalAccessException``: if the user is not allowed to access
            this photo.

        @raise ``UndefinedObjectException``: if the specified photo is not
            registered to the platform.
        """
        return Object.from_json(
                self.send_request(
                    http_method=self.HttpMethod.DELETE,
                    path='/photo/(photo_id)/bookmark',
                    url_bits={
                        'photo_id': photo_id
                    },
                    authentication_required=True,
                    signature_required=True))


    def remove_tags(self, tags,
            photo_id=None):
        """
        Remove the specified tags from the specified photo or, if not
        defined, from every photo the user may have added these tags.


        @param photo_id: the identification of the photo to remove the
            list of tags from.

        @param tags: a list of one or more tags to remove from the specified
             photo on behalf of the user.
        """
        if photo_id:
            return self.send_request(
                    http_method=self.HttpMethod.DELETE,
                    path='/photo/(photo_id)/tag',
                    url_bits={
                        'photo_id': photo_id
                    },
                    arguments={
                        'tags': ','.join(tags)
                    },
                    authentication_required=True,
                    signature_required=True)
        else:
            return self.send_request(
                    http_method=self.HttpMethod.DELETE,
                    path='/photo/tag',
                    arguments={
                        'tags': ','.join(tags)
                    },
                    authentication_required=True,
                    signature_required=True)


    def report_photo_view(self, photo_id):
        """
        Report that a user has just viewed a given photo.


        @param photo_id: identification of the photo that a user has
            seen.


        @return: an instance containing the following members:

            * ``photo_id`` (required): identification of the photo that is viewed.

            * ``update_time`` (required): the time of the most recent modification
              of the properties of this photo.

            * ``view_count`` (required): number of times this photo has been
              viewed by users.


        @raise DeletedObjectException: if the specified photo has been
            deleted.

        @raise DisabledObjectException: if the specified photo has been
            disabled.

        @raise UndefinedObjectException: if the specified photo is not
            registered to the platform.
        """
        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.POST,
                        path='/photo/(photo_id)/view',
                        url_bits={
                            'photo_id': photo_id
                        },
                        authentication_required=True,
                        signature_required=True))


    def search_photos(self,
            keywords=None,
            limit=None,
            locale=None,
            offset=0,
            tags=None):
        """
        Return a list of photos, worth of extended information, that match one
        or more the specified keywords.


        @note:  at least one of the arguments ``keywords`` and ``tags`` must
            be passed to this function.


        @param keywords: a list of keywords used to search for photos which
            content or meta data match one or more those terms.  The minimal
            length of a keyword is 2 characters.

        @param limit: constrain the number of photos that are returned to the
            specified number.

        @param locale: an instance ``Locale`` to return textual information of
            the photos, such as their content and their note.

        @param offset: require to skip that many photos before beginning to
            return them.  If both ``limit`` and ``offset`` are specified, then
            ``offset`` photos are skipped before starting to count the
            ``limit`` photos that are returned.

        @param tags: a list of tags that the user may have added to some
            photos.  This attribute requires the user to be authenticated.


        @return: an instance or a list of instances containing the following
            members:
        """
        if not keywords and not tags:
            raise ValueError('A list of keywords of 2 characters or more or a list of tags must be provided')

        return [ Object.from_json(payload)
                for payload in self.send_request(
                        http_method=self.HttpMethod.GET,
                        path='/photo',
                        arguments={
                            'keywords': keywords and ','.join(keywords),
                            'limit': limit,
                            'locale': locale,
                            'offset': offset,
                            'tags': tags and ','.join(tags)
                        },
                        authentication_required=False,
                        signature_required=True) ]


    def set_photo_rating(self, photo_id, value):
        """
        Rate a photo on behalf of a user, whether he likes or dislikes this
        photo, or whether he has no particular opinion about this photo.


        @param photo_id: identification of the photo that is rated.

        @param value: a value among the possible following values:

            * ``-1``: the user dislikes this photo.

            * ``0``: the user has no particular opinion about this photo.

            * ``1``: the user likes this photo.


        @return: an instance containing the following members:

            * ``dislike_count`` (required): number of users who dislike this photo.

            * ``like_count`` (required): number of users who like this photo.

            * ``photo_id`` (required): identification of the photo that the
                user has rated.

            * ``update_time`` (required): time of the most recent modification of
              one or more properties of this photo.


        @raise InvalidArgumentException: if the rating value provided by the
            user is no in the valid range.

        @raise UndefinedObjectException: if the specified photo is not
            registered to the platform.
        """
        if value not in range(-1, 2):
            raise self.InvalidArgumentException('The rating value of a photo MUST be an integer in the range [-1, 1]')

        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.PUT,
                        path='/photo/(photo_id)/rating',
                        url_bits={
                            'photo_id': photo_id
                        },
                        arguments={
                            'value': value
                        },
                        authentication_required=True,
                        signature_required=True))


    def suggest_photo_scene_type(self, photo_id, scene_type,
            fingerprint_id=None):
        """
        Suggest on behalf of a user, authenticated or not, the scene type
        depicted on a photo.


        @param photo_id: identification of the photo.

        @param scene_type: an instance of `SceneType` indicating the type of
            the scene depicted in the specified photograph, or ``None`` to
            clear the previous suggestion sent by this user.

        @param fingerprint_id: the fingerprint of the user's browser.  This
            ID will be used to represent an anonymous user.
        """
        if scene_type and scene_type not in SceneType:
            raise self.InvalidArgumentException('The scene type of a photo MUST be an item of "SceneType"')

        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.PUT,
                        path='/photo/(photo_id)/scene_type',
                        url_bits={
                            'photo_id': photo_id
                        },
                        arguments={
                            'fingerprint_id': fingerprint_id,
                            'scene_type': scene_type
                        },
                        authentication_required=False,
                        signature_required=True))


    def update_comment(self, photo_id, comment_id, label):
        """
        Update the content of a comment that the authenticated user has posted
        to a photo.


        @param photo_id: identification of the photo which the comment
            has been posted to.

        @param comment_id: identification of the comment to update the
            content.

        @param label: an instance ``Label`` of the new content of this
            comment.


        @return: an instance containing the following information:

            * ``account_id`` (required): identification of the user who initially
              posted and recently  updated this comment.

            * ``comment_id`` (required): identification of the comment which
              content has been updated.

            * ``photo_id`` (required): identification of the photo which the
              comment has been posted to.

            * ``update_time`` (required): time of the most recent modification of
              this comment and, by extension, of this photo.
        """
        return self.send_request(
                http_method=self.HttpMethod.PUT,
                path='/photo/(photo_id)/comment/(comment_id)',
                url_bits={
                    'comment_id': comment_id,
                    'photo_id': photo_id
                },
                message_body={
                    'content': label.content,
                    'locale': label.locale,
                },
                authentication_required=True,
                signature_required=True)











        # def delete_photos(self, photo_ids):
    #     """
    #     Delete the specified photos from the platform.
    #
    #
    #     @param photo_ids: list of identifications of the photos to be deleted.
    #
    #
    #     @return: the list of identifications of the photos that have been
    #         deleted.
    #     """
    #     return [ cast.string_to_uuid(payload)
    #             for payload in self.send_request(
    #                     http_method=self.HttpMethod.DELETE,
    #                     path='/photo/(photo_ids)',
    #                     url_bits={
    #                         'photo_ids': ','.join([ photo_id.hex for photo_id in photo_ids ])
    #                     },
    #                     authentication_required=True,
    #                     signature_required=True) ]
    #
    #
    # def get_photos(self,
    #         bounds=None,
    #         limit=None,
    #         locale=DEFAULT_LOCALE,
    #         location=None,
    #         offset=0,
    #         photo_ids=None,
    #         radius=5000,
    #         sync_time=None):
    #     """
    #     Return a list of photos, worth of extended information, corresponding
    #     to the specified criteria.
    #
    #
    #     @param bounds: a tuple of two instances ``GeoPoint`` that represent
    #         the north-east corner and the south-west corners of the rectangle
    #         area to search photos in.
    #
    #     @param limit: constrain the number of photos that are returned to the
    #       specified number.
    #
    #     @param locale: an instance ``Locale`` to return textual information of
    #         the photos, such as their title and their description.
    #
    #     @param location: an instance ``GeoPoint`` of the geographic location
    #         to search nearby places.  This parameter is incompatible with the
    #         parameters ``bounds`` and ``photo_ids``.
    #
    #     @param offset: require to skip that many photos before beginning to
    #       return them.  If both ``limit`` and ``offset`` are specified, then
    #       ``offset`` photos are skipped before starting to count the ``limit``
    #       photos that are returned.
    #
    #     @param photo_ids: identifications of specific photos to return.  This
    #         parameter is incompatible with the parameters ``bounds``,
    #         ``location``, and ``radius``.
    #
    #         This function silently filters out photos that are not public and
    #         which this user doesn't have access to:
    #
    #         the user is not the owner of these photos
    #
    #         the user is not a member of the organisations that owns or that is
    #           shared these photos
    #
    #         the user is not a moderator of the geographical region that
    #           corresponds to these photos
    #
    #         the user is not a super-user of the platform
    #
    #     @param radius: maximal distance in meters of the radius of search for
    #         photos nearby the specified location.  This parameter requires the
    #         parameter ``location`` to be specified.
    #
    #     @param sync_time: indicate the earliest time to return photos based on
    #         the time of their most recent modification. If not specified, the
    #         platform returns any available photos, sorted by ascending order
    #         of their modification time.
    #
    #
    #     @return: a list of instances containing the following members:
    #
    #         ``account_id`` (required): identification of the account of the
    #           user who uploaded this photo.
    #
    #         ``creation_time`` (required): time when this photo has been
    #           registered to the platform.
    #
    #         ``location`` (optional): an instance ``GeoPoint`` corresponding
    #           to the geographic coordinates where the photo has been taken.
    #
    #         ``reviewer_id`` (optional): identification of the account of the
    #           expert of the platform who verified this photo prior to being
    #           published on the platform.
    #
    #         ``photo_id`` (required): identification of the photo.
    #
    #         ``photo_url`` (required): Uniform Resource Locator (URL) that
    #           specifies the location of the photo, if any defined.  The client
    #           application can use this URL and append the query parameter ``size``
    #           to specify a given pixel resolution of the photo, such as
    #           ``thumbnail``, ``small``, ``medium``, or ``large``
    #
    #         ``place_id`` (optional): identification of an heritage site this
    #           photo corresponds to.
    #
    #         ``team_ids`` (required): list of identifications of the teams with
    #           which the user shares these photos.  This attributes is returned
    #           when the attribute ``visibility`` equals ``group``.
    #
    #         ``update_time`` (required): time of the last modification of one
    #           or more attributes of this photo.
    #
    #           .. note::
    #
    #              This time should be used by the client application to manage its
    #              cache of photos and to reduce the average time to access data of
    #              photos. When the client application needs to read photos'
    #              attributes, it first checks whether a copy of these data is in its
    #              cache.  If so, the client application immediately reads from the
    #              cache, which is much faster than requesting these data from the
    #              server platform.
    #
    #         ``visibility`` (required): indicate which visibility needs to be
    #           setup for these photos:
    #
    #           ``group``: the photo is restricted to the specified organization(s).
    #             Only the members of these organizations, and the experts of the
    #             platform, can view it.
    #
    #           ``private``: the photo is private.  Only the user who added
    #             this photo, and the experts of the platform, can view.
    #
    #           ``public``: the photo is public.  Anyone registered against
    #             the platform can view it.
    #     """
    #     return [ Object.from_json(payload)
    #             for payload in self.send_request(
    #                     http_method=self.HttpMethod.GET,
    #                     path='/photo',
    #                     arguments={
    #                         'bounds': bounds and '%s,%s,%s,%s' % (bounds[0].longitude, bounds[0].latitude, bounds[1].longitude, bounds[1].latitude),
    #                         'location': location and '%s,%s' % (location.longitude, location.latitude),
    #                         'limit': limit,
    #                         'locale': locale,
    #                         'offset': offset,
    #                         'photo_ids': photo_ids,
    #                         'radius': radius,
    #                         'sync_time': sync_time,
    #                     },
    #                     authentication_required=False,
    #                     signature_required=True) ]
    #
    #
    # def set_photo_rating(self, photo_id, value):
    #     """
    #     Rate a photo on behalf of a user, whether he likes or dislikes this
    #     photo, or whether he has no particular opinion about this photo.
    #
    #
    #     @param photo_id: identification of the photo that is rated.
    #
    #     @param value: a value among the possible following values:
    #
    #         ``-1``: the user dislikes this photo.
    #
    #         ``0``: the user has no particular opinion about this photo.
    #
    #         ``1``: the user likes this photo.
    #
    #
    #     @raise DeletedObjectException: if the specified photo has been
    #         deleted, while the argument ``check_status`` has been set to
    #         ``True``.
    #
    #     @raise DisabledObjectException: if the specified photo has been
    #         disabled, while the argument ``check_status`` has been set to
    #         ``True``.
    #
    #     @raise IllegalAccessException: if the user rates the photo while this
    #         photo is not yet available to the public.
    #
    #     @raise InvalidArgumentException: if the rating value provided by the
    #         user is no in the valid range.
    #
    #     @raise InvalidOperationException: if the user is the owner of the
    #         photo; it is not allowed to rate one's own photo.
    #
    #     @raise UndefinedObjectException: if the specified photo is not
    #         registered to the platform.
    #     """
    #     if value not in range(-1, 2):
    #         raise self.InvalidArgumentException('The rating value of a photo MUST be an integer in the range [-1, 1]')
    #
    #     return Object.from_json(
    #             self.send_request(
    #                     http_method=self.HttpMethod.PUT,
    #                     path='/photo/(photo_id)/rating',
    #                     url_bits={
    #                         'photo_id': photo_id
    #                     },
    #                     arguments={
    #                         'value': value
    #                     },
    #                     authentication_required=True,
    #                     signature_required=True))
