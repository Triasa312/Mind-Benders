from flask import Flask
from app.database import init_db

def create_app():
    app = Flask(__name__)
    
    # Initialize the database within the application context
    with app.app_context():
        init_db()

    # Import routes and register them
    from app.routes import main
    app.register_blueprint(main)

    return app
