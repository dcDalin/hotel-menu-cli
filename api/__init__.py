from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dc_dalin/Desktop/Programming/Projects/Python/Flask/hotel-menu-cli/menu.db'
db = SQLAlchemy(app)

from api.menu.views import menu
app.register_blueprint(menu)

db.create_all()
