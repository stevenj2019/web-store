from application import db, login_manager
from flask_login import UserMixin 

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(25), nullable = False)
    last_name = db.Column(db.String(25), nullable = False)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(500), nullable = False)
    level = db.Column(db.String(10), nullable = False)

@login_manager.user_loader
def load_user(user):
    return User.get(user)