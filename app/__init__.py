from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY')
    )

    from . import (
        home,
        catalogue,
        recipes
    )

    app.register_blueprint(home.bp)
    app.register_blueprint(catalogue.bp)
    app.register_blueprint(recipes.bp)

    return app
