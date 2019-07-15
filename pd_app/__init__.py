from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from pd_app.config import Config


# Create db
db = SQLAlchemy()

# Set up encrpytion
bcrypt = Bcrypt()

# Create instance of login manager
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Cross-Site Request Forgery Protection
csrf = CSRFProtect()

# Mail
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)


    from pd_app.main.views import main
    from pd_app.users.views import users
    from pd_app.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app
