from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    user = os.getenv("MYSQL_ROOT_USER", "root")   # pega user
    password = os.getenv("MYSQL_ROOT_PASSWORD", "root")
    database = os.getenv("MYSQL_DATABASE", "market_management")
    port = os.getenv("MYSQL_PORT", "3306")
    host = os.getenv("MYSQL_HOST", "localhost")   # adiciona host também (pode ser mysql no docker-compose)

    database_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()