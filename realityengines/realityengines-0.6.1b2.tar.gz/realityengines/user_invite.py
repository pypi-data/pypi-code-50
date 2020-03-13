from .user import User
from .organization import Organization


class UserInvite():
    '''

    '''

    def __init__(self, client, userInviteId=None, email=None, acceptedAt=None, createdAt=None, organization=[], user=[]):
        self.client = client
        self.id = userInviteId
        self.user_invite_id = userInviteId
        self.email = email
        self.accepted_at = acceptedAt
        self.created_at = createdAt
        self.organization = client._build_class(Organization, organization)
        self.user = client._build_class(User, user)

    def __repr__(self):
        return f"UserInvite(user_invite_id={repr(self.user_invite_id)}, email={repr(self.email)}, accepted_at={repr(self.accepted_at)}, created_at={repr(self.created_at)}, organization={repr(self.organization)}, user={repr(self.user)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'user_invite_id': self.user_invite_id, 'email': self.email, 'accepted_at': self.accepted_at, 'created_at': self.created_at, 'organization': self.organization.to_dict() if self.organization else None, 'user': self.user.to_dict() if self.user else None}

    def delete_invite(self):
        return self.client.delete_invite(self.user_invite_id)
