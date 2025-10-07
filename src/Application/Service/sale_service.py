from src.Infrastructure.Model.sale_model import Sale
from src.config.data_base import db

class SaleService:
    @staticmethod
    def create_sale(sale):
        sale = Sale(
            seller_id=sale.seller_id,
            product_id=sale.product_id,
            quantity=sale.quantity,
            price=sale.price
        )
        db.session.add(sale)
        db.session.commit()
        return sale

    @staticmethod
    def get_all_sales():
        try:
            sales = Sale.query.all()
            return [sale.to_dict() for sale in sales]
        except Exception as e:
            return None
        
    @staticmethod
    def get_sale_by_id(sale_id):
        try:
            sale = Sale.query.filter_by(id=sale_id).first()
            return sale.to_dict()
        except Exception as e:
            return None
        
    @staticmethod
    def update_sale(sale_id, sale):
        try:
            sale = Sale.query.filter_by(id=sale_id).first()
            if not sale:
                return None, "Sale not found"

            sale.seller_id = sale.seller_id
            sale.product_id = sale.product_id
            sale.quantity = sale.quantity
            sale.price = sale.price

            db.session.commit()
            return sale

        except Exception as e:
            return None

    @staticmethod
    def delete_sale(sale_id):
        try:
            sale = Sale.query.filter_by(id=sale_id).first()
            if not sale:
                return None, "Sale not found"

            db.session.delete(sale)
            db.session.commit()
            return True, "Sale deleted successfully"
        except Exception as e:
            return None

    @staticmethod
    def get_sale_by_seller_id(seller_id):
        try:
            sales = Sale.query.filter_by(seller_id=seller_id).all()
            return [sale.to_dict() for sale in sales]
        except Exception as e:
            return None
        
    @staticmethod
    def get_sale_by_product_id(product_id):
        try:
            sales = Sale.query.filter_by(product_id=product_id).all()
            return [sale.to_dict() for sale in sales]
        except Exception as e:
            return None