from apiflask import APIFlask
from src.config.data_base import init_db
from src.Application.Dto.seller_dto import SellerRegisterSchema
from src.Application.Service.seller_service import SellerService
from src.routes import init_routes

def create_app():
    """
    Função que cria e configura a aplicação Flask.
    """
    app = APIFlask(__name__)

    init_db(app)

    init_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
