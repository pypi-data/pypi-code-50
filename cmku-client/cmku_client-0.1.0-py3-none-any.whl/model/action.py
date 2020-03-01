from marshmallow import Schema
from marshmallow.fields import Str, Integer, DateTime, Nested, List
from marshmallow import EXCLUDE, pre_load, post_load

from ..lib.declass import DeClass


class ActionTypeSchema(Schema):
    id = Integer()
    name = Str()
    code = Str()
    description = Str()

    @post_load
    def make_type(self, data, **kwargs):
        return DeClass(_name="ActionType", _resp=("id", "name"), **data)


class OrganizerSchema(Schema):
    """
    Schema for action organizer info
    """
    class Meta:
        unknown = EXCLUDE

    club_id = Integer(data_key="organizerClub")
    email = Str(data_key="contactMail")
    phone = List(Str(), data_key="contactPhone")
    web = Str(data_key="contactWeb")

    @pre_load
    def load_phone(self, in_data, **kwargs):
        if "contactPhone" not in in_data:
            return in_data
        if "," not in in_data["contactPhone"]:
            in_data["contactPhone"] = (in_data["contactPhone"])
        elif "," in in_data["contactPhone"]:
            in_data["contactPhone"] = [phone.strip() for phone in in_data["contactPhone"].split(",")]
        return in_data

    @post_load
    def make_action(self, data, **kwargs):
        return DeClass(_name="Organizer", _resp=("email", "web"), **data)


class ActionDetailGeneralSchema(Schema):
    """
    General schema for action detail
    """
    class Meta:
        unknown = EXCLUDE

    id = Integer(data_key="id")
    name = Str(data_key="name")
    place = Str(data_key="place")
    deadlines = List(DateTime(data_key="deadlines"))
    organizer = Nested(OrganizerSchema)
    days = List(Str(data_key="exhibitionDays"))
    web = Str(data_key="web")
    type = Integer(data_key="type")

    @pre_load
    def load_organizer(self, in_data, **kwargs):
        in_data["organizer"] = in_data
        return in_data

    @post_load
    def make_action(self, data, **kwargs):
        return DeClass(_name="ActionDetail", _resp=("id", "name"), **data)


class ActionListGeneralSchema(Schema):
    """
    General schema for list item of actoins
    """
    class Meta:
        unknown = EXCLUDE

    id = Integer()
    name = Str()
    place = Str()
    date_from = DateTime(data_key="start")
    date_to = DateTime(data_key="end")
    organizer = Str()
    web = Str()
    type = Str()

    @post_load
    def make_action(self, data, **kwargs):
        return DeClass(_name="ActionListItem", _resp=("id", "name"), **data)