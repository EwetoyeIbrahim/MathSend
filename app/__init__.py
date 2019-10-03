from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

__version__ = "2.0.2"

from app import routes

