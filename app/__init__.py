from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    from .dog_routes import dog_bp
    app.register_blueprint(dog_bp)

    from .cat_routes import cat_bp
    app.register_blueprint(cat_bp)

    return app