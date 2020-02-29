from pvlv_commando.replyes.permissions_replies import (
    insufficient_permissions,
)


class InsufficientPermissions(Exception):
    def __init__(self, language):

        self.language = language

    def __str__(self):
        return insufficient_permissions(self.language)
