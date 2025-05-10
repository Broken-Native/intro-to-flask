# All flask extensions
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_app.database.models import user_account

login_manager = LoginManager()

db = SQLAlchemy()     

@login_manager.user_loader
def load_user(username):
    return user_account.query.filter_by(user_name = username).first()