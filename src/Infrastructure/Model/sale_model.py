from src.config.data_base import db

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "seller_id": self.seller_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price": self.price,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }