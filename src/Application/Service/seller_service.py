from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller_model import Seller
from src.config.data_base import db

class SellerService:
    @staticmethod
    def create_seller(name, cnpj, email, cellphone, password):
        new_seller = SellerDomain(name,  cnpj, email, cellphone, password)
        seller = Seller(name=new_seller.name,
                        cnpj=new_seller.cnpj,
                        e_mail=new_seller.e_mail,
                        cellphone=new_seller.cellphone,
                        password=new_seller.password)
        
        db.session.add(seller)
        db.session.commit()
        return seller