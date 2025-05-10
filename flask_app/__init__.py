from flask import Flask
from . import authentication as auth
from extensions import db, login_manager


def create_app(app_config) -> Flask:
    # creating class instance
    app = Flask(__name__)
    
    # configure your flask app
    app.config.from_object(app_config)

    # initialise flask extensions
    db.init_app(app) #initialising database/connecting to db
    login_manager.init_app(app)


    # create our database table
    with app.app_context():
        db.create_all()
        
    # register blueprint
    app.register_blueprint(auth.bp)
    
    return app