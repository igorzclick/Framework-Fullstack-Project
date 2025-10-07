from src.Infrastructure.Model.product_model import Product
from src.config.data_base import db
from src.Domain.product import ProductDomain

class ProductService:
    @staticmethod
    def create_product(product):
        try:
            if Product.query.filter_by(name=product.name).first():
                return None, "Product already exists"
                    
            product = Product(
                name=product.name,
                price=product.price,
                quantity=product.quantity,
                img=product.img,
                status=product.status
            )

            db.session.add(product)
            db.session.commit()
            return product, None
        except Exception as e:
            db.session.rollback()
            return None, str(e)
        
    @staticmethod
    def get_all_products():
        try:
            products = Product.query.all()
            return [product.to_dict() for product in products]
        except Exception as e:
            return None
        
    @staticmethod
    def get_product_by_id(product_id):
        try:
            product = Product.query.filter_by(id=product_id).first()
            return product.to_dict()
        except Exception as e:
            return None
        
    @staticmethod
    def update_product(product_id, product):
        try:
            product = Product.query.filter_by(id=product_id).first()
            
            product_by_name = Product.query.filter_by(name=product.name).first()
            if product_by_name != None and product_by_name.id != product.id:
                return None, "Product already exists"

            if not product:
                return None, "Product not found"    
            
            product.name = product.name
            product.price = product.price
            product.quantity = product.quantity
            product.img = product.img
            product.status = product.status

            db.session.commit()
            return product, None
        except Exception as e:
            db.session.rollback()
            return None, str(e)
        
    @staticmethod
    def delete_product(product_id):
        try:
            product = Product.query.filter_by(id=product_id).first()
            if not product:
                return None, "Product not found"
            db.session.delete(product)
            db.session.commit()
            return True, "Product deleted successfully"
        except Exception as e:
            return None
        
    @staticmethod
    def get_product_by_name(name):
        try:
            product = Product.query.filter_by(name=name).first()
            return product.to_dict()
        except Exception as e:
            return None
    