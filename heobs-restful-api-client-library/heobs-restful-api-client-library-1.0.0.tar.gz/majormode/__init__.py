# Copyright (C) 2015 Majormode.  All rights reserved.
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

# The package "majormode.*" can be also defined for any other projects
# that used this platform library installed as an "egg" bundle.  The
# Python package extension utility "pkgutil", and its function
# "extend_path" makes sure Python is aware there is more than one sub-
# package within a package, physically located elsewhere and the
# interpreter then does not stop searching after it fails to find a
# module under the first package path it encounters in "sys.path", but
# searches all paths in "__path__".
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
