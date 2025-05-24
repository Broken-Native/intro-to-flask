# configurations for our flask app
from dotenv import load_dotenv
import os


load_dotenv()
DEFAULT_KEY = 'adfdbb97be9c054bce797b8ef9d113681acc3808fb88bed9e7b783065548654e'

class development_config:
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY") or DEFAULT_KEY
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DB") or "sqlite:///project.db"    

    MAIL_SEVER = os.getenv("MAIL_SERVER") or 'smtp.gmail.com'
    MAIL_PORT = int(os.getenv("MAIL_PORT") or 587)  
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS") or True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME") or 'hila'
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD") or 'password'
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER") or 'hila@gmail.com'
   