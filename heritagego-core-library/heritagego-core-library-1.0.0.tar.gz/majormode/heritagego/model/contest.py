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

from majormode.perseus.model.enum import Enum


ContestPhotoRejectionReason = Enum(
    # The photo of the user doesn't allow to precisely identify the
    # location where the photo has been taken: the photo may be blurred,
    # the focal or the direction the camera was pointing at might be
    # inappropriate.
    'unrecognizable_location',

    # The photo has been taken in a location other than the required one.
    'wrong_location',

    # The content of the photo is inappropriate, which may be sexually
    # explicit, violent, prohibited, or even illegal.
    'inappropriate_content'
)


IdentityDocumentRejectReason = Enum(
    # The identity document is not readable: the scan may be blurred or its
    # resolution too small.
    'unreadable_document',

    # The document uploaded by the user doesn't correspond to a identity
    # document.
    'wrong_document_type',

    # The identification number of the identity document uploaded by the
    # user and the identitication number entered by the user don't match
    'unmatched_identifications'
)
