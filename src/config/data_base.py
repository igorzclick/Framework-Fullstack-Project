from flask_sqlalchemy import SQLAlchemy
import os
import time

db = SQLAlchemy()

def init_db(app):
    DB_USER = os.getenv('MYSQL_USER', 'root')
    DB_PASSWORD = os.getenv('MYSQL_PASSWORD', 'root')
    DB_HOST = os.getenv('MYSQL_HOST', 'db') 
    DB_NAME = os.getenv('MYSQL_DATABASE', 'marketManagement')
    DB_PORT = os.getenv('MYSQL_PORT', '3306')
    
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        for i in range(10):
            try:
                db.create_all()
                break
            except Exception as e:
                print("Aguardando MySQL...", e)
                time.sleep(3)