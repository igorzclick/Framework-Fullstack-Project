from apiflask import Schema
from apiflask.fields import String, Email
from apiflask.validators import Length

class SellerRegisterSchema(Schema):
    name = String(required=True, validate=Length(1))
    cnpj = String(required=True, validate=Length(equal=14))  # Ajuste se quiser permitir formatação
    email = Email(required=True)
    cellphone = String(required=True, validate=Length(min=10))
    password = String(required=True, validate=Length(min=6))

seller_schema = SellerRegisterSchema()
sellers_schema = SellerRegisterSchema(many=True)