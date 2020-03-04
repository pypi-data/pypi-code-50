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
# from majormode.perseus.model.locale import DEFAULT_LOCALE
# from majormode.perseus.model.obj import Object
#
#
# class BenefactorService(BaseService):
#     BaseService._declare_custom_exceptions({
#     })
#
#
#     def get_benefactors(self,
#             limit=None,
#             locale=DEFAULT_LOCALE,
#             offset=0,
#             sync_time=None):
#         """
#         Return a list of benefactors, worth of extended information.
#
#
#         @param limit: constrain the number of benefactors that are returned to
#             the specified number.
#
#         @param locale: an instance ``Locale`` to return textual information of
#             the benefactors, such as their address information.
#
#         @param offset: require to skip that many benefactors before beginning
#             to return them.  If both ``limit`` and ``offset`` are specified,
#             then ``offset`` benefactors are skipped before starting to count
#             the ``limit`` benefactors that are returned.
#
#         @param sync_time: indicate the earliest time to return benefactors
#             based on the time of their most recent modification.  If not
#             specified, the platform returns any benefactors, sorted by
#             ascending order of their modification time.
#
#
#         @return: a list of instances containing the following members:
#         """
#         return [ Object.from_json(payload)
#                 for payload in self.send_request(
#                         http_method=self.HttpMethod.GET,
#                         path='/benefactor',
#                         arguments={
#                             'limit': limit,
#                             'locale': locale,
#                             'offset': offset,
#                             'sync_time': sync_time,
#                         },
#                         authentication_required=False,
#                         signature_required=True) ]
