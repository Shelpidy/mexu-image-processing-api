from ..extensions.extension import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(500),nullable=False)
    email= db.Column(db.String(100),nullable=False,unique=True)

    def __init__(self,username:str,email:str,password:str):
        self.username = username
        self.password = password
        self.email = email



