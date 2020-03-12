"""
Preset data for creation of user permissions and dynamic details.
"""
from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class UserPresets(AutoName):
    ALL_FALSE = auto()
    SITE_ADMIN = auto()
    # PLANT_USER_STD = auto()
    # CONTRACTOR_STD = auto()
    # CONTRACTOR_SUPERVISOR = auto()


user_perm_presets = {
    UserPresets.ALL_FALSE: {
        "approved": False,
        "companyID": None,
        "managementSubscriptions": {
            "newTaskCreated": False,
            "allTaskStatusChanged": False,
            "taskDeleted": False,
            "craftRecordDeleted": False,
            "scaffolds": False,
        },
        "permissions": {
            "getsNewTaskNotifications": False,
            "canEditContractorDetails": False,
            "canCreateTasks": False,
            "canUpdateTasks": False,
            "canDeleteTasks": False,
            "canCreateCraftRecords": False,
            "canUpdateCraftRecords": False,
            "canDeleteCraftRecords": False,
            "isPlantPersonnel": False,
            "isSiteAdmin": False,
        },
    },
    UserPresets.SITE_ADMIN: {
        "approved": True,
        "companyID": None,
        "managementSubscriptions": {
            "newTaskCreated": False,
            "allTaskStatusChanged": False,
            "taskDeleted": False,
            "craftRecordDeleted": False,
            "scaffolds": False,
        },
        "permissions": {
            "getsNewTaskNotifications": True,
            "canEditContractorDetails": True,
            "canCreateTasks": True,
            "canUpdateTasks": True,
            "canDeleteTasks": True,
            "canCreateCraftRecords": True,
            "canUpdateCraftRecords": True,
            "canDeleteCraftRecords": True,
            "isPlantPersonnel": True,
            "isSiteAdmin": True,
        },
    },
}
