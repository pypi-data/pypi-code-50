from mongoengine import StringField, DictField, ReferenceField,\
    DateTimeField, Document


class Role(Document):
    name = StringField(required=True, unique=True)
    permissions = DictField(required=False)


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = ReferenceField(
        Role,
        dbref=True,
        required=True
    )


class WhitelistToken(Document):
    token = StringField(required=True, unique=True)
    created_at = DateTimeField()
