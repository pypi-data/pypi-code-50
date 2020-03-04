# # Copyright (C) 2016 Majormode.  All rights reserved.
# #
# # This software is the confidential and proprietary information of
# # Majormode or one of its subsidiaries.  You shall not disclose this
# # confidential information and shall use it only in accordance with
# # the terms of the license agreement or other applicable agreement you
# # entered into with Majormode.
# #
# # MAJORMODE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# # SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING
# # BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY,
# # FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  MAJORMODE
# # SHALL NOT BE LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE
# # AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS
# # DERIVATIVES.
# #
# # @version $Revision$
#
# from majormode.perseus.client.service.base_service import BaseService
# from majormode.perseus.constant.privacy import Visibility
# from majormode.perseus.model.locale import DEFAULT_LOCALE
# from majormode.perseus.model.obj import Object
#
# from majormode.utils import cast
#
#
# class ExpertService(BaseService):
#     BaseService._declare_custom_exceptions({
#     })
#
#
#     def get_areas_experts(self, area_id,
#             limit=None,
#             sync_time=None):
#         """
#         Return a list of user accounts of the experts for the specified
#         geographic areas.
#
#
#         @param area_id: identification of a geographic area.
#
#
#         @return: a list of instances containing the following members:
#
#             * ``account_id`` (required): identification of the user account of an
#               expert of this geographic area.
#
#             * ``fullname`` (optional): full name of the user.
#
#             * ``username`` (optional): name of the account of the user, if any
#               defined.
#
#             * ``picture_id`` (optional): identification of the user account's
#               picture, if any picture defined for this user account.
#
#             * ``picture_url`` (optional): Uniform Resource Locator (URL) that
#               specifies the location of the user account's picture, if any
#               defined.  The client application can use this URL and append the
#               query parameter ``size`` to specify a given pixel resolution of the
#               user account's picture, such as ``thumbnail``, ``small``,
#               ``medium``, ``large``.
#         """
#         return self.send_request(
#                 http_method=self.HttpMethod.GET,
#                 path='/area/(area_id)/expert',
#                 url_bits={
#                     'area_id': area_id.hex,
#                 },
#                 authentication_required=True,
#                 signature_required=True)
