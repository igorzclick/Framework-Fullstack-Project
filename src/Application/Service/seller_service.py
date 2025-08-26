from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller_model import Seller
from src.config.data_base import db

class SellerService:
    @staticmethod
    def create_seller(name, cnpj, email, cellphone, password):
      try:  
        new_seller = SellerDomain(name,  cnpj, email, cellphone, password)
        seller = Seller(name=new_seller.name,
                        cnpj=new_seller.cnpj,
                        e_mail=new_seller.e_mail,
                        cellphone=new_seller.cellphone,
                        password=new_seller.password)
        
        db.session.add(seller)
        db.session.commit()
        db.session.refresh(seller)
        return jsonify(seller.to_dict()), seller
      except SQLAlchemyError as e:
        return {
            "message": "Error creating seller",
            "error": str(e)
        }

    def get_seller_by_id(seller_id):
        return Seller.query.get(seller_id)
    
    def get_Sellers():
    try:  
        return Seller.query.all()
    except SQLAlchemyError as e:
        return {
            "message": "Error finding sellers",
            "error": str(e)
        }
    def update_seller(seller_id, name, cnpj, email, cellphone, password):
     try:
        seller = Seller.query.get(seller_id)
        seller.name = name
        seller.cnpj = cnpj
        seller.e_mail = email
        seller.cellphone = cellphone
        seller.password = password
        db.session.commit()
        return {
            "message": "Seller updated successfully",
            "seller": seller.to_dict()
        }, 200
     except SQLAlchemyError as e:
         db.session.rollback()
        return {
            "message": "Error updating seller",
            "error": str(e) 
        }
        
        return seller
    
    def delete_seller(seller_id):
       try: 
        seller = Seller.query.get(seller_id)
        db.session.delete(seller)
        db.session.commit()
        return seller
       except SQLAlchemyError as e:
           db.session.rollback()
           return {
               "message": "Error deleting seller",
               "error": str(e)
           } 
    