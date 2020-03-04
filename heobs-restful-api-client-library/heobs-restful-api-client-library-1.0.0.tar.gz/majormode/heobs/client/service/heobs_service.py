# Copyright (C) 2015 Majormode.  All rights reserved.
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

from majormode.perseus.model.contact import Contact
from majormode.perseus.client.service.base_service import BaseService
from majormode.perseus.constant.privacy import Visibility
from majormode.perseus.model.locale import DEFAULT_LOCALE
from majormode.perseus.model.obj import Object


class HeritageObservatoryService(BaseService):
    BaseService._declare_custom_exceptions({
    })


    def sign_in(self, email_address, password):
        session = self.session.connection.build_authenticated_session(
                self.send_request(
                    http_method=self.HttpMethod.POST,
                    path='/account/session',
                    message_body={
                        'email_address': email_address,
                        'password': password },
                    authentication_required=False,
                    signature_required=True))

        self.set_session(session)

        return session


    def sign_up(self,
            contacts,
            password,
            username=None,
            fullname=None,
            locale=DEFAULT_LOCALE,
            recaptcha=None,
            auto_sign_in=True):
        """
        Register a new user account against the platform.

        A user account is identified by a contact or/and a username, except
        account that is created from a 3rd-party Social Networking Service
        (SNS), in which case contacts and username are optional.

        A password is mandatory except for botnet, ghost, and SNS user
        accounts.


        @param app_id: identification of the client application such as a Web,
            a desktop, or a mobile application, that accesses the service.

        @param account_type: an item of ``AccountType`` that describes the
            context that caused the registration of this user account.

        @param contacts: a tuple or a list of tuple representing the contacts
            information of this user account.  A contact information
            corresponds to the possible following tuples::

                ``(name, value)``

            or::

                ``(name, value, is_primary)``

            where:

            * ``name``: an item of the enumeration ``Contact.ContactPropertyName``.

            * ``value``: value of the property representing by a string, such
              as ``+84.01272170781``, the formatted value for a telephone
              number property.

            * ``is_primary``: indicate whether this contact information is the
              primary.  By default, the first contact information of a given
              type is the primary.

        @param username:  a name used to gain access to a the platform.  The
            username MUST be unique among all the usernames already registered
            by other users to the platform.  This argument is optional if and
            only if contact information has been passed.

        @param password: password associated to the user account.

        @param fullname: complete full name of the user.

        @param locale: a ``Locale`` instance referencing the preferred
            language of the user.

        @param recaptcha: properties of the reCAPTCHA challenge verification
            that the user has passed, represented by the following tuple:

                (recaptcha_private_key, client_ip_address, recaptcha_challenge, recaptcha_response)

            where:

            * ``recaptcha_private_key``: The private key that was used when
              requesting the reCAPTCHA challenge/response.

            * ``client_ip_address``: the Internet Protocol (IP) address of the
              client application of the user who solved the CAPTCHA challenge.

            * ``recaptcha_challenge``: the token that identifies the challenge
              that reCAPTCHA provided to the user.

            * ``recaptcha_response``: the response that the user provided.

        @param auto_signin: indicate whether the platform is requested to
            sign-in this user once the sign-up procedure completes
            successfully.


        @return: an instance containing the following members:

            * ``account_id``: identification of the account of the user.

            * ``creation_time``: time when this account has been registered.
              This information should be stored by the client application to
              manage its cache of accounts.

            * ``expiration_time``: time when the login session will expire.
              This information is provided if the client application requires
              the platform to automatically sign-in the user (cf. query
              parameter ``auto_sigin``).

            * ``fullname``: complete full name of the user as given by the
              user himself, i.e., untrusted information, or as determined from
              his email address as for a ghost account.

            * ``is_verified``: indicate whether this contact information
              has been verified, whether it has been grabbed from a trusted
              Social Networking Service (SNS), or whether through a challenge/
              response process.  The user should be reminded to confirm his
              contact information if not already verified, or the user would
              take the chance to have his account suspended.

            * ``is_primary``: indicate whether this contact information
              is the primary one for the given property.

            * ``session_id``: identification of the login session of the user.
              This information is provided if the client application requires
              the platform to automatically sign-in the user (cf. query
              parameter ``auto_signin``).

            * ``username``: also known as screen name or nickname, username is
              chosen by the end user to identify himself when accessing the
              platform and communicating with others online.  A username
              should be totally made-up pseudonym, not reveal the real name of
              the person.  The username is unique across the platform.  A
              username is not case sensitive.

        @raise ContactAlreadyUsedException: if one or more contacts are
            already associated and verified for an existing user account.

        @raise InvalidArgumentException: if one or more arguments are not
            compliant with their required format, if some required information
            is missing.

        @raise UsernameAlreadyUsedException: if the specified username is
            already associated with an existing user account.
        """
        if isinstance(contacts, tuple):
            contacts = [ contacts ]

        for (name, value) in contacts:
            if name not in Contact.ContactPropertyName:
                raise ValueError('Invalid contact information "%s"' % name)

        message_body = {
            'contacts': contacts,
            'fullname': fullname,
            'locale': locale,
            'password': password,
            'username': username
        }

        if recaptcha:
            (recaptcha_private_key, recaptcha_challenge, recaptcha_response) = recaptcha
            message_body.update({
                'recaptcha': {
                    'private_key': recaptcha_private_key,
                    'challenge': recaptcha_challenge,
                    'response': recaptcha_response
                }
            })

        session_payload = Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.POST,
                        path='/account',
                        arguments={ 'auto_sign_in': auto_sign_in },
                        message_body=message_body,
                        authentication_required=False,
                        signature_required=True))

        if auto_sign_in:
            self.set_session(self.session.connection.build_authenticated_session(session_payload))

        return session_payload







