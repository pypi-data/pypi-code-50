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
# from majormode.perseus.model.obj import Object
#
#
# class WatermarkService(BaseService):
#     BaseService._declare_custom_exceptions({
#     })
#
#     # Default transparency to bend a watermark into a photo of a user.  The
#     # opacity setting is applied uniformly across the entire watermark.
#     # Opacity is in the range ``0.0`` to ``1.0``, both included.  The lower
#     # value, the more transparent.  An opacity value of ``1.0`` means the
#     # watermark is fully opaque; an opacity value of ``0.0`` means the
#     # watermark is not at all opaque, i.e., fully transparent.
#     DEFAULT_OPACITY = 0.25
#
#     # Default relative positioning of a watermark on a photo on both the X
#     # and Y axes expressed in the format ``XxY`` where ``X`` and ``Y``
#     # represent values in the range 0.0 to 1.0, both included:
#     #
#     #     +------------------+
#     #     |                  |
#     #     |                  |
#     #     |                  |
#     #     | +----+           |
#     #     | |    |           |
#     #     | +----+           |
#     #     +------------------+
#     DEFAULT_POSITION = '0.1x0.9'
#
#     # Default counterclockwise rotation in degrees to apply to a watermark
#     # before embedding it in a photo of a user.  Rotation is in the range
#     # ``0`` to ``360``, where ``0`` is inclusive and ``360`` is exclusive.
#     DEFAULT_ROTATION = 0
#
#     # Default scale of a watermark compared to the size of a photo to embed
#     # the watermark in.  Scale is in the range ``0.0`` to ``1.0``, both
#     # included.  The lower value, the smaller the watermark.  A scale value
#     # of ``1.0`` means the watermark covers completely the photo.
#     DEFAULT_SCALE = 0.1
#
#
#     def delete_watermark(self, app_id, account_id, watermark_id):
#         """
#         Delete the specified watermark.
#
#
#         @param watermark_id: identification of a watermark to delete.
#
#
#         @raise IllegalAccessException: if the watermark has been registered by
#             another user.
#
#         @raise UndefinedObjectException: if the specified watermark doesn't
#             not exist.
#         """
#         return Object.from_json(
#             self.send_request(
#                 http_method=self.HttpMethod.DELETE,
#                 path='/watermark/(watermark_id)',
#                 url_bits={
#                     'watermark_id': watermark_id
#                 },
#                 authentication_required=True,
#                 signature_required=True))
#
#
#     def get_watermarks(self):
#         """
#         Return up to 100 watermarks, worth of extended information, registered
#         by the authenticated user.
#
#
#         @return: a list of instances containing the following members:
#
#             * ``creation_time`` (required): date and time when the user uploaded
#               this watermark to the platform.
#
#             * ``image_height`` (required): number of pixel rows of the watermark's
#               image.
#
#             * ``image_width`` (required): number of pixel columns of the
#               watermark's image.
#
#             * ``object_status`` (required): current status of this watermark:
#
#               * ``OBJECT_STATUS_ENABLED``: this watermark is automatically
#                 embedded to any photos that the user uploads to the platform.
#
#               * ``OBJECT_STATUS_DISABLED``: this watermark is not embedded to
#                 photos that the user uploads to the platform.
#
#               * ``OBJECT_STATUS_DELETED``: this watermark has been deleted; it
#                 cannot be used anymore.
#
#             * ``opacity`` (required): transparency to bend the watermark into a
#               photo of this user.  The opacity setting is applied uniformly across
#               the entire watermark.  Opacity is in the range ``0.0`` to ``1.0``,
#               both included.  The lower value, the more transparent.  An opacity
#               value of ``1.0`` means the watermark is fully opaque; an opacity
#               value of ``0.0`` means the watermark is not at all opaque, i.e.,
#               fully transparent.
#
#             * ``position`` (required): relative positioning on both the X and Y
#               axes expressed in the format ``X%xY%`` where ``X%`` and ``Y%``
#               represent values in the range ``0.0`` to ``1.0``, both included.
#
#             * ``rotation`` (required): counterclockwise rotation in degrees to
#               apply to the watermark before embedding it in a photo of the user.
#               Rotation is in the range ``0`` to ``360``, where ``0`` is inclusive
#               and ``360`` is exclusive.
#
#             * ``scale`` (required): scale of the watermark compared to the size of
#               the photo to embed the watermark in.  Scale is in the range ``0.0``
#               to ``1.0``, both included.  The lower value, the smaller the
#               watermark.  A scale value of ``1.0`` means the watermark covers
#               completely the photo.
#
#             * ``update_time`` (required): date and time of the last modification
#               of one or more properties of this watermark.
#
#             * ``watermark_id`` (required): identification of the watermark.
#         """
#         return Object.from_json(
#             self.send_request(
#                 http_method=self.HttpMethod.GET,
#                 path='/watermark',
#                 authentication_required=True,
#                 signature_required=True))
#
#
#     def set_watermark_options(self, watermark_id,
#             opacity=None,
#             position=None,
#             rotation=None,
#             scale=None):
#         """
#         Redefine one or more options of a watermark.
#
#
#         @param watermark_id: identification of a watermark to change the
#             specified options.
#
#         @param opacity: transparency to bend the watermark into a photo of
#             this user.  The opacity setting is applied uniformly across the
#             entire watermark.  Opacity is in the range ``0.0`` to ``1.0``,
#             both included.  The lower value, the more transparent.  An opacity
#             value of ``1.0`` means the watermark is fully opaque; an opacity
#             value of ``0.0`` means the watermark is not at all opaque, i.e.,
#             fully transparent.
#
#         @param position: relative positioning on both the X and Y axes
#             expressed in the format ``XxY`` where ``X`` and ``Y`` represent
#             values in the range 0.0 to 1.0, both included.
#
#         @param rotation: counterclockwise rotation in degrees to apply to the
#             watermark before embedding it in a photo of the user.  Rotation is
#             in the range ``0`` to ``360``, where ``0`` is inclusive and
#             ``360`` is exclusive.
#
#         @param scale: scale of the watermark compared to the size of the photo
#             to embed the watermark in.  Scale is in the range ``0.0`` to
#             ``1.0``, both included.  The lower value, the smaller the
#             watermark. A scale value of ``1.0`` means the watermark covers
#             completely the photo.
#
#
#         @raise IllegalAccessException: if the watermark has been registered by
#             another user.
#
#         @raise InvalidOperationException: if no option has been specified.
#
#         @raise UndefinedObjectException: if the specified watermark doesn't
#             not exist.
#         """
#         return Object.from_json(
#             self.send_request(
#                 http_method=self.HttpMethod.PUT,
#                 path='/watermark/(watermark_id)/option',
#                 url_bits={
#                     'watermark_id': watermark_id
#                 },
#                 arguments={
#                     'opacity': opacity,
#                     'position': position,
#                     'rotation': rotation,
#                     'scale': scale
#                 },
#                 authentication_required=True,
#                 signature_required=True))
#
#
#     def set_watermark_status(self, watermark_id, object_status):
#         """
#         Enable or disable a specified watermark.
#
#         If the user enables this watermark, the platform will automatically
#         deactivate any other watermark of this user that would be enabled.
#
#
#         @param watermark_id: identification of a watermark to enable or
#             disable.
#
#         @param value: indicate whether to enable or to disable the
#             watermark:
#
#             * ``OBJECT_STATUS_ENABLED``: enable the watermark.  This watermark is
#               automatically embedded to any photos that the user uploads to the
#               platform.
#
#             * ``OBJECT_STATUS_DISABLED``: disable the watermark.  This watermark
#               is not embedded to photos that the user uploads to the platform.
#
#
#         @raise IllegalAccessException: if the watermark has been registered by
#             another user.
#
#         @raise InvalidOperationException: if the specified status has not a
#             valid value.
#
#         @raise UndefinedObjectException: if the specified watermark doesn't
#             not exist.
#         """
#         return Object.from_json(
#             self.send_request(
#                 http_method=self.HttpMethod.PUT,
#                 path='/watermark/(watermark_id)/status',
#                 url_bits={
#                     'watermark_id': watermark_id
#                 },
#                 arguments={
#                     'value': object_status
#                 },
#                 authentication_required=True,
#                 signature_required=True))
#
#
#     def upload_watermark(self, file,
#             opacity=DEFAULT_OPACITY,
#             position=DEFAULT_POSITION,
#             rotation=DEFAULT_ROTATION,
#             scale=DEFAULT_SCALE):
#         """
#         Register a watermark uploaded to the platform.
#
#
#         @param file: a list of file-like objects to upload to the platform.
#
#         @param opacity: transparency to bend the watermark into a photo of
#             this user.  The opacity setting is applied uniformly across the
#             entire watermark.  Opacity is in the range ``0.0`` to ``1.0``,
#             both included.  The lower value, the more transparent.  An opacity
#             value of ``1.0`` means the watermark is fully opaque; an opacity
#             value of ``0.0`` means the watermark is not at all opaque, i.e.,
#             fully transparent.
#
#         @param position: relative positioning on both the X and Y axes
#             expressed in the format ``XxY`` where ``X`` and ``Y`` represent
#             values in the range 0.0 to 1.0, both included.
#
#         @param rotation: counterclockwise rotation in degrees to apply to the
#             watermark before embedding it in a photo of the user.  Rotation is
#             in the range ``0`` to ``360``, where ``0`` is inclusive and
#             ``360`` is exclusive.
#
#         @param scale: scale of the watermark compared to the size of the photo
#             to embed the watermark in.  Scale is in the range ``0.0`` to
#             ``1.0``, both included.  The lower value, the smaller the
#             watermark.  A scale value of ``1.0`` means the watermark covers
#             completely the photo.
#
#
#         @return: an instance containing the following members:
#
#             * ``file_name`` (required): the original local file name as the
#             ``filename`` parameter of the ``Content-Disposition`` header.
#
#             * ``watermark_id`` (required): identification of the watermark as
#               registered to the platform.
#
#             * ``watermark_url`` (required): Uniform Resource Locator (URL) that
#               specifies the location of the watermark's image.  The client
#               application can use this URL and append the query parameter ``size``
#               to specify a given pixel resolution of the photo, such as
#               ``thumbnail``, ``small``, ``medium``, or ``large``.
#
#             * ``update_time`` (required): date and time of the most recent
#               modification of some properties of this watermark.  This information
#               should be stored by the client application to manage its cache of
#               watermarks.
#
#
#         @raise IllegalAccess: if the watermark has been already uploaded by
#             another user.
#
#         @raise InvalidOperation: if the format of the watermark's image is not
#             supported.
#         """
#         return Object.from_json(
#             self.send_request(
#                 http_method=self.HttpMethod.POST,
#                 path='/watermark',
#                 arguments={
#                     'opacity': opacity,
#                     'position': position,
#                     'rotation': rotation,
#                     'scale': scale
#                 },
#                 files=[ file ],
#                 authentication_required=True,
#                 signature_required=True))
