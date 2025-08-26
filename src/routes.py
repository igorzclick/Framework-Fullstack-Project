from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.seller_controler import SellerController
from src.Application.Service.seller_service import SellerService
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
    
    @app.route('/seller/create', methods=['POST'])
    @app.input(SellerRegisterSchema, location='json')
    def create_seller(body):
        return SellerController.create_seller(body)
    @app.route('/seller/update/<int:seller_id>', methods=['PUT'])
    def update_seller(seller_id):
        return SellerController.update_seller(seller_id)
    @app.route('/seller/get_by_id/<int:seller_id>', methods=['GET'])
    def get_seller_by_id(seller_id):
        return SellerController.get_seller_by_id(seller_id)
    
    @app.route('/seller/get_all', methods=['GET'])   
    def get_sellers():
        return SellerController.get_sellers()
    
    @app.route('/seller/delete/<int:seller_id>', methods=['DELETE'])
    def delete_seller(seller_id):
        return SellerController.delete_seller(seller_id)
    
    
    

