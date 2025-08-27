class SellerDomain:
    def __init__(self,name,cnpj,email,cellphone,password,status="Inativo"):
        self.name = name
        self.cnpj = cnpj
        self.e_mail = email
        self.cellphone = cellphone
        self.password = password
        self.status = status
        
    def to_dict(self):
        return {
            "name": self.name,
            "cnpj": self.cnpj,
            "e_mail": self.e_mail,
            "cellphone": self.cellphone,
            "password": self.password,
            "status": self.status
        }    