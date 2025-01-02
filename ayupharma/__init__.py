from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import email_validator
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '7de1b1db5a512400e05cd87eff0fbb5a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' 


login_manager.init_app(app)
from ayupharma import routes