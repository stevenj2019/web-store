from application import db, login_manager
from flask_login import UserMixin 

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(500), nullable = False)

@login_manager.user_loader
def load_user(user):
    return User.get(user)