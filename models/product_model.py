from entities.product import Product

class ProductModel:
    def __init__(self):
        self.products = []
        self.id_inc=1

    def add_product(self, product): 
        product.id=self.id_inc
        self.id_inc+=1
        self.products.append(product)
        return product

    def get_all_products(self):
        return self.products    
    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product