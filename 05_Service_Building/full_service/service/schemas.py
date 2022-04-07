from marshmallow import Schema, fields


class RequestSchema(Schema):
    text = fields.String(required=True)


class ResponseSchema(Schema):
    prediction = fields.String()
    score = fields.Number()
