"""Checks view access for Permissions"""


# pylint: disable=too-few-public-methods
class CheckAcess:
    """
    Checks the permissions for Request.
    """
    def __init__(self, request, permissions):
        self.request = request
        self.permissions = permissions

    def have_view_access(self):
        """
        Checks if any of the permission is true for request.
        """
        method_based = tuple(filter(
            lambda x: x[0] == 'method',
            self.permissions
        ))
        class_based = tuple(filter(
            lambda x: x[0] == 'class',
            self.permissions
        ))
        attr_based = tuple(filter(
            lambda x: x[0] == 'attr',
            self.permissions
        ))

        if any(
                p[1](self.request) for p in method_based
        ):
            return True
        if any(
                p[1](self.request)() for p in class_based
        ):
            return True
        if any(
                p[2] == getattr(self.request.user, p[1]) for p in attr_based
        ):
            return True
        return False
