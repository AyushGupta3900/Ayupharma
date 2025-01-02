from datetime import datetime
from ayupharma import db, login_manager
from flask_login import  UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    mobile_number= db.Column(db.String(10),unique=True)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    search = db.Column(db.String(20),nullable=False,default='')
    password = db.Column(db.String(60),nullable=False,default='')
    disease_1 = db.Column(db.String(20),nullable=False,default='')
    disease_2 = db.Column(db.String(20),nullable=False,default='')
    disease_3 = db.Column(db.String(20),nullable=False,default='')

class Disease(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    disease = db.Column(db.String(120),nullable=False)
    symptoms = db.Column(db.String(500),nullable=False)
    ayurvedic_herbs = db.Column(db.String(500),nullable=False)
    yoga_practices = db.Column(db.String(500),nullable=False)
    questions = db.Column(db.String(500),nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(20),nullable=False)
    lastname = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    mobile_number= db.Column(db.String(10),nullable=False)
    message = db.Column(db.String(100),nullable=False)