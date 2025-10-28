from src.Infrastructure.Model.sale_model import Sale
from src.Infrastructure.Model.product_model import Product
from src.config.data_base import db

class SaleService:
    @staticmethod
    def create_sale(sale):
        try:
            product = Product.query.filter_by(id=sale.product_id).first()
            if not product:
                return None, "Product not found"
            
            if product.quantity <= sale.quantity:
                return None, f"Insufficient quantity. Available: {product.quantity}, Requested: {sale.quantity}"
            
            product.quantity -= sale.quantity
            
            if product.quantity == 0:
                product.status = "Inativo"
            
            new_sale = Sale(
                seller_id=sale.seller_id,
                product_id=sale.product_id,
                quantity=sale.quantity,
                price=sale.price
            )
            
            db.session.add(new_sale)
            db.session.commit()
            return new_sale, None
            
        except Exception as e:
            db.session.rollback()
            return None, str(e)

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
    def update_sale(sale_id, sale_domain):
        sale = Sale.query.get(sale_id)
        if not sale:
            return None, "Sale not found"

        try:
            sale.product_id = sale_domain.product_id
            sale.quantity = sale_domain.quantity
            sale.price = sale_domain.price

            db.session.commit()
            return sale, None 
        except Exception as e:
            db.session.rollback()
            return None, str(e)

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
            db.session.rollback()
            return None