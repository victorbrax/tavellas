# TMP FILE!

from app import create_app
from app.extensions import db
from app.models.auth import Auth
from app.models.client import Client
from app.models.repair import Repair
from app.models.service import Service
from app.models.bike import Bike

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
