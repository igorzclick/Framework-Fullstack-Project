from models.product_model import ProductModel

class ProductService:
    def __init__(self):
        self.products = ProductModel()

    def create(self, name, price, description):
        return self.products.add_product(name, price, description).to_dict()