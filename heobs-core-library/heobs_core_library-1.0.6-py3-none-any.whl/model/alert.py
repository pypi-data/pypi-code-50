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

from majormode.perseus.constant.obj import ObjectStatus
from majormode.perseus.utils import cast

from heobs.constant.alert import AlertFrequency


class AreaSubscriptionSync(object):
    """
    Represent the subscription of a user to alerts from a geographic area
    to be synchronized with the server platform.
    """
    def __init__(
            self,
            area_id,
            object_status,
            frequency=None):
        """
        Build an instance ``AreaAlertSubscriptionSync`` used to synchronize
        the subscription of a user to alerts from a geographic area.


        @param area_id: identification of a geographic area.
         
        @param object_status: current status of the subscription of the user to
            alerts from this geographic area:
            
            * ``ObjectStatus.pending``: the user is subscribing to alerts from
              this geographic area.
         
            * ``ObjectStatus.enabled``: the user has changed the properties of his
              subscription to alerts from this geographic area, i.e., the frequency
              at which alerts should be sent to him.

            * ``ObjectStatus.deleted``: the user is unsubscribing from alerts from
              this geographic area.
         
        @param frequency: an item of the enumeration ``AlertFrequency`` which
            indicates the frequency at which alerts related to this geographic
            area should be sent to the user.  This argument MUST be specified
            when the user subscribes to alerts from the geographic area.
        """
        self.area_id = area_id

        assert object_status in (ObjectStatus.pending, ObjectStatus.enabled, ObjectStatus.deleted), 'Invalid status of the subscription to synchronize'
        assert object_status == ObjectStatus.deleted or frequency is not None, 'The frequency argument MUST be passed'
        self.object_status = object_status

        self.frequency = frequency

    @staticmethod
    def from_json(payload):
        return payload and AreaSubscriptionSync(
            cast.string_to_uuid(payload['area_id']),
            cast.string_to_enum(payload['object_status'], ObjectStatus),
            frequency=cast.string_to_enum(payload.get('frequency'), AlertFrequency))
