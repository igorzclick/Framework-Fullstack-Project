from src.config.data_base import db
class Seller(db.model):
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    CNPJ= db.Column(db.String(14), unique=True, nullable=False)
    e_mail = db.Column(db.String(100), unique=True, nullable=False)
    celular = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "CNPJ": self.CNPJ,
            "e_mail": self.e_mail,
            "celular": self.celular,
            "senha": self.senha
        }