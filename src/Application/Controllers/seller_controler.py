from flask import request, jsonify, make_response
from src.Application.Service.seller_service import SellerService

class SellerController:
    @staticmethod
    def register_seller(body):
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