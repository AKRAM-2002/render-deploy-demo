import os

from flask import Flask 

from .extensions import db
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    # postgresql://calisthenics_db_w8s0_user:fRgsZRT7KsGaUblNMkjzohCALExanKUZ@dpg-csufgerqf0us738r9sbg-a.oregon-postgres.render.com/calisthenics_db_w8s0

    db.init_app(app)

    app.register_blueprint(main)

    return app