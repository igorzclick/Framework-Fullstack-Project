from flask import request,jsonify, make_response
from src.Application.Service.seller_service import SellerService


class SellerController:
    @staticmethod
    def register_seller():
        data = request.get_json()
        nome = data.get('nome')
        CNPJ = data.get('CNPJ')
        email = data.get('email')
        celular = data.get('celular')
        password = data.get('password')

        if not nome or not CNPJ or not email or not celular or not password:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        seller = SellerService.create_seller(nome, CNPJ, email, celular, password)
        return make_response(jsonify({
            "mensagem": "Seller salvo com sucesso",
            "vendedores": seller.to_dict()
        }), 200)