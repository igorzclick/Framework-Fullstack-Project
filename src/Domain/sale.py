class saleDomain:
    def __init__(self, seller_id, product_id, quantity, price):
        self.seller_id = seller_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        
    def to_dict(self):
        return {
            "seller_id": self.seller_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price": self.price
        }