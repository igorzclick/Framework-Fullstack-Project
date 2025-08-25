from flask import request, jsonify, make_response
from src.Application.Service.seller_service import SellerService
from apiflask import Schema
from apiflask.fields import String, Email
from apiflask.validators import Length

class SellerRegisterSchema(Schema):
    name = String(required=True, validate=Length(1))
    cnpj = String(required=True, validate=Length(equal=14))  # Ajuste se quiser permitir formatação
    email = Email(required=True)
    cellphone = String(required=True, validate=Length(min=10))
    password = String(required=True, validate=Length(min=6))

class SellerController:
    @staticmethod
    def register_seller(body: SellerRegisterSchema):

        seller = SellerService.create_seller(
            body['name'],
            body['cnpj'],
            body['email'],
            body['cellphone'],
            body['password']
        )
        return make_response(jsonify({
            "message": "Seller registered successfully",
            "seller": seller.to_dict()
        }), 200)