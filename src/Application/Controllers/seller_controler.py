from flask import request,jsonify, make_response
from src.Application.Service.seller_service import SellerService


class SellerController:
    @staticmethod
    def register_seller():
        data = request.get_json()
        nome = data.get('nome')
        cnpj = data.get('CNPJ')
        email = data.get('email')
        celular = data.get('celular')
        password = data.get('password')

        # Validate required fields
        required_fields = ['nome', 'CNPJ', 'email', 'celular', 'password']
        for field in required_fields:
            if not data.get(field):
                return make_response(jsonify({"error": f"{field} is required"}), 400)

        seller = SellerService.create_seller(nome, cnpj, email, celular, password)
        return make_response(jsonify({
            "mensagem": "Seller salvo com sucesso",
            "vendedores": seller.to_dict()
        }), 200)