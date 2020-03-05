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

import uuid

from majormode.perseus.constant.contact import ContactName
from majormode.perseus.constant.place import AddressComponentType
from majormode.perseus.constant.privacy import Visibility
from majormode.perseus.model.contact import Contact
from majormode.perseus.model.geolocation import GeoPoint
from majormode.perseus.model.label import Label
from majormode.perseus.model.locale import DEFAULT_LOCALE
from majormode.perseus.model.place import Place
from majormode.perseus.utils import cast
import numpy


class HeritageSite(object):
    def __init__(
            self,
            category,
            location,
            site_id=None,
            area_id=None,
            address=None,
            contacts=None,
            locale=DEFAULT_LOCALE,
            timezone=None):
        """

        @param category: an item of the enumeration ``SportCategory``
            representing the sport played at this site.

        @param location: either an instance ``GeoPoint`` corresponding to
            the geographic coordinates of the location, either a polygon
            specifying the geofence's region of the site as an array of
            vertices.  There must be at least three vertices.  Each vertex
            is a tuple composed of a longitude, a latitude, and a altitude::

                [ longitude, latitude, altitude ]
            where:

            * ``altitude`` (optional): altitude in meters of the site.

            * ``latitude`` (required): latitude-angular distance, expressed
              in decimal degrees (WGS84 datum), measured from the center of the
              Earth, of a point north or south of the Equator corresponding to
              the site's location.

            * ``longitude`` (required): longitude-angular distance,
              expressed in decimal degrees (WGS84 datum), measured from the
              center of the Earth, of a point east or west of the Prime
              Meridian corresponding to the site's location.

            Note that the first and last vertices must not be identical; a
            polygon is "auto-closed" between the first and last vertices.

            When specifying the geofence of the site, the function
            automatically computes the coordinates of the geometric center
           (centroid) of the polygon representing the geofence of the sport
            site.  It corresponds to the arithmetic mean ("average")
           position of all the points in the shape.

        @param site_id: the identification of the site when this site
            is already registered against the server platform.

        @param area_id: identification of the geographic area where the
            site is located in.  This parameter is optional if the argument
            ``address`` is passed.  Both ``area_id`` and ``address`` can be
            passed to the constructor.  If this argument is passed to the
            constructor, it takes precedence over any administrative
            division of the same level or larger that would be defined as
            part of the address components.

        @param address:postal address of the site, composed of one or more
            address components, which textual information is written in the
            specified locale.  An address component is defined with a
            component type and its value.  The component type is one of these:

            * ``city``

            * ``country``

            * ``district``: represent districts in rural areas and
              precincts in urban areas.

            * ``hamlet``: small settlement, with a small population, in
              a rural area, or a # component of a larger settlement or
              municipality.

            * ``house_number``: unique number of the  site in the
              street or area, which eases to locate this particular site.
              House numbering schemes vary by site, and in many cases even
              within cities.  In some areas of the world, including many
              remote areas, houses are not numbered at all, instead simply
              being named.  In some other areas, this numbering can be
              composed of a first number along the street followed by a
              second the number along intersecting street, or they would
              adopt a system where the city is divided into small sections
              each with its own numeric code.  The houses within that zone
              are then labeled based on the order in which they were
              constructed, or clockwise around the block.

            * ``neighborhood``: a geographically localised community
              within a larger city, town, # suburb or rural area.
              Neighborhoods are often social communities  with considerable
              face-to-face interaction among members.  Researchers have not
              agreed on an exact definition.  Neighborhood is  generally
              defined spatially as a specific geographic area and
              functionally as a set of social networks.

            * ``postal_code``: postal code as used to address postal
              mail within the country.

            * ``province``

            * ``recipient_name``: intended recipients name or other
              designation, which can be an individual, a business, a site,
              an organization.

            * ``street_name``: street name or odonym, i.e., an
              identifying name, given to the street where the site is
              located in.  The street name usually forms part of the address
              (though addresses in some parts of the world, notably most of
              Japan, make no reference to street names).

            * ``ward``: represent rural communes, commune-level town,
              and urban wards.

        @param contacts: list of properties such as e-mail addresses, phone
            numbers, etc., in respect of the electronic business card
            specification (vCard).  The contact information is represented
            by a list of tuples of the following form::

                [ (name:string, value:string, is_primary:boolean), ... ]

            where:

            * ``name`` (required): type of this contact information, which
              can be one of these standard names in respect of the electronic
              business card specification (vCard):

              * ``FN``: formatted name, i.e., the way that the name is to
                be displayed.

              * ``EMAIL``: e-mail address.

              * ``PHONE``: phone number in E.164 numbering plan, an ITU-T
                recommendation which defines the international public
                telecommunication numbering plan used in the Public Switched
                Telephone Network (PSTN).

              * ``WEBSITE``: Uniform Resource Locator (URL) of a Web site.

            * ``value`` (required): value of this contact information
              representing by a string, such as ``+84.01272170781``, the
              formatted value for a telephone number property.

            * ``is_primary`` (optional): indicate whether this contact
              information is the primary for this site.  By default, the first
              contact information of a given type is the primary of this site.

        @param locale: an instance ``Locale`` of the textual information
            that describes this site.

        @param timezone: time zone at the site's location.  It is the
            difference between the time at this location and UTC
            (Coordinated Universal Time).  UTC is also known as GMT or
            Greenwich Mean Time or Zulu Time.
        """
        self.category = category

        if isinstance(location, GeoPoint):
            self.location = location
            self.geofence = None
        else:
            if len(location) < 3:
                raise ValueError("The polygon of the site's geofence MUST be defined with at least three vertices")

            # Compute the coordinates of the geometric center (centroid) of the
            # polygon representing the geofence of the sport site.  It
            # corresponds to the arithmetic mean ("average") position of all the
            # points in the shape.
            (longitude, latitude, altitude) = numpy.mean(location, axis=0)
            self.location = GeoPoint(longitude, latitude, altitude=altitude)
            self.geofence = location

        self.site_id = site_id

        self.area_id = area_id
        self.address = address
        self.contacts = contacts

        self.locale = locale
        self.timezone = timezone


    @staticmethod
    def from_json(payload):
        """
        Build a ``site`` instance from the specified JSON object.

        @param payload: JSON representation of a site::

                {
                  "area_id": string,
                  "address": {
                    component_type: string,
                    ...
                  }
                  "category": string,
                  "contacts": [
                    [ name:string, value:string, is_primary:boolean ],
                    ...
                  ],
                  "geofence": [ vertex, ... ],
                  "locale": string,
                  "location": coordinates,
                  "timezone": integer
                }

            where:

            * ``area_id`` (optional): identification of the geographic area
              where the site is located in.  This parameter is optional if the
              parameter ``address`` is passed.  Both ``area_id`` and ``address``
              can be passed to the function.  If this parameter is passed to the
              function, it takes precedence over any administrative division of
              the same level or larger that would be defined as part of the
              address components.

            * ``address`` (required): postal address of the site, composed of
              one or more address components, which textual information is
              written in the specified locale.  An address component is defined
              with a component type and its value.  The component type is one of
              these:

                * ``city``

                * ``country``

                * ``district``: represent districts in rural areas and
                  precincts in urban areas.

                * ``hamlet``: small settlement, with a small population, in
                  a rural area, or a # component of a larger settlement or
                  municipality.

                * ``house_number``: unique number of the  site in the
                  street or area, which eases to locate this particular site.
                  House numbering schemes vary by site, and in many cases even
                  within cities.  In some areas of the world, including many
                  remote areas, houses are not numbered at all, instead simply
                  being named.  In some other areas, this numbering can be
                  composed of a first number along the street followed by a
                  second the number along intersecting street, or they would
                  adopt a system where the city is divided into small sections
                  each with its own numeric code.  The houses within that zone
                  are then labeled based on the order in which they were
                  constructed, or clockwise around the block.

                * ``neighborhood``: a geographically localised community
                  within a larger city, town, # suburb or rural area.
                  Neighborhoods are often social communities  with considerable
                  face-to-face interaction among members.  Researchers have not
                  agreed on an exact definition.  Neighborhood is  generally
                  defined spatially as a specific geographic area and
                  functionally as a set of social networks.

                * ``postal_code``: postal code as used to address postal
                  mail within the country.

                * ``province``

                * ``recipient_name``: intended recipients name or other
                  designation, which can be an individual, a business, a site,
                  an organization.

                * ``street_name``: street name or odonym, i.e., an
                  identifying name, given to the street where the site is
                  located in.  The street name usually forms part of the address
                  (though addresses in some parts of the world, notably most of
                  Japan, make no reference to street names).

                * ``ward``: represent rural communes, commune-level town,
                  and urban wards.

            * ``category_id`` (optional): category qualifying this site.

            * ``contacts`` (optional): list of properties such as e-mail
              addresses, phone numbers, etc., in respect of the electronic
              business card specification (vCard).  The contact information is
              represented by a list of tuples of the following form::

                  [ [ name:string, value:string, is_primary:boolean ], ... ]

              where:

              * ``name`` (required): type of this contact information, which
                can be one of these standard names in respect of the electronic
                business card specification (vCard):

                * ``FN``: formatted name, i.e., the way that the name is to
                  be displayed.

                * ``EMAIL``: e-mail address.

                * ``PHONE``: phone number in E.164 numbering plan, an ITU-T
                  recommendation which defines the international public
                  telecommunication numbering plan used in the Public Switched
                  Telephone Network (PSTN).

                * ``WEBSITE``: Uniform Resource Locator (URL) of a Web site.

              * ``value`` (required): value of this contact information
                representing by a string, such as ``+84.01272170781``, the
                formatted value for a telephone number property.

              * ``is_primary`` (optional): indicate whether this contact
                information is the primary for this site.  By default, the first
                contact information of a given type is the primary of this site.

            * ``geofence`` (optional): a polygon specifying the geofence's
              region of this site.  It corresponds to an array of vertices.
              There must be at least three vertices. Each vertex is a tuple
              composed of a longitude, a latitude, and a altitude::

                [ longitude, latitude, altitude ]

              Note that the first and last vertices must not be identical; a
              polygon is "auto-closed" between the first and last vertices.

            * ``locale`` (required): locale of the textual information that
              describes this site.  A locale corresponds to a tag respecting RFC
              4646, i.e., a ISO 639-3 alpha-3 code element optionally followed by
              a dash character ``-`` and a ISO 3166-1 alpha-2 code (referencing
              the country that this language might be specific to).  For example:
              ``eng`` (which denotes a standard English), ``eng-US`` (which
              denotes an American English).

            * ``location`` (optional): geographic coordinates of the location of
              the site represented with the following JSON structure::

                  {
                    "accuracy": decimal
                    "altitude": decimal,
                    "latitude": decimal,
                    "longitude": decimal,
                  }

              where:

              * ``accuracy`` (optional): accuracy of the site's position in
                meters.

              * ``altitude`` (optional): altitude in meters of the site.

              * ``latitude`` (required): latitude-angular distance, expressed
                in decimal degrees (WGS84 datum), measured from the center of the
                Earth, of a point north or south of the Equator corresponding to
                the site's location.

              * ``longitude`` (required): longitude-angular distance,
                expressed in decimal degrees (WGS84 datum), measured from the
                center of the Earth, of a point east or west of the Prime
                Meridian corresponding to the site's location.

                .. note::

                   The parameter ``location`` is ignored when the parameter
                   ``geofence`` is provided.  The platform computes the coordinates
                   of the geometric center (centroid) of the polygon representing the
                   geofence of the sport site.  It corresponds to the arithmetic
                   mean ("average") position of all the points in the shape.

            * ``timezone`` (required): time zone at the site's location.  It is
              the difference between the time at this location and UTC
              (Coordinated Universal Time).  UTC is also known as GMT or
              Greenwich Mean Time or Zulu Time.

        @note: the name of the site corresponds to the address component
            ``recipient_name``.

        @return: a ``site`` instance or ``None`` if the JSON payload is
            nil.
        """
        return payload and \
            Place(
                SiteMetadataClass.from_json(payload.get('category')),
                location=[
                    (float(lon), float(lat), float(alt))
                    for (lon, lat, alt) in payload['geofence']
                ] if payload.get('geofence')
                    else GeoPoint.from_json(payload['location']),
                site_id=cast.string_to_uuid(payload.get('site_id')),
                area_id=cast.string_to_uuid(payload.get('area_id')),
                address=payload.get('address') and dict([
                    (cast.string_to_enum(name, AddressComponentType), value)
                    for (name, value) in payload['address'].iteritems()
                ]),
                contacts=payload.get('contact') and [
                    Contact(cast.string_to_enum(contact[0], ContactName), contact[1], contact[2] if len(contact) == 3 else False)
                    for contact in payload['contacts']
                ],
                locale=cast.string_to_locale(payload.get('locale')) and DEFAULT_LOCALE,
                timezone=payload.get('timezone'))

    def is_info_complete(self):
        """
        Indicate if the information of the site could be considered complete
        or not, i.e., whether it has a name.

        @return: ``True`` if the site's information is complete, ``False``
            otherwise.
        """
        return self.address is not None and \
               self.address.get(AddressComponentType.recipient_name) is not None


