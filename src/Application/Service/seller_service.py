from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller_model import Seller
from src.config.data_base import db

class SellerService:
    @staticmethod
    def create_seller(nome, CNPJ, email, celular, password):
        new_seller = SellerDomain(nome, CNPJ, email, celular, password)
        seller = Seller(nome=new_seller.nome,
                        CNPJ=new_seller.CNPJ,
                        e_mail=new_seller.e_mail,
                        celular=new_seller.celular,
                        senha=new_seller.senha)
        db.session.add(seller)
        db.session.commit()
        return seller