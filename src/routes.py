from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.seller_controller import SellerController
from flask import jsonify, make_response, request
from src.Application.Dto.seller_dto import SellerRegisterSchema, sellers_schema, seller_schema
from src.Application.Service.seller_service import seller_service

def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    @app.route('/seller', methods=['POST'])
    def register_seller():
        data = request.get_json()
        errors = SellerRegisterSchema().validate(data)
        if errors:
            return jsonify(errors), 400
        return SellerController.register_seller(data), 200

    @app.route("/seller", methods=['GET'])
    def list_all():
        seller = seller_service.get_all_sellers()
        result = sellers_schema.dump(seller) # faz virar lista
        return jsonify(result)
    
    @app.route("/seller/<int:seller_id>", methods=['GET'])
    def get_seller_by_id(seller_id):
        seller = seller_service.get_seller_by_id(seller_id)
        if not seller:
            return jsonify({"message": "Seller not found"}), 404
        return jsonify(seller_schema.dump(seller)), 200
    
    @app.route("/seller/<int:seller_id>", methods=['PUT'])
    def update_seller(seller_id):
        data = request.get_json()
        seller = seller_service.update_seller(seller_id, data['name'], data['cnpj'], data['email'], data['cellphone'], data['password'])
        if not seller:
            return jsonify({"message": "Seller not found"}), 404
        return jsonify(seller_schema.dump(seller)), 200
    
    @app.route("/seller/<int:seller_id>", methods=['DELETE'])
    def delete_seller(seller_id):
        seller = seller_service.delete_seller(seller_id)
        if not seller:
            return jsonify({"message": "Seller not found"}), 404 
        return jsonify(seller_schema.dump(seller)), 200
