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
from majormode.perseus.constant.privacy import Visibility
from majormode.perseus.model.locale import DEFAULT_LOCALE
from majormode.perseus.model.obj import Object

from majormode.utils import cast


class HeritageAtRiskService(BaseService):
    BaseService._declare_custom_exceptions({
    })


    def add_photo(self, file,
            locale=DEFAULT_LOCALE,
            suggest_address=True,
            suggest_places=True,
            report_id=None):
        """
        Upload a photo of a heritage at risk.  
        
        If the report to add this photo to is not specified, the platform
        automatically creates a new report and attach to it this photo.  The
        user will be able to add more photos to this report.
        
        The photo is only accessible by the user who sent it until this user
        submits his report for review.
        
        If the photo file has Exif GPS tag, the platform will try its best to
        find a heritage registered to the platform that would match this
        photo.  Up to the user, or a reviewer of the platform, to confirm this
        suggestion.

        For safety and security reasons, the platform removes all meta data
        from the photo file.


        @param file: a file-like object of the image file of the photo to
            upload to the platform.

        @param locale: an instance `Locale` to return textual information in,
            such as the suggested address of the location where the photo has
            been taken, or the name of heritage sites that could possibly
            correspond to the photo taken by the user.
            
        @param suggest_address: indicate whether the platform needs to suggest
            the address of the location where the photo has been taken, if the
            Exif information of this photo contains GPS meta data.  The
            textual content of the address components is returned in the
            specified locale, whenever possible.
            
        @param suggest_places: indicate whether the platform needs to suggest
            a list of heritage sites that could possibly correspond to the 
            photo that the user has taken.  The name and address of these
            places are returned in the specified locale, whenever possible.
            
            
        @return: an instance containing the following members:
        
            * ``areas`` (optional): suggested geographic areas of the location where
              the photo has been taken:
            
              * ``area_id`` (required): identification of an administrative
                subdivision.
            
              * ``area_level`` (required): administrative level of this area.  For
                clarity and convenience the standard neutral reference for the largest
                administrative subdivision of a country is called the "first-level
                administrative division" or "first administrative level".  Next
                smaller is called "second-level administrative division" or "second
                administrative level".
            
              * ``content`` (required): name of this administrative subdivision.
            
              * ``locale`` (required): locale in which the name of the administrative
                subdivision is given.
            
              * ``parent_id`` (optional): identification of the parent administrative
                subdivision.
            
            * ``capture_time`` (optional): local date and time when the original
              image data were generated, which, for a digital still camera, is the
              date and time the picture was taken or recorded.
            
            * ``location`` (optional): information about the location where the
              photo has been taken:
            
              * ``bearing`` (optional): angle of the direction that the camera pointed
                to when this photo has been taken.
            
              * ``accuracy`` (optional): accuracy in meters of the location where the
                photo has been taken.
            
              * ``altitude`` (optional): altitude in meters of the location where the
                photo has been taken.
            
              * ``fix_time`` (optional): time when the fix of the location, where the
                photo has been taken, has been calculated.
            
              * ``latitude`` (required): latitude-angular distance, expressed in
                decimal degrees (WGS84 datum), measured from the center of the Earth,
                of a point north or south of the Equator corresponding to the location
                where the photo has been taken.
            
              * ``longitude`` (required): longitude-angular distance, expressed in
                decimal degrees (WGS84 datum), measured from the center of the Earth,
                of a point east or west of the Prime Meridian corresponding to the
                location where the photo has been taken.
            
              .. note::
            
                 The client application SHOULD compare the time when the GPS fix has
                 been calculated with the time when the photo has been recorded.  If
                 the delta is more than a few minutes, the GPS location might not
                 correspond to the position where the user took this photo.  The client
                 SHOULD inform the user that he needs to refresh the GPS location of
                 his device just before he takes a picture with his camera app.
            
            * ``suggested_location`` (optional): information about the estimated
              location of the heritage at risk:
            
              * ``accuracy`` (optional): accuracy in meters of the estimeated
                location of the heritage at risk.
            
              * ``latitude`` (required): latitude-angular distance, expressed in
                decimal degrees (WGS84 datum), measured from the center of the Earth,
                of a point north or south of the Equator corresponding to the
                estimated location of the heritage at risk.
            
              * ``longitude`` (required): longitude-angular distance, expressed in
                decimal degrees (WGS84 datum), measured from the center of the Earth,
                of a point east or west of the Prime Meridian corresponding to the
                estimated location of the heritage at risk.
            
            * ``photo_id`` (required): identification of the photo that has been
              uploaded, as registered on the platform.
            
            * ``photo_url`` (optional): Uniform Resource Locator (URL) that
              specifies the location of the photo, if any defined.  The client
              application can use this URL and append the query parameter ``size``
              to specify a given pixel resolution of the photo, such as
              ``thumbnail``, ``small``, ``medium``, or ``large``.
            
            * ``report_id`` (required): identification of the report of the
              heritage at risk.
            
            * ``suggested_places`` (optional): a list of places already registered
              to the platform that may correspond to this photo, sorted in
              descending order of relevance:
            
              * ``address`` (optional): postal address of the suggested heritage that
                may match the photo of the user.  This address is composed of one or
                more address components, which textual information is written in the
                specified locale.  An address component is defined with a component
                type and its value.  The component type can be one of these:
            
                * ``house_number``: unique number of the place in the street or area,
                  which eases to locate this particular venue.  House numbering schemes
                  vary by place, and in many cases even within cities.  In some areas of
                  the world, including many remote areas, houses are not numbered at
                  all, instead simply being named.  In some other areas, this numbering
                  can be composed of a first number along the street followed by a
                  second the number along intersecting street, or they would adopt a
                  system where the city is divided into small sections each with its own
                  numeric code.  The houses within that zone are then labeled based on
                  the order in which they were constructed, or clockwise around the
                  block.
            
                * ``street_name``: street name or odonym, i.e., an identifying name,
                  given to the street where the venue is located in.  The street name
                  usually forms part of the address (though addresses in some parts of
                  the world, notably most of Japan, make no reference to street names).
            
                * ``ward``: represent rural communes, commune-level town, and urban
                  wards.
            
                * ``district``: represent districts in rural areas and precincts in
                  urban areas.
            
                * ``city``
            
                * ``postal_code``: postal code as used to address postal mail within the
                  country.
            
                * ``province``
            
                * ``recipient_name``: intended recipients name or other designation,
                  which can be an individual, a business, a venue, an organization.
            
                * ``country``
            
              * ``category_id`` (optional): identification of the category of this
                heritage.
            
              * ``location`` (required): geographic location of the heritage.
            
                * ``accuracy`` (optional): accuracy in meters of the location.
            
                * ``altitude`` (optional): altitude in meters of the location.
            
                * ``latitude`` (required): latitude-angular distance, expressed in
                  decimal degrees (WGS84 datum), measured from the center of the Earth,
                  of a point north or south of the Equator corresponding to the
                  location.
            
                * ``longitude`` (required): longitude-angular distance, expressed in
                  decimal degrees (WGS84 datum), measured from the center of the Earth,
                  of a point east or west of the Prime Meridian corresponding to the
                  location.
            
              * ``object_status`` (required): current status of the record of this
                heritage, whether it is ``enabled`` or still ``pending``.
            
              * ``place_id`` (required): identification of the heritage as registered
                to the platform.
            
              * ``score`` (required): relevance score of this suggested heritage in
                a match with the submitted photo, from ``0.0`` to ``1.0``.  The higher
                the score, the higher the relevance of the suggested heritage.
            
              * ``update_time``: time of the most recent modification of an attribute
                of the information of this heritage.
            
            * ``update_time`` (required): date and time of the most recent mod
              modification of some properties of this photo.  This information
              should be stored by the client application to manage its cache of
              photos.
                
        
        @raise ClosedObjectException: if the specified report has been closed
            by the experts who reviewed it.
            
        @raise DeletedObjectException: if the specified report has been
            cancelled by the user who submitted it.

        @raise DisabledObjectException: if the specified report has been
            rejected by experts of the platform.

        @raise IllegalAccessException: if the photo has been already submitted
            by another user.
            
        @raise InvalidArgumentException: if the size of the photo is not in
            the interval of the accepted minimum and maximum sizes, or if file
            format of the photo is not supported.  

        @raise InvalidOperationException: if the photo has been already
            submitted by the user but for another report.
    
        @raise UndefinedObjectException: if the specified report is not
            registered to the platform.
        """
        if file is None:
            raise ValueError('The image file of a photo MUST be specified')

        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.POST,
                        path='/har/report/(report_id)/photo' if report_id else '/har/photo',
                        url_bits={
                            'report_id': report_id
                        },
                        arguments={
                            'locale': locale,
                            'suggest_address': suggest_address,
                            'suggest_places': suggest_places
                        },
                        files=file,
                        authentication_required=True,
                        signature_required=True))


    def get_report(self, report_id,
            include_address=True,
            include_photos=True,
            locale=DEFAULT_LOCALE):
        """
        Return extended information about the specified heritage at risk
        report.


        @note: the visibility of this report depends on its current status:
        
            * ``draft``: the report is only visible by the user who created it.
           
            * ``submitted``: the report is visible to the users who have been
              designated as reviewers of the geographic area where the heritage at
              risk is located in.
            
            * ``enabled``: the report is visible to all the users of the platform,
              even those who are anonymous.
        
        
        @param report_id: identification of the report of a heritage at risk.
         
        @param include_address: 
        
        @param include_photos: 
        
        @param locale: an instance ``Locale`` in which to return any textual
            information of the heritage at risk report.
        
        
        @return: 
        
        
        @raise DeletedObjectException: if the specified report has been
            cancelled by the user who created it.

        @raise DisabledObjectException: if the specified report has been
            rejected.

        @raise IllegalAccessException: if the report is not currently visible
            to the user on behalf of whom this function is called.
            
        @raise UndefinedObjectException: if the specified report is not
            registered to the platform.       
        """
        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.POST,
                        path='/har/report/(report_id)',
                        url_bits={
                            'report_id': report_id
                        },
                        arguments={
                            'include_address': include_address,
                            'include_photos': include_photos,
                            'locale': locale
                        },
                        authentication_required=True,
                        signature_required=True))


    def review_report(self, report_id, review_action):
        """
        Review the specified heritage at risk report submitted by a user on
        behalf of another user who have been designated as reviewer of the
        geographic area this heritage is located in.
        
        
        @param report_id: identification of the heritage at risk report to
            review.
             
        @param review_action: an item of the enumeration ``ReportReviewAction``
            representing the action selected by the reviewer related to the
            heritage at risk report.
    
    
        @return: 
        """
        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.POST,
                        path='/har/report/(report_id)/review',
                        url_bits={
                            'report_id': report_id
                        },
                        arguments={
                            'action': review_action
                        },
                        authentication_required=True,
                        signature_required=True))
