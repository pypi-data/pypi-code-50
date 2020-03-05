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


# Types of orientation of a photo.
Orientation = Enum(
    # The display is wider than it is tall.
    'landscape',

    # The display is taller than it is wide.
    'portrait'
)

# Type of hardware that has generated the image of a photo, either a
# scanner, either a DSLR/smartphone camera.
PhotoProvider = Enum(
    # Define a Digital Single-Lens Reflex (DSLR) camera or a handheld
    # personal computer (smartphone or tablet).
    'camera',

    # Define a device that optically scans photograph printed on paper, such
    # as a flatbed or hand-held scanner,
    'scanner'
)

# Extended status of a photo.
PhotoObjectStatus = ObjectStatus.extend(
    'processing',
    'dmz'
)

# Types of the scene depicted on a photo.  This classification allows
# the platform to determine whether a particular photo could be
# precisely geolocated using a mechanical turk method.  This applies to
# photos of heritage sites.
SceneType = Enum(
    # Any form of life such as plant or living creature, would it be human
    # or any other animal.
    'being',

    # A place of cultural, historical, or natural significance for a group
    # or society.
    'heritage',

    # Any other type of image that doesn't represent a photograph, such as
    # painting, illustration, etc.
    'other',

    # Any form of landscapes that show little or no human activity and are
    # created in the pursuit of a pure, unsullied depiction of nature, also
    # known as scenery.
    'scenery',
)