class SiteCategory(object):
    """
    MetadataClass that indicates the particular use of heritage site.
    """
    def __init__(self,
            category_id=None,
            labels=None):
        """
        Build an instance ``SiteCategory``.

        @param account_id:  identification of the account
              of the user who submitted this localized name of the category.

        @param category_id: identification of the category.

        @param labels: localized humanely-readable names of this category.  A
            caption is provided by a client application when the category has
            not been already registered to the platform, i.e., the user enters
            a new category.

            * ``account_id`` (required): identification of the account
              of the user who submitted this localized name of the category.

            * ``caption`` (required): humanely-readable names of this
              category in a given locale.

            * ``locale`` (required): locale used for the caption of this
              category is return.

            * ``moderator_id`` (optional): identification of the account
              of a moderator of the platform who reviewed this particular
              localization of the category.

            * ``object_status`` (required): current status of this
              localized caption, either pending, either reviewed.

        @param moderator_id: identification of the account of a moderator of
            the platform who reviewed this localized caption of the category.
        """
        if not (category_id or labels):
            raise ValueError("MetadataClass of heritage site MUST be defined either by an identification or a localized caption")

        self.is_new = category_id is None
        self.category_id = category_id or uuid.uuid1()
        self.labels = labels

    @property
    def label(self):
        if len(self.labels) != 1:
            raise ValueError('This category has no localized caption or more than one localized caption defined')

        return self.labels[0]

    @staticmethod
    def from_json(payload, locale=None):
        if not payload:
            return None

        category_id = cast.string_to_uuid(payload.get('category_id'), strict=False)

        labels_payload = payload.get('labels')
        if labels_payload:
            labels = []
            for label_payload in labels_payload:
                label = Label.from_json(label_payload)
                if locale:
                    label.locale = locale

                label.account_id = cast.string_to_uuid(label_payload.get('account_id'))
                label.moderator_id = cast.string_to_uuid(label_payload.get('moderator_id'))

                labels.append(label)

        else:
            labels = None if category_id else [ Label(payload['caption'], locale) ]

        return SiteCategory(
                category_id=cast.string_to_uuid(payload.get('category_id')),
                labels=labels)


