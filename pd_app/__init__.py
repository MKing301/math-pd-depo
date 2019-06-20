from flask import Flask
from pd_app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from pd_app.main.views import main
    app.register_blueprint(main)

    return app
