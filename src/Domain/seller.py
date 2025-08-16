class SellerDomain:
    def __init__(self,nome,CNPJ,email,celular,senha,status="Inativo"):
        self.nome = nome
        self.CNPJ = CNPJ
        self.e_mail = email
        self.celular = celular
        self.senha = senha
        self.status = status
    def to_dict(self):
        return {
            "nome": self.nome,
            "CNPJ": self.CNPJ,
            "e_mail": self.e_mail,
            "celular": self.celular,
            "senha": self.senha,
            "status": self.status
        }    