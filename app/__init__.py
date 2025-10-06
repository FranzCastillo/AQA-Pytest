from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    # Default configuration
    app.config.update(
        SECRET_KEY='dev-key',
        TESTING=False
    )

    # Apply configuration if provided
    if config:
        app.config.update(config)

    # Register blueprints
    from app.routes import main_bp, auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
