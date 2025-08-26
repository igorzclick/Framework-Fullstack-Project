#verificações de autenticação de tipo de dados(c é string, c tem x qtd de caracter etc)
from apiflask import Schema, HTTPBasicAuth 
from apiflask.fields import String, Email
from apiflask.validators import Length
# from seller_model import Seller
# from SellerDomain  import SellerDomain



# auth = HTTPBasicAuth()

class SellerRegisterSchema(Schema):
    name = String(required=True, validate=Length(1))
    cnpj = String(required=True, validate=Length(equal=14))  # Ajuste se quiser permitir formatação
    email = Email(required=True)
    cellphone = String(required=True, validate=Length(min=10))
    password = String(required=True, validate=Length(min=6))
    

    
        
    