from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.seller_controler import SellerController
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
    @app.input(SellerRegisterSchema, location='json')
    def register_seller(body):
        return SellerController.register_seller(body)
    

