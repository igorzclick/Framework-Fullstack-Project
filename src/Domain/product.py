class productDomain:
    def __init__(self, name, price, quantity, img, status="Inativo"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
        self.img = img
        
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "status": self.status,
            "img": self.img
        }