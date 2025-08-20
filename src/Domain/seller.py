class SellerDomain:
    def __init__(self,nome,cnpj,email,celular,password,status="Inativo"):
        self.nome = nome
        self.cnpj = cnpj
        self.e_mail = email
        self.celular = celular
        self.password = password
        self.status = status
    def to_dict(self):
        return {
            "nome": self.nome,
            "CNPJ": self.cnpj,
            "e_mail": self.e_mail,
            "celular": self.celular,
            "senha": self.password,
            "status": self.status
        }    