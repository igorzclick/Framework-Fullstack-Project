from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller_model import Seller
from src.config.data_base import db

class SellerService:
    @staticmethod
    def create_seller(name, cnpj, email, cellphone, password):
        new_seller = SellerDomain(name,  cnpj, email, cellphone, password)
        seller = Seller(name=new_seller.name,
                        cnpj=new_seller.cnpj,
                        email=new_seller.email,
                        cellphone=new_seller.cellphone,
                        password=new_seller.password)
        
        db.session.add(seller)
        db.session.commit()
        return seller
    
    @staticmethod
    def get_all_sellers():
        return Seller.query.all()
    
    @staticmethod
    def get_seller_by_id(id):
        return Seller.query.filter_by(id=id).first()
    
    @staticmethod
    def update_seller(id, name, cnpj, email, cellphone, password):
        seller = Seller.query.filter_by(id=id).first()
        if not seller:
            return None
        seller.name = name
        seller.cnpj = cnpj
        seller.email = email
        seller.cellphone = cellphone
        seller.password = password
        db.session.commit()
        return seller
    
    @staticmethod
    def delete_seller(seller_id):
        seller = Seller.query.filter_by(id=seller_id).first()
        if not seller:
            return None
        db.session.delete(seller)
        db.session.commit()
        return seller
    
seller_service = SellerService()