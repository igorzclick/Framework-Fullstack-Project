from flask import make_response, jsonify
from src.Application.Service.product_service import ProductService
from src.Domain.product import ProductDomain

class ProductController:
    @staticmethod
    def create_product(body):
        product_domain = ProductDomain(
            name=body.get('name'),
            price=body.get('price'),
            quantity=body.get('quantity'),
            img=body.get('img'),
            status=body.get('status')
        )
        product, error_message = ProductService.create_product(product_domain)

        if error_message:
            return make_response(jsonify({"message": error_message}), 400)
        return make_response(jsonify({
            "message": "Product created successfully",
            "product": product.to_dict()
        }), 201)
    
    @staticmethod
    def get_all_products():
        products = ProductService.get_all_products()
        return make_response(jsonify({
            "products": products
        }), 200)

    @staticmethod
    def get_product_by_id(product_id):
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return make_response(jsonify({"message": "Product not found"}), 404)
        return make_response(jsonify({
            "product": product
        }), 200)
    
    @staticmethod
    def update_product(body, product_id):
        product_domain = ProductDomain(
            name=body.get('name'),
            price=body.get('price'),
            quantity=body.get('quantity'),
            img=body.get('img'),
            status=body.get('status')
        )
        product, error_message = ProductService.update_product(product_id, product_domain)
        if error_message:
            return make_response(jsonify({"message": error_message}), 400)
        if not product:
            return make_response(jsonify({"message": "Product not found or update failed"}), 404)
        return make_response(jsonify({
            "message": "Product updated successfully",
            "product": product.to_dict()
        }), 200)
    
    @staticmethod
    def delete_product(product_id):
        product, message = ProductService.delete_product(product_id)
        if not product:
            return make_response(jsonify({"message": message}), 404)
        return make_response(jsonify({
            "message": message,
        }), 200)
    
    @staticmethod
    def get_product_by_name(name):
        product = ProductService.get_product_by_name(name)
        if not product:
            return make_response(jsonify({"message": "Product not found"}), 404)
        return make_response(jsonify({
            "product": product
        }), 200)
