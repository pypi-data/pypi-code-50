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
from majormode.perseus.model.enum import Enum


# Extended statuses of a heritage at risk report.
ReportObjectStatus = ObjectStatus.extend(
    # The report has been created by a user but not submitted yet for
    # approval by reviewers.
    'draft',

    # The report has been submitted for approval by reviewers, but it is
    # still not accepted or rejected.
    'submitted',

)

# Actions that a reviewer can select related to a heritage at risk
# report submitted by a user.
ReportReviewAction = Enum(
    # The reviewer approves the heritage at risk report submitted by a user.
    'accept',

    # The reviewer has not idea if the heritage at risk report submitted by
    # a user is valid or fake.
    'dunno',

    # The reviewer rejects the heritage at risk report submitted by a user.
    'reject',
)
