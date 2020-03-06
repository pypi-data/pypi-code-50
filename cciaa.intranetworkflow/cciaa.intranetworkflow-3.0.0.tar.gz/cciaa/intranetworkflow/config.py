# -*- coding: utf-8 -*-

from Products.CMFCore.permissions import setDefaultRoles
from AccessControl import ModuleSecurityInfo

security = ModuleSecurityInfo("cciaa.intranetworkflow.config")

PROJECTNAME = 'cciaa.intranetworkflow'

REVIEW_LEV1 = 'CamCom: Approvazione livello 1'
REVIEW_LEV2 = 'CamCom: Approvazione livello 2'

try:
    from customize import CCIAA_ROLES_GLOBALLY_ASSIGNABLE
except ImportError:
    CCIAA_ROLES_GLOBALLY_ASSIGNABLE = False

setDefaultRoles(REVIEW_LEV1, ('Manager',))
setDefaultRoles(REVIEW_LEV2, ('Manager',))
