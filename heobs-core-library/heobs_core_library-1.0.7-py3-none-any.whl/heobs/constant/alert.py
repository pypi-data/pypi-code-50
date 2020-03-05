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


AlertFrequency = Enum(
    # Indicate that the user wants to receive alerts as soon as they
    # happen.  This is the default option.
    'immediate',

    # Indicate that the user wants to receive alerts at most once a day.
    'daily',

    # Indicate that the user wants to receive alerts at most once a week.
    'weekly'
)