#
#     def link_place_photos(self, place_id, photo_ids):
#         """
#         Link a list of photos uploaded by the user to a place registered to
#         the platform.
#
#         These photos MUST have been uploaded by the user on behalf of whom
#         this function is called.
#
#         If the specified place has not been reviewed yet, this place MUST have
#         been submitted by the user on behalf of whom this function is called.
#
#
#         @param place_id: identification of the place to link the specified
#             photos to.
#
#         @param photo_ids: a list of identifications of photos that the user
#             has previously uploaded and that he links to the specified place.
#
#
#         @raise DeletedObjectException: if a specified photo has been deleted,
#             if the specified place has been deleted.
#
#         @raise DisabledObjectException: if a specified photo has been
#             disabled, if the specified place has been disabled.
#
#         @raise IllegalAccessException: if a specified photo has been uploaded
#             by another user, if the specified place has been submitted by
#             another user but has not been reviewed yet.
#
#         @raise InvalidOperationException: if a specified photo is already
#             linked to a place registered in the platform.
#
#         @raise UndefinedObjectException: if the specified photo is not
#             registered in the platform, if the specified place is not
#             registered in the platform
#         """
#         return Object.from_json(
#                 self.send_request(
#                         http_method=self.HttpMethod.POST,
#                         path='/place/(place_id)/photo/(photo_ids)',
#                         url_bits={
#                             'photo_ids': ','.join([ photo_id.hex for photo_id in photo_ids ]),
#                             'place_id': place_id
#                         },
#                         authentication_required=True,
#                         signature_required=True))
#
#
#     def submit_place(self, photo_id):
#         """
#         Submit an heritage site identified by a photo already uploaded by the
#         user.
#
#
#         @param photo_id: identification of a geotagged photo that the user has
#             previously uploaded.  This photo MUST no be linked to any heritage
#             site.  This photo MUST NOT be already linked to another heritage
#             site.
#
#
#         @return: an instance containing the following members:
#
#             * ``creation_time`` (required): time when this heritage site has been
#               registered.  This information should be stored by the client
#               application to manage its cache of heritage sites.
#
#             * ``location`` (required): information about the estimated location of
#               the heritage site.
#
#             * ``photo_ids`` (optional): a list of identifications of photos
#                 submitted by this user that may match this heritage site.
#
#             * ``place_id`` (required): identification of the heritage site as
#               registered in the platform.
#
#
#         @raise DeletedObjectException: if the specified photo has been
#             deleted.
#
#         @raise DisabledObjectException: if the specified photo has been
#             disabled.
#
#         @raise IllegalAccessException: if the specified photo has been
#             uploaded by another user.
#
#         @raise InvalidOperationException: if the specified photo is not
#             geotagged, if the specified photo is already linked to an heritage
#             site already registered in the platform, if the specified photo
#             doesn't have location information.
#
#         @raise UndefinedObjectException: if the specified photo is not
#           registered in the platform.
#         """
#         return Object.from_json(
#                 self.send_request(
#                         http_method=self.HttpMethod.POST,
#                         path='/place',
#                         arguments={
#                             'photo_id': photo_id
#                         },
#                         authentication_required=True,
#                         signature_required=True))
#
#
#
#     def sign_up(self,
#             contacts,
#             password,
#             username=None,
#             fullname=None,
#             locale=DEFAULT_LOCALE,
#             recaptcha=None,
#             auto_sign_in=True):
#         """
#         Register a new user account against the platform.
#
#         A user account is identified by a contact or/and a username, except
#         account that is created from a 3rd-party Social Networking Service
#         (SNS), in which case contacts and username are optional.
#
#         A password is mandatory except for botnet, ghost, and SNS user
#         accounts.
#
#
#         @param app_id: identification of the client application such as a Web,
#             a desktop, or a mobile application, that accesses the service.
#
#         @param account_type: an item of ``AccountType`` that describes the
#             context that caused the registration of this user account.
#
#         @param contacts: a tuple or a list of tuple representing the contacts
#             information of this user account.  A contact information
#             corresponds to the possible following tuples::
#
#                 ``(name, value)``
#
#             or::
#
#                 ``(name, value, is_primary)``
#
#             where:
#
#             * ``name``: an item of the enumeration ``Contact.ContactPropertyName``.
#
#             * ``value``: value of the property representing by a string, such
#               as ``+84.01272170781``, the formatted value for a telephone
#               number property.
#
#             * ``is_primary``: indicate whether this contact information is the
#               primary.  By default, the first contact information of a given
#               type is the primary.
#
#         @param username:  a name used to gain access to a the platform.  The
#             username MUST be unique among all the usernames already registered
#             by other users to the platform.  This argument is optional if and
#             only if contact information has been passed.
#
#         @param password: password associated to the user account.
#
#         @param fullname: complete full name of the user.
#
#         @param locale: a ``Locale`` instance referencing the preferred
#             language of the user.
#
#         @param recaptcha: properties of the reCAPTCHA challenge verification
#             that the user has passed, represented by the following tuple:
#
#                 (recaptcha_private_key, client_ip_address, recaptcha_challenge, recaptcha_response)
#
#             where:
#
#             * ``recaptcha_private_key``: The private key that was used when
#               requesting the reCAPTCHA challenge/response.
#
#             * ``client_ip_address``: the Internet Protocol (IP) address of the
#               client application of the user who solved the CAPTCHA challenge.
#
#             * ``recaptcha_challenge``: the token that identifies the challenge
#               that reCAPTCHA provided to the user.
#
#             * ``recaptcha_response``: the response that the user provided.
#
#         @param auto_signin: indicate whether the platform is requested to
#             sign-in this user once the sign-up procedure completes
#             successfully.
#
#
#         @return: an instance containing the following members:
#
#             * ``account_id``: identification of the account of the user.
#
#             * ``creation_time``: time when this account has been registered.
#               This information should be stored by the client application to
#               manage its cache of accounts.
#
#             * ``expiration_time``: time when the login session will expire.
#               This information is provided if the client application requires
#               the platform to automatically sign-in the user (cf. query
#               parameter ``auto_sigin``).
#
#             * ``fullname``: complete full name of the user as given by the
#               user himself, i.e., untrusted information, or as determined from
#               his email address as for a ghost account.
#
#             * ``is_verified``: indicate whether this contact information
#               has been verified, whether it has been grabbed from a trusted
#               Social Networking Service (SNS), or whether through a challenge/
#               response process.  The user should be reminded to confirm his
#               contact information if not already verified, or the user would
#               take the chance to have his account suspended.
#
#             * ``is_primary``: indicate whether this contact information
#               is the primary one for the given property.
#
#             * ``session_id``: identification of the login session of the user.
#               This information is provided if the client application requires
#               the platform to automatically sign-in the user (cf. query
#               parameter ``auto_signin``).
#
#             * ``username``: also known as screen name or nickname, username is
#               chosen by the end user to identify himself when accessing the
#               platform and communicating with others online.  A username
#               should be totally made-up pseudonym, not reveal the real name of
#               the person.  The username is unique across the platform.  A
#               username is not case sensitive.
#
#         @raise ContactAlreadyUsedException: if one or more contacts are
#             already associated and verified for an existing user account.
#
#         @raise InvalidArgumentException: if one or more arguments are not
#             compliant with their required format, if some required information
#             is missing.
#
#         @raise UsernameAlreadyUsedException: if the specified username is
#             already associated with an existing user account.
#         """
#         if isinstance(contacts, tuple):
#             contacts = [ contacts ]
#
#         for (name, value) in contacts:
#             if name not in Contact.ContactPropertyName:
#                 raise ValueError('Invalid contact information "%s"' % name)
#
#         message_body = {
#             'contacts': contacts,
#             'fullname': fullname,
#             'locale': locale,
#             'password': password,
#             'username': username
#         }
#
#         if recaptcha:
#             (recaptcha_private_key, recaptcha_challenge, recaptcha_response) = recaptcha
#             message_body.update({
#                 'recaptcha': {
#                     'private_key': recaptcha_private_key,
#                     'challenge': recaptcha_challenge,
#                     'response': recaptcha_response
#                 }
#             })
#
#         session_payload = Object.from_json(
#                 self.send_request(
#                         http_method=self.HttpMethod.POST,
#                         path='/account',
#                         arguments={ 'auto_sign_in': auto_sign_in },
#                         message_body=message_body,
#                         authentication_required=False,
#                         signature_required=True))
#
#         if auto_sign_in:
#             self.set_session(self.session.connection.build_authenticated_session(session_payload))
#
#         return session_payload
#
#
#     def upload_photos(self,
#             files=None,
#             place_id=None,
#             visibility=Visibility.public,
#             team_ids=None):
#         """
#         Upload a list of photos to the platform.
#
#
#         @note: the platform simply ignores photos file which image format is
#             not supported.
#
#         @note: either the argument ``file_path_names` is specified, either the
#             argument ``files``.  The latter has priority over the argument
#             ``file_path_names``; if both were specified, the function will
#              only use the argument ``files``.
#
#
#         @param files: a list of file-like objects to upload to the platform.
#
#         @param place_id: identification of the heritage site that has been
#             taken in photos, if known.  The set of photos MUST correspond to a
#             same heritage site.
#
#         @param visibility: indicate which visibility needs to be setup for
#             these photos.
#
#         @param team_ids: list of identifications of the teams with which the
#             user shares these photos.  This argument MUST be used when the
#             argument ``visibility`` equals ``organization``.
#
#
#         @return: a list of instances containing the following members:
#
#             * ``error``: this attribute is provided if and only this photo has not
#               been processed successfully.  Its content indicates the error that
#               occurred while processing the photo's uploaded file.  The platform
#               returns only then this attribute and the attribute ``file_name``;
#               all the other attributes are not provided.
#
#               Reasons of error during photo processing can be various:
#
#               * the image format of the photo is not supported
#
#               * the pixel resolution of the photo is below 512px x 256px, in
#                 landscape or portrait mode
#
#               * this photo has been already registered but on behalf of
#                 another user
#
#             * ``file_name``: the original local file name as the ``filename``
#               parameter of the ``Content-Disposition`` header.
#
#             * ``location``: information about the location where the photo has
#               been taken:
#
#               * ``bearing``: angle of the direction that the camera pointed to
#                 when this photo has been taken.
#
#               * ``accuracy``: accuracy in meters of the location where the
#                 photo has been taken.
#
#               * ``altitude``: altitude in meters of the location where the
#                 photo has been taken.
#
#               * ``fix_time``: time when the fix of the location, where the
#                 photo has been taken, has been calculated.
#
#               * ``latitude``: latitude-angular distance, expressed in decimal
#                 degrees (WGS84 datum), measured from the center of the Earth,
#                 of a point north or south of the Equator corresponding to the
#                 the location where the photo has been taken.
#
#               * ``longitude``: longitude-angular distance, expressed in
#                 decimal degrees (WGS84 datum), measured from the center of the
#                 Earth, of a point east or west of the Prime Meridian
#                 corresponding to the location where the photo has been taken.
#
#             * ``photo_id`` (required): identification of the photo that has been
#               uploaded, as registered on the platform.
#
#             * ``update_time``: date and time of the most recent modification of
#               some properties of this photo.  This information should be stored
#               by the client application to manage its cache of photos.
#
#
#         @raise DeletedObjectException: if the specified heritage venue has been
#             deleted.
#
#         @raise DisabledObjectException: if the specified heritage venue has
#             been disabled.
#
#         @raise UndefinedObjectException: if the specified heritage venue is not
#             registered in the platform.
#         """
#         if files is None:
#             raise ValueError('A list of files with their corresponding field names MUST be specified')
#
#         return Object.from_json(
#             self.send_request(
#                 http_method=self.HttpMethod.POST,
#                 path='/photo',
#                 arguments={
#                     'team_ids': team_ids and ','.join([ team_id.hex for team_id in team_ids ]),
#                     'visibility': visibility,
#                 },
#                 files=files,
#                 authentication_required=True,
#                 signature_required=True))
#
#
#     # def add_venue(self, locale,
#     #         address=None,
#     #         category=None,
#     #         contact=None,
#     #         location=None,
#     #         metadata=None,
#     #         timezone=None):
#     #     """
#     #     Add a new heritage venue, which is an official location where pieces of
#     #     political, military, cultural, or social history have been preserved
#     #     due to their cultural heritage value.
#     #
#     #     An heritage venue is described by sets of information:
#     #
#     #     * *geographic coordinates*: degrees of latitude and longitude
#     #       describing the location of the venue on the earth's surface.
#     #
#     #     * *address information*: collection of localized information used
#     #       for describing the location of the  venue, generally using political
#     #       boundaries and street name about the location of the venue.
#     #
#     #     * *contact information*: information about how to contact the owner
#     #       of the venue.
#     #
#     #     * *category*: classification of the venue using a precise taxonomy.
#     #
#     #     @note: the name of the venue corresponds to the address component
#     #        ``recipient_name``.
#     #
#     #     @param locale: an instance of ``Locale`` representing the locale of
#     #         the textual information that describes this venue.
#     #
#     #     @param address: postal address of the venue, composed of one or more
#     #         address components:
#     #
#     #                     [ { type:item, value:string }, ... ]
#     #
#     #         where:
#     #
#     #         * ``type``: type of this component, as an item of the enumeration
#     #             ``AddressComponentType``.
#     #
#     #         * ``value``: textual information of this component, written in the
#     #             specified locale.
#     #
#     #     @param category: a tuple ``(category_id, caption)`` that indicates the
#     #         the particular use this venue has been designed for, or ``None`` if
#     #         this information has not been given::
#     #
#     #         * ``category_id``: identification of a category already registered
#     #           to the platform, or ``None`` if this category has not been
#     #           registered yet.
#     #
#     #         * ``caption``: the human-readable name of a new category, or
#     #           ``None`` if an identification of an existing category has been
#     #           given.
#     #
#     #     @param contact: a list of contact information properties represented
#     #         by tuples of the of the following form:
#     #
#     #            (name:item, value:string, is_primary:boolean)
#     #
#     #         where:
#     #
#     #         * ``name``: an item of the enumeration ``Contact.ContactPropertyName``.
#     #
#     #         * ``value``: value of the property representing by a string, such
#     #           as for instance ``+84.01272170781``, the formatted value for a
#     #           telephone number property.
#     #
#     #         * ``is_primary``: indicate whether this contact information is the
#     #           primary for this venue.  By default, the first contact
#     #           information of a given type is the primary for this venue.
#     #
#     #     @param location: an instance ``GeoPoint`` representing the
#     #         geographic coordinates of the venue.
#     #
#     #     @param metadata: list of metadata that describe more specifically this
#     #         heritage venue.  Metadata provide information about one or more
#     #         aspects of the building such as, for instance, the number of
#     #         floors, date of construction, date of completion, architectural
#     #         style, etc.
#     #
#     #         Each instances contains the following members:
#     #
#     #         * ``caption`` (optional): type of this metadatum information, a
#     #           human-readable insensitive case caption written in the language
#     #           of the user who enters it.
#     #
#     #         * ``class_id`` (optional): identification of the class of this
#     #           metadatum information as already registered to the platform.
#     #           When this member is defined, the attribute ``caption`` is
#     #           ignored if provided.
#     #
#     #         * ``value`` (required): value of this metadatum information, a
#     #           human-readable caption written in the language of the user who
#     #           enters it.
#     #
#     #           @note: the supported type of data currently is limited to text, but
#     #              we are planning to support several other common media types.
#     #
#     #         * ``visibility`` (optional): indicate which visibility needs to be
#     #           setup for this metadatum:
#     #
#     #           * ``organization``: the metadatum is restricted to the specified
#     #             organisations (cf. the argument list composed of ``team_id``).
#     #             Only the members of these organisations, and the  moderators of
#     #             the platform, can view it.
#     #
#     #           * ``private``: the metadatum is private.  Only the user who
#     #             added this metadatum, and the moderators of the platform, can
#     #             view.
#     #
#     #           * ``public``: the metadatum is public.  Anyone registered to
#     #             the platform can view it.
#     #
#     #         * ``[ team_id, ... ]`` (optional): list of identifiers of the
#     #           organisations that are allowed to view this datatum, when the
#     #           visibility is set to ``organization``.
#     #
#     #     @param timezone: time zone of the default location of the venue.  It
#     #          is the difference between the time at this location and UTC
#     #         (Universal Time Coordinated).  UTC is also known as GMT or
#     #          Greenwich Mean Time or Zulu Time.
#     #
#     #     @return: an instance containing the following member:
#     #
#     #         * ``creation_time``:  time when this venue has been registered.
#     #           This information should be stored by the client application to
#     #           manage its cache of venues.
#     #
#     #         * ``venue_id``: identification of the venue as registered against
#     #           the platform.
#     #     """
#     #     message_body = {
#     #         'locale': locale
#     #     }
#     #
#     #     if address:
#     #         message_body['address'] = address
#     #
#     #     if category:
#     #         (category_id, category_caption) = category
#     #         message_body['category'] = {
#     #             'category_id': category_id,
#     #             'caption': category_caption
#     #         }
#     #
#     #     if contact:
#     #         message_body['contact'] = contact
#     #
#     #     if location:
#     #         message_body['location'] = location
#     #
#     #     if metadata:
#     #         message_body['metadata'] = metadata
#     #
#     #     if timezone:
#     #         message_body['timezone'] = timezone
#     #
#     #     return Object.from_json(
#     #             self.send_request(
#     #                 http_method=self.HttpMethod.POST,
#     #                 path='/venue',
#     #                 message_body=message_body,
#     #                 authentication_required=True,
#     #                 signature_required=True))
#     #
#     #
#     # def get_photos(self, photo_ids):
#     #     return Object.from_json(
#     #         self.send_request(
#     #             http_method=self.HttpMethod.GET,
#     #             path='/photo',
#     #             arguments={
#     #                 'ids': photo_ids and ','.join([ photo_id.hex for photo_id in photo_ids ])
#     #             },
#     #             authentication_required=True,
#     #             signature_required=True))
#     #
#     #
#     # def get_venue_categories(self,
#     #         category_ids=None,
#     #         limit=BaseService.DEFAULT_LIMIT, offset=0,
#     #         locale=None, sync_time=None):
#     #     """
#     #     Return a list of building categories that can be used to classify an
#     #     heritage venue, designed for some particular use which it may be
#     #     important to indicate.
#     #
#     #     @param category_ids: list of identifications of categories that
#     #         indicate the particular use of heritage venues to returned.  If no
#     #         category is specified, the function does not no filter heritage
#     #         venues by their category.
#     #
#     #     @param limit: constrain the number of categories that are returned to
#     #         the specified number.  Maximum value is ``venueService.MAXIMAL_CATEGORY_LIMIT``.
#     #         The default value is ``venueService.DEFAULT_CATEGORY_LIMIT``.
#     #
#     #     @param offset: require to skip that many categories before beginning
#     #         to return them.  If both ``limit`` and ``offset`` are specified,
#     #         then ``offset`` categories are skipped before starting to count
#     #         the ``limit`` categories that are returned.
#     #
#     #     @param locale: an instance ``Locale`` that indicate the language to
#     #         return categories.
#     #
#     #     @param sync_time: indicate the time of the latest version of the list
#     #         of categories cached by the client application.  If this time
#     #         corresponds to the most recent version of the categories on the
#     #         platform, the request returns an empty list, otherwise it returns
#     #         the last version of this list.  If this parameter is not provided,
#     #         the request always returns the most recent version of the list of
#     #         categories.
#     #
#     #     @return: a list of instances containing the following members:
#     #
#     #         * ``categories``: a list of categories used to classify heritage
#     #           venues designed for some particular use which it may be important
#     #           to indicate:
#     #
#     #           * ``category_id``: identification of the category.
#     #
#     #           * ``labels``: a list of ``Label`` instances corresponding to
#     #             localized humanely-readable names of this category.
#     #
#     #             * ``account_id``: identification of the account of the user
#     #               who submitted this localized name of the category.
#     #
#     #             * ``caption``: humanely-readable names of this category in a
#     #               given locale.
#     #
#     #             * ``locale``: locale used for the caption of this category is
#     #               return.
#     #
#     #             * ``moderator_id``: identification of the account of a
#     #               moderator of the platform who validated this particular
#     #               localization of the category.
#     #
#     #             * ``object_status``: current status of this localized caption,
#     #               either pending, either reviewed.
#     #
#     #         * ``update_time`` (required): time of the latest version of the list
#     #           of categories.  This time should be cached by the client
#     #           application along with this list of categories.  The client
#     #           application is expected to provide this time when it will request
#     #           the list of categories.
#     #     """
#     #     return [ venueCategory.from_json(payload)
#     #             for payload in self.send_request(
#     #                     http_method=self.HttpMethod.GET,
#     #                     path='/venue/category',
#     #                     arguments={
#     #                         'category_ids': category_ids,
#     #                         'limit': limit,
#     #                         'locale': locale,
#     #                         'offset': offset,
#     #                         'sync_time': sync_time
#     #                     },
#     #                     authentication_required=False,
#     #                     signature_required=True) ]
#     #
#     #
#     # def get_venue_metadata_classes(self,
#     #         limit=BaseService.DEFAULT_LIMIT, offset=0,
#     #         locale=None, sync_time=None):
#     #     """
#     #     Return up to 100 metadata classes that are used to describe more
#     #     specifically heritage venues.  Metadata provide information about one
#     #     or more aspects of buildings such as, for instance, the number of
#     #     floors, date of construction, date of completion, architectural
#     #     style, etc.
#     #
#     #     @param limit: constrain the number of classes that are returned to
#     #         the specified number.  Maximum value is ``venueService.MAXIMAL_ROW_LIMIT``.
#     #         The default value is ``venueService.DEFAULT_LIMIT``.
#     #
#     #     @param offset: require to skip that many classes before beginning to
#     #         return them.  If both ``limit`` and ``offset`` are specified, then
#     #         ``offset`` classes are skipped before starting to count the
#     #         ``limit`` classes that are returned.
#     #
#     #     @param locale: an instance ``Locale`` that indicate the language to
#     #         return classes.
#     #
#     #     @param sync_time: indicate the time of the latest version of the list
#     #         of classes cached by the client application.  If this time
#     #         corresponds to the most recent version of the classes on the
#     #         platform, the request returns an empty list, otherwise it returns
#     #         the last version of this list.  If this parameter is not provided,
#     #         the request always returns the most recent version of the list of
#     #         classes.
#     #
#     #     @return: an instance containing the following members:
#     #
#     #         * ``classes``: a list of classes used to describe more specifically
#     #           heritage venues:
#     #
#     #           * ``class_id``: identification of the metadatum class.
#     #
#     #           * ``labels``: localized humanely-readable names of this class.  If
#     #             the class has not a caption in the specified locale, the platform
#     #             returns all the available localized captions of this class.
#     #
#     #             * ``account_id``: identification of the account of the user who
#     #               submitted this localized name of the class.
#     #
#     #             * ``caption``: human-readable name of the metadatum class in a
#     #               given locale.
#     #
#     #             * ``locale``: an instance ``Locale`` that indicate the language to
#     #               the class is written to.
#     #
#     #             * ``moderator_id``: identification of the account of a moderator
#     #               of the platform who reviewed this particular localization of the
#     #               class.
#     #
#     #             * ``object_status``: current status of this localized caption,
#     #               either pending, either reviewed.
#     #
#     #         * ``update_time``: time of the latest version of the list of classes.
#     #           This time should be cached by the client application along with this
#     #           list of classes.  The client application is expected to provide this
#     #           time when it will request the list of classes.
#     #     """
#     #     return [ venueMetadataClass.from_json(payload)
#     #             for payload in self.send_request(
#     #                     http_method=self.HttpMethod.GET,
#     #                     path='/venue/metadata/class',
#     #                     arguments={
#     #                         'limit': limit,
#     #                         'locale': locale,
#     #                         'offset': offset,
#     #                         'sync_time': sync_time
#     #                     },
#     #                     authentication_required=False,
#     #                     signature_required=True) ]
