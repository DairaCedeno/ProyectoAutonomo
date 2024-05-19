# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:admin@localhost/mi_basededatos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'admin'
