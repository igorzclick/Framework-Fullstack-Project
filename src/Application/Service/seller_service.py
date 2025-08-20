from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller_model import Seller
from src.config.data_base import db

class SellerService:
    @staticmethod
    def create_seller(nome, cnpj, email, celular, password):
        new_seller = SellerDomain(nome,  cnpj, email, celular, password)
        seller = Seller(nome=new_seller.nome,
                        CNPJ=new_seller.cnpj,
                        e_mail=new_seller.e_mail,
                        celular=new_seller.celular,
                        senha=new_seller.senha)
        db.session.add(seller)
        db.session.commit()
        return seller