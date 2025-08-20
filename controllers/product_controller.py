from flask import Blueprint, request, jsonify
from Service.product_service import ProductService

product = Blueprint('product', __name__)
service = ProductService()

@product.route('/products', methods=['POST'])
def create():
    data = request.get_json()
    return service.create(data['name'], data['price'], data['description'])