# Copyright (C) 2017 Majormode.  All rights reserved.
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

from majormode.heobs.model.alert import AlertFrequency

from majormode.perseus.client.service.base_service import BaseService
from majormode.perseus.model.obj import Object


class AlertService(BaseService):
    BaseService._declare_custom_exceptions({
    })


    def get_area_subscriptions(self):
        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.GET,
                        path='/area/subscription',
                        authentication_required=True,
                        signature_required=True))


    def sync_area_subscriptions(self, area_subscriptions):
        return Object.from_json(
                self.send_request(
                        http_method=self.HttpMethod.PUT,
                        path='/area/subscription',
                        message_body=area_subscriptions,
                        authentication_required=True,
                        signature_required=True))

