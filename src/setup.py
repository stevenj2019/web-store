from application import db 
from application import bcrypt
import application.models

from getpass import getpass
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from re import search

db.drop_all()

db.create_all()

default_owner = application.models.Admin(
    first_name = "Default",
    last_name = "Owner",
    email = "default@none.com",
    password = bcrypt.generate_password_hash(password='DeFauLt_PaSsW0rD'),
    level = 'owner'
)
db.session.add(default_owner)
db.session.commit()

