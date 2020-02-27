from marshmallow import Schema, fields


class ConcentratorSchema(Schema):
    id = fields.Int()
    number = fields.Str()
    name = fields.Str(attribute="name")
    ip_address = fields.Str(attribute="ip_address")
    model = fields.Str(attribute="model")
    type = fields.Str(attribute="type")
    dc_address = fields.Str(attribute="dc_ws_address")
    ws_ip = fields.Str(attribute="stg_ws_ip_address")
    ws_pass = fields.Str(attribute="stg_ws_password")


class RegisterSchema(Schema):
    id = fields.Int()
    number = fields.Str()
    name = fields.Str(attribute="name")
    tg_name = fields.Str(attribute="name")
    cnc = fields.Nested(ConcentratorSchema, attribute="cnc_id")
