from flask import make_response, jsonify
from src.Domain.sale import SaleDomain
from src.Application.Service.sale_service import SaleService
from flask_jwt_extended import get_jwt_identity


class SaleController:
    @staticmethod
    def create_sale(body):
        seller_id = get_jwt_identity()

        sale = SaleDomain(
            seller_id=seller_id,
            product_id=body['product_id'],
            quantity=body['quantity'],
            price=0
        )

        created_sale, error_message = SaleService.create_sale(sale)

        if error_message:
            return make_response(jsonify({"message": error_message}), 400)
        
        return make_response(jsonify({
            "message": "Sale created successfully",
            "sale": created_sale.to_dict()
        }), 201)
    
    @staticmethod
    def get_all_sales():
        sales = SaleService.get_all_sales()
        if sales is None:
            return make_response(jsonify({"message": "Could not retrieve sales"}), 500)
        return make_response(jsonify({
            "sales": sales
        }), 200)

    @staticmethod
    def get_sale_by_id(sale_id):
        sale = SaleService.get_sale_by_id(sale_id)
        if not sale:
            return make_response(jsonify({"message": "Sale not found"}), 404)
        return make_response(jsonify({
            "sale": sale
        }), 200)
    
    @staticmethod
    def update_sale(body, sale_id):
        sale_domain = SaleDomain(
            seller_id=body.get('seller_id'),
            product_id=body.get('product_id'),
            quantity=body.get('quantity'),
            price=body.get('price')
        )
        sale, error_message = SaleService.update_sale(sale_id, sale_domain)
        
        if error_message:
            return make_response(jsonify({"message": error_message}), 400)
        
        if not sale:
            return make_response(jsonify({"message": "Sale not found or update failed"}), 404)
        
        return make_response(jsonify({
            "message": "Sale updated successfully",
            "sale": sale.to_dict()
        }), 200)

    @staticmethod
    def delete_sale(sale_id):
        sale, message = SaleService.delete_sale(sale_id)
        if not sale:
            return make_response(jsonify({"message": message}), 404)
        return make_response(jsonify({
            "message": message,
        }), 200)
    