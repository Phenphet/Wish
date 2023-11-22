from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = str(Config.DATABASE_FILE)

from app import views
from app import admin_views
