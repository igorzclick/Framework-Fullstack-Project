from src.Application.Controllers.seller_controller import SellerController
from src.Application.Controllers.user_controller import UserController
from flask import jsonify, make_response, request
from src.Application.Dto.seller_dto import SellerRegisterSchema


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
            return make_response(jsonify(errors), 400)
        return SellerController.register_seller(data)

    @app.route("/seller", methods=['GET'])
    def get_all_sellers():
        return SellerController.get_all_sellers()
 
    @app.route("/seller/<int:seller_id>", methods=['GET'])
    def get_seller_by_id(seller_id):
        return SellerController.get_seller_by_id(seller_id)
    
    @app.route("/seller/<int:seller_id>", methods=['PUT'])
    def update_seller(seller_id):
        data = request.get_json()
        return SellerController.update_seller(data, seller_id)
    
    @app.route("/seller/<int:seller_id>", methods=['DELETE'])
    def delete_seller(seller_id):
        return SellerController.delete_seller(seller_id)