from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# Create db Globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECREAT_KEY'] = "your-secreat-key"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqllite:///doit.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.init(app)

    from app.routes.auth import auth_bp
    from app.routes.auth import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app


