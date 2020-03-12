from yolapy.services import Yola


class User(object):
    """Yola User - a service model that uses the yola client for persistence.

    Example use:
    ```
    from yolapy.models import User as YolaUser

    yola_user = YolaUser(
        email='test@example.com',
        name='Jane',
        surname='Doe',
        partner_id='WL_PARTNER',
        preferences={'locale': 'en'})

    yola_user.save()
    ```
    """

    _client = None
    _fields = ('active', 'deleted', 'email', 'id', 'name', 'partner_id',
               'preferences', 'signup_date', 'surname')

    def __init__(self, **kwargs):
        """Construct a Yola User.

        The data in a User instance does not persist until it has been saved.


        :param active: Bool, toggled ``False`` when user is deactivated
        :param deleted: Timestamp, date the user was deleted
        :param email: Str, user's email address
        :param id: Str, user's 32 character ID
        :param name: Str, user's first name
        :param partner_id: Str, yola partner responsible the user
        :param preferences: Dict, user's preferences
        :param signup_date: Timestamp, date the user signed up
        :param surname: Str, user's second name

        :return: :class:`User <User>` object
        :rtype: yolapy.users.models.User

        """

        for field_name in self._fields:
            setattr(self, field_name, kwargs.get(field_name))

        self.partner_id = self.partner_id or self.get_client().username
        self.active = self.active or False
        self.preferences = self.preferences or {}

    @classmethod
    def get_client(cls):
        if not cls._client:
            cls._client = Yola()
        return cls._client

    @classmethod
    def get(cls, user_id):
        """Get a user from the Yola API."""
        user_attributes = cls.get_client().get_user(user_id)
        return cls(**user_attributes)

    @classmethod
    def create(cls, **kwargs):
        user = cls.get_client().create_user(**kwargs)
        return cls(**user)

    def update(self, **attributes):
        """Update all keyword arguments to update instance attributes."""
        for attr, val in attributes.items():
            setattr(self, attr, val)
