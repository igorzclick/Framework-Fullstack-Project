from copy import error
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

        if error:
            return make_response(jsonify({"message": error}), 400)
        
        return make_response(jsonify({
            "message": "Seller registered successfully",
            "seller": seller.to_dict()
        }), 201)
    
    @staticmethod
    def get_all_sellers():
        sellers = SellerService.get_all_sellers()
        return make_response(jsonify({
            "sellers": sellers
        }), 200)
    
    @staticmethod
    def get_seller_by_id(seller_id):
        seller = SellerService.get_seller_by_id(seller_id)
        return make_response(jsonify({
            "seller": seller.to_dict()
        }), 200)

    @staticmethod
    def update_seller(body):
        seller = SellerService.update_seller(
            body['id'],
            body['name'],
            body['cnpj'],
            body['email'],
            body['cellphone'],
            body['password']
        )
        return make_response(jsonify({
            "message": "Seller updated successfully",
            "seller": seller.to_dict()
        }), 200)
    
    @staticmethod
    def delete_seller(seller_id):
        seller = SellerService.delete_seller(seller_id)
        return make_response(jsonify({
            "message": "Seller deleted successfully",
            "seller": seller.to_dict()
        }), 200)
    
seller_controller = SellerService()