class SiteMetadataClass(object):
    """
    Matadatum class that is used to describe more specifically heritage
    sites.  Metadata provide information about one or more aspects of
    buildings such as, for instance, the number of floors, date of
    construction, date of completion, architectural style, etc.
    """
    def __init__(
            self,
            class_id=None,
            labels=None,
            visibility=Visibility.public,
            team_ids=None):
        """
        Build an instance ``SiteMetadataClass``.

        @param account_id:  identification of the account of the user who
            submitted this localized name of the class.

        @param class_id: identification of the class.

        @param labels: localized humanely-readable names of this class.  A
            caption is provided by a client application when the class has
            not been already registered to the platform, i.e., the user enters
            a new class.

            * ``account_id`` (required): identification of the account
              of the user who submitted this localized name of the class.

            * ``caption`` (required): human-readable names of this
              class in a given locale.

            * ``locale`` (required): locale used for the caption of this
              class is return.

            * ``moderator_id`` (optional): identification of the account
              of a moderator of the platform who reviewed this particular
              localization of the class.

            * ``object_status`` (required): current status of this
              localized caption, either pending, either reviewed.

        @param moderator_id: identification of the account of a moderator of
            the platform who reviewed this localized caption of the class.

        @param visibility: an item of the enumeration ``Visibility`` that
            indicates which visibility needs to be setup for this metadatum
            class.

        @param team_ids: list of identifications of the teams that are allowed
            to view metadata of this class, when the visibility is set to
            ``Visibility.organization``.
        """
        if not (class_id or labels):
            raise ValueError("Metadatum class of heritage site MUST be defined either by an identification or a localized caption")

        self.is_new = class_id is None
        self.class_id = class_id or uuid.uuid1()
        self.labels = labels
        self.team_ids = team_ids
        self.visibility = visibility


    @staticmethod
    def from_json(payload, locale=None):
        """
        Build an instance ``SiteMetadataClass`` from a JSON expression.

        @param payload: a JSON expression of the following structure:

                {
                  "class_id": string,
                  "labels": [
                    {
                      "account_id": string,
                      "caption": string,
                      "locale": string,
                      "moderator_id": string,
                      "object_status": integer
                    },
                    ...
                  ],
                  "team_ids": [ string, ... ],
                  "visibility": string
                }

            where:

            * ``class_id`` (required): identification of the class.

            * ``labels`` (required): localized human-readable names of this
              class.  If the class has not a caption in the specified locale,
              the platform returns all the available localized captions of
              this class.

              * ``account_id`` (required): identification of the account of
                the user who submitted this localized name of the class.

              * ``caption`` (required): human-readable names of this class in
                a given locale.

              * ``locale`` (required): locale used for the caption of this
                class is return.  A locale corresponds to a tag respecting
                RFC 4646, i.e., a ISO 639-3 alpha-3 code element optionally
                followed by a dash character ``-`` and a ISO 3166-1 alpha-2
                code (referencing the country that this language might be
                specific to).  For example: ``eng`` (which denotes a standard
                English), ``eng-US`` (which denotes an American English).

              * ``moderator_id`` (optional): identification of the account of
                a moderator of the platform who reviewed this particular
                localization of the class.

              * ``object_status`` (required): current status of this localized
                caption, either pending, either reviewed.

            * ``team_ids`` (optional): list of identifications of the teams
              that are allowed to view this metadatum.

            * ``visibility`` (optional): indicate which visibility needs to be
              setup for these metadatum:

              * ``organization``: the metadatum is restricted to the
                specified organisations (cf. the argument list composed of
                ``team_id``). Only the members of these organisations, and the
                moderators of the platform, can view it.

              * ``private``: the metadatum is private.  Only the user who
                added this metadatum, and the moderators of the platform, can
                view.

              * ``public``: the metadatum is public.  Anyone registered to
                the platform can view it.

        @param locale: an instance ``Locale`` that indicates the language in
            which the caption of the class is written.  If the JSON
            attribute ``locale`` is defined, it overrides this argument
            ``locale``.

        @return: an instance ``SiteMetadataClass``.
        """
        if not payload:
            return None

        labels = []
        for label_payload in payload['labels']:
            label = Label.from_json(label_payload)
            if locale:
                label.locale = locale

            label.account_id = cast.string_to_uuid(label_payload.get('account_id'))
            label.moderator_id = cast.string_to_uuid(label_payload.get('moderator_id'))

            labels.append(label)

        return SiteMetadataClass(
            class_id=cast.string_to_uuid(payload.get('class_id')),
            labels=labels,
            team_ids=payload.get('team_ids') and [
                cast.string_to_uuid(team_id)
                for team_id in payload['team_ids']
            ],
            visibility=cast.string_to_enum(payload.get('visibility'), Visibility, strict=False) and Visibility.public)
