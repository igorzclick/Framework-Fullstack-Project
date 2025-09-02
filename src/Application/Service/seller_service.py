from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller_model import Seller
from src.config.data_base import db

class SellerService:
    @staticmethod
    def create_seller(name, cnpj, email, cellphone, password):
        try:
            new_seller = SellerDomain(name, cnpj, email, cellphone, password)

            if Seller.query.filter_by(email=new_seller.email).first():
                return None, "Email já cadastrado"
            if Seller.query.filter_by(cnpj=new_seller.cnpj).first():
                return None, "CNPJ já cadastrado"
            
            seller = Seller(
                name=new_seller.name,
                cnpj=new_seller.cnpj,
                email=new_seller.email,
                cellphone=new_seller.cellphone,
                password=new_seller.password
            )

            db.session.add(seller)
            db.session.commit()
            return seller, None
        except Exception as e:
            db.session.rollback()
            return None, str(e)
    
    @staticmethod
    def get_all_sellers():
        try:
            sellers = Seller.query.all()        
            return [seller.to_dict() for seller in sellers]
        except Exception as e:
            return None
            
    @staticmethod
    def get_seller_by_id(id):
        try:
            seller = Seller.query.filter_by(id=id).first()        
            return seller.to_dict()
        except Exception as e:
            return None
        
    @staticmethod
    def update_seller(id, name, cnpj, email, cellphone, password):
        try:
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
        except Exception as e:
            return None
         
    @staticmethod
    def delete_seller(seller_id):
        try:
            seller = Seller.query.filter_by(id=seller_id).first()
            if not seller:
                return None
            db.session.delete(seller)
            db.session.commit()
            return seller
        except Exception as e:
            return None
