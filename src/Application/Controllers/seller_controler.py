from flask import request, jsonify, make_response
from src.Application.Service.seller_service import SellerService
from src.Application.Service.seller_service import SellerService

class SellerController:
    @staticmethod
    def create_seller(body):
       try: 
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
        except Exception as e:
            return make_response(jsonify({
                "message": "Error registering seller",
                "error": str(e)
            }), 500)
        
    @staticmethod
    def delete_seller(seller_id):
        try:
            seller = SellerService.delete_seller(seller_id)
            return make_response(jsonify({
                "message": "Seller deleted successfully",
                "seller": seller.to_dict()
            }), 200)
        except Exception as e:
            return make_response(jsonify({
                "message": "Error deleting seller",
                "error": str(e)
            }), 500)
            
    @staticmethod
    def update_seller(seller_id):
        try:
            seller = SellerService.update_seller(
                seller_id,
                request.json['name'],
                request.json['cnpj'],
                request.json['email'],
                request.json['cellphone'],
                request.json['password']
            )
            return make_response(jsonify({
                "message": "Seller updated successfully",
                "seller": seller.to_dict()
            }), 200)
        except Exception as e:
            return make_response(jsonify({
                "message": "Error updating seller",
                "error": str(e)
            })
        )        
        
    @staticmethod
    def get_seller_by_id(seller_id):
        try:
            seller=SellerService.get_seller_by_id(seller_id)
            return make_responde(jsonify({
                "message": "seller found successfully",
                "seller": seller.to_dict()
                }),200)    
            
        except Exception as e:
            return make_response(jsonify({
                "message": "Error finding seller",
                "error": str(e)
            }))
    @staticmethod
    def get_sellers():
        try:
            sellers=SellerService.get_Sellers()
            return make_responde(jsonify({
                "message": "sellers found successfully",
                "sellers": [seller.to_dict() for seller in sellers]
                }),200)    
            
        except Exception as e:
            return make_response(jsonify({
                "message": "Error finding sellers",
                "error": str(e)
            }))    
            
            
    @staticmethod
    def activate_seller(seller_id):
        pass
        
            