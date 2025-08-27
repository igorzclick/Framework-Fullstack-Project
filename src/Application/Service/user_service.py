from src.Domain.user import UserDomain
# from src import user
from src.config.data_base import db 

class UserService:
    @staticmethod
    def create_user(name, email, password):
        new_user = UserDomain(name, email, password)
        user = user(name=new_user.name, email=new_user.email, password=new_user.password)        
        db.session.add(user)
        db.session.commit()
        return user
