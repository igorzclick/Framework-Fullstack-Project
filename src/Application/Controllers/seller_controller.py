from flask import jsonify, make_response
from src.Application.Service.seller_service import SellerService

class SellerController:
    @staticmethod
    def register_seller(body):
        seller, error_message = SellerService.create_seller(
            body['name'],
            body['cnpj'],
            body['email'],
            body['cellphone'],
            body['password']
        )

        if error_message:
            return make_response(jsonify({"message": error_message}), 400)
        
        return make_response(jsonify({
            "message": "Seller registered successfully",
            "seller": seller.to_dict()
        }), 201)
    
    @staticmethod
    def get_all_sellers():
        sellers = SellerService.get_all_sellers()
        if sellers is None:
            return make_response(jsonify({"message": "Could not retrieve sellers"}), 500)
        return make_response(jsonify({
            "sellers": sellers
        }), 200)
    
    @staticmethod
    def get_seller_by_id(seller_id):
        seller = SellerService.get_seller_by_id(seller_id)
        if not seller:
             return make_response(jsonify({"message": "Seller not found"}), 404)
        return make_response(jsonify({
            "seller": seller
        }), 200)

    @staticmethod
    def update_seller(body, seller_id):
        seller, error_message = SellerService.update_seller(
            seller_id,
            body.get('name'),
            body.get('cnpj'),
            body.get('email'),
            body.get('cellphone'),
            body.get('password')
        )

        if error_message:
            return make_response(jsonify({"message": error_message}), 400)
        
        if not seller:
            return make_response(jsonify({"message": "Seller not found or update failed"}), 404)

        return make_response(jsonify({
            "message": "Seller updated successfully",
            "seller": seller.to_dict()
        }), 200)
    
    @staticmethod
    def delete_seller(seller_id):
        seller = SellerService.delete_seller(seller_id)
        if not seller:
            return make_response(jsonify({"message": "Seller not found"}), 404)
            
        return make_response(jsonify({
            "message": "Seller deleted successfully",
        }), 200)